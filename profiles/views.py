from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, UserUpdateForm

from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView

# Create your views here.

from django.utils.decorators import method_decorator
from .models import Profile
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse
from django.urls import reverse


class UserLoginView(LoginView):
    template_name = "profiles/login.html"


class UserLogoutView(LogoutView):
    template_name = "profiles/login.html"


class UserRegisterView(CreateView):
    template_name = "profiles/register.html"
    form_class = UserRegisterForm
    success_url = "/profiles/login"

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


@method_decorator(login_required(login_url="/profiles/login"), name="dispatch")
class UserProfile(DetailView):
    template_name = "profiles/profile.html"
    model = Profile
    success_url = "/profiles/login"
    context_object_name = "profile"


@method_decorator(login_required(login_url="/profiles/login"), name="dispatch")
class UserUpdateView(UpdateView):
    template_name = "profiles/update.html"
    model = Profile
    form_class = UserUpdateForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if form.instance.pk == self.request.user.id:
            return super().form_valid(form)
        return HttpResponse("Forbidden")

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="/profiles/login"), name="dispatch")
class AddFriendsView(ListView):
    template_name = "profiles/profile_list.html"
    context_object_name = "profiles"
    model = Profile
    paginate_by = 5

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)
        self._toggle_friend(request_data.get("user_id"), request.user.id)
        return HttpResponse(request_data.get("user_id"))

    def _toggle_friend(self, friend_pk, user_pk):
        current_user = Profile.objects.get(pk=user_pk)
        profile = Profile.objects.get(pk=friend_pk)
        if profile in current_user.cached_friends.all():
            current_user.friends.remove(profile)
        else:
            current_user.friends.add(profile)


@method_decorator(login_required(login_url="/profiles/login"), name="dispatch")
class FriendListView(ListView):
    template_name = "profiles/profile_list.html"
    context_object_name = "profiles"
    model = Profile
    paginate_by = 5

    def get_queryset(self):
        return Profile.objects.get(pk=self.request.user.id).friends.all()
