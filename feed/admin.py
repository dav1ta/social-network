from django.contrib import admin

# Register your models here.



from .models import Post,Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ('profile_id','title','date_published')
    list_filter = ('profile_id','title','date_published')
    search_fields =  ('profile_id','title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post_id','author_id','date_commented')
    list_filter= ('post_id','author_id','date_commented')
    search_fields =  ('post_id','author_id',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
