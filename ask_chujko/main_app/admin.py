from django.contrib import admin

from .models import Profile,Question, Answer, Like, Tag
# Register your models here.
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Like)
admin.site.register(Tag)

