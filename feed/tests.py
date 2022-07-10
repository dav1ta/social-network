from django.test import TestCase
from django.test.client import Client
from .models import Post
from profiles.models import Profile
from django.urls import reverse
from .forms import PostCreationForm


# Create your tests here.
class FeedTests(TestCase):


    def setUp(self):
        self.client = Client()
        self.test_user = Profile.objects.create_user('davitichanturia', 'blah@blah.com', 'chantu1@3$5')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.client.login(username='davitichanturia', password='chantu1@3$5')

    def tearDown(self):
        for obj in Profile.objects.all():
            obj.delete()
        for obj in Post.objects.all():
            obj.delete()

    def test_feed_view(self):
        test_response = self.client.get(reverse('posts'))
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, 'feed/post_list.html')

    # def test_add_comment(self):
    #     post = Post.objects.create(title="david",profile_id=self.test_user)
    #     post.save()
    #     test_response = self.client.post(reverse('post',args=[post.id]) ,{"comment":"my comment"})
    #     self.assertEqual(len(post.comments.all),1)
    #     self.assertEqual(test_response.status_code, 200)


class TestForms(TestCase):

    def test_forms(self):
        form_data = {'title': 'something','description':'something'}
        form = PostCreationForm(data=form_data)
        self.assertTrue(form.is_valid()) 



