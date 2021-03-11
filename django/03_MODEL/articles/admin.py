from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at')

admin.site.register(Article,ArticleAdmin)  #관리자 계정에 등록하겟다