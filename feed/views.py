from django.views.generic import CreateView, DetailView,ListView
from .forms import PostCreationForm
from .models import Post,Comment
from profiles.models import Profile
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.




@method_decorator(login_required(login_url='/profiles/login'),name='dispatch')
class PostListview(ListView):

    template_name = 'feed/post_list.html'
    context_object_name = 'posts'
    model = Post
    paginate_by = 7


    def get_queryset(self):
        friend_ids = Profile.objects.filter(friends=self.request.user).only('id')
        return Post.objects.filter(profile_id__in=friend_ids)


@method_decorator(login_required(login_url='/profiles/login'),name='dispatch')
class PostCreateView(CreateView):
    template_name = 'feed/post_create.html'
    model = Post
    form_class = PostCreationForm
    success_url="/feed"


    def form_valid(self, form):
        form.instance.profile_id = self.request.user
        form.instance.image = self.request.FILES.get("image")
        return super().form_valid(form)




@method_decorator(login_required(login_url='/profiles/login'),name='dispatch')
class PostDetailView(DetailView):
    template_name = 'feed/post.html'
    model = Post
    context_object_name="post"


    def get_queryset(self):

         friend_ids = Profile.objects.filter(friends=self.request.user).only('id')
         return super().get_queryset().filter(profile_id__in=friend_ids)
            



  

    def post(self,request,*args,**kwargs):
        commet_text = request.POST.get("comment")
        post_object = self.get_object()
        comment = Comment.objects.create(author_id=self.request.user,post_id=post_object,comment=commet_text)
        comment.save()
        return redirect("post", pk=post_object.id)


 
@method_decorator(login_required(login_url='/profiles/login'),name='dispatch')
class PostRemoveView(DetailView):
    template_name = 'feed/post_list.html'
    model = Post

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs['pk'])
        print(post.profile_id.id)
        print(request.user.id)
        if post.profile_id.id == request.user.id:
            print("ddf")
            print("delete")
            post.delete()
            return redirect('posts')

        else:
            return redirect('posts')
