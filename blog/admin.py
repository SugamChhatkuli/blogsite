from django.contrib import admin
from .models import Blog, Profile
# Register your models here.

@admin.register(Blog)
class blogAdmin(admin.ModelAdmin):

    list_display = ['id','title','desc','banner_img','author']
    class Meta:
        model =Blog


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
        list_display = ['id','user','address','contract','profile_img']
    


