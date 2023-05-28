from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)  # registering the Post model into djangoadmin interface