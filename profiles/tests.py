from django.test import TestCase

from django.test.client import Client
from .models import Profile
from django.urls import reverse
from .forms import UserRegisterForm

# Create your tests here.
class ProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = Profile.objects.create_user(
            "davitichanturia", "blah@blah.com", "chantu1@3$5"
        )
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.client.login(username="davitichanturia", password="chantu1@3$5")

    def tearDown(self):
        # delete all user affer test
        for obj in Profile.objects.all():
            obj.delete()

    def test_user_is_superuser(self):
        self.assertEqual(self.test_user.is_superuser, True)

    def test_login(self):
        login = self.client.login(username="davitichanturia", password="chantu1@3$5")
        self.failUnless(login, "Could not log in")

    def test_login_view(self):
        test_response = self.client.get(reverse("login"))
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, "profiles/login.html")

    def test_profile_view(self):

        test_response = self.client.get(reverse("profile", args=[self.test_user.id]))
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, "profiles/profile.html")

    def test_update_view(self):

        test_response = self.client.get(reverse("update", args=[self.test_user.id]))
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, "profiles/update.html")


class TestForms(TestCase):
    def test_forms(self):
        form_data = {
            "username": "someusername",
            "first_name": "firstname",
            "email": "asdfsdf@gmail.com",
            "password1": "somepass1@#4",
            "password2": "somepass1@#4",
        }
        form = UserRegisterForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_forms_invalid(self):
        form_data = {
            "username": "something",
            "email": "asdfsdf",
            "password": "somepass",
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(not form.is_valid())
