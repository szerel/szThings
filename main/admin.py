from django.contrib import admin
from main.models import Media_models, Comments
# from .models import Task
# from user_profile.models import Usermodel



class Amin_media(admin.ModelAdmin):
    list_display = ('id','name','title','slug', 'data_time_update', 'geeks_field')
    search_fields = ('name','title','post')
    list_filter = ('data_time_create','data_time_update')
    prepopulated_fields = {'slug':('title',)}


class Amin_group(admin.ModelAdmin):
    list_display = ('id','name', 'title', 'data_time','user_comment', 'slug', 'geeks_field')
    search_fields = ('name',)
    list_filter = ('data_time',)



admin.site.register(Media_models,Amin_media)
admin.site.register(Comments,Amin_group)
# admin.site.register(Usermodel,Amin_user)



