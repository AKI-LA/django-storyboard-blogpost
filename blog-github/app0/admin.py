from django.contrib import admin
from .models import Post, Comment

# Post Admin Customization
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)

# Comment Admin Customization
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    search_fields = ('post__title', 'user__username', 'body')
    list_filter = ('created_at',)


