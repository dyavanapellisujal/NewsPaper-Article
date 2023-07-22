from django.contrib import admin
from .models import Articles, Comment


class CommentInline(admin.TabularInline):  # new
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):  # new
    inlines = [
        CommentInline,
    ]


admin.site.register(Articles, ArticleAdmin)  # new
admin.site.register(Comment)
