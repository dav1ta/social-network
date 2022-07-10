from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# Register your models here.








class AdminProfiles(UserAdmin):
    model = Profile
    list_display = ('email','first_name','last_name')
    list_filter = ('email','first_name','last_name')
    search_fields =  ('email','first_name','last_name')
    ordering = ('email','first_name')

  

admin.site.register(Profile,AdminProfiles)
