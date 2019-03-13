from django import forms
from .models import WikiArticleModel , WikiEditorModel , ArticleSideContentModel

class EditorForm(forms.ModelForm):
    class Meta:
        model = WikiEditorModel
        exclude = ['AccountLink']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = WikiArticleModel
        exclude =['DateCreated','LastEditted','User']

class SideContentForm(forms.ModelForm):
    class Meta:
        model = ArticleSideContentModel
        exclude = ['ArticleLink']