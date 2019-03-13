from django.contrib import admin
from .forms import WikiEditorModel , ArticleSideContentModel , WikiArticleModel
# Register your models here.

admin.site.register(WikiArticleModel)
admin.site.register(WikiEditorModel)
admin.site.register(ArticleSideContentModel)