from django.contrib import admin
from myblog.models import Post, Category

# class CategoryInline(admin.TabularInline):
#     model = Post.categorys.through

class PostAdmin(admin.ModelAdmin):
  # inlines = [
  #   CategoryInline
  # ]
  pass

class CategoryAdmin(admin.ModelAdmin):
  pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category)