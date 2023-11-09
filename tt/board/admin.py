from django.contrib import admin
from .models import TT, Comment

@admin.register(TT)
class TTAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ['title']
    readonly_fields = ('slug',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date')
    search_fields = ['text']
