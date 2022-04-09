from django.contrib import admin
from .models import PostModel, TestModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(TestModel)
