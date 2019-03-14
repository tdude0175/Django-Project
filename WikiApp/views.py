from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleSideContentModel, WikiEditorModel, \
    WikiArticleModel, ArticleForm, EditorForm, SideContentForm
from django.contrib.auth.models import User
from django.utils import timezone


# Create your views here.

def index(request):
    fullArticleList = WikiArticleModel.objects.all()  # grabs all articles made may add a limit to how many grabbed
    context = \
        {
            'ArticleList': fullArticleList
        }
    return render(request, 'WikiApp/index.html', context)


def createNewUser(request):
    NewUserForm = EditorForm()
    context = \
        {
            'UserForm': NewUserForm
        }
    return render(request, 'WikiApp/NewUser.html', context)


def SaveNewUser(request):
    newUserRequest = EditorForm(request.POST)
    if newUserRequest.is_valid():
        NewUser = newUserRequest.save(commit=None)
        userLink = User.objects.create_user(request.POST['Username'], request.POST['Email'], request.POST['Password'])
        NewUser.Accountlink = userLink
        NewUser.save()
        return redirect('index')
    else:
        context = \
            {
                'UserForm': newUserRequest
            }
        return render(request, 'WikiApp/NewUser.html', context)


@login_required
def createNewArticle(request):
    NewArticle = ArticleForm(request.POST or None, request.FILES or None)
    SideContent = SideContentForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and NewArticle.is_valid():
        CompleteArticle = NewArticle.save(commit=None)
        ArticleCreator = WikiEditorModel.objects.get(Accountlink=request.user)
        CompleteArticle.User = ArticleCreator
        CompleteArticle.save()
        if SideContent.is_valid() and request.POST['SideTitle'] != '':
            contentToSave = SideContent.save(commit=None)
            contentToSave.ArticleLink = CompleteArticle
            contentToSave.save()
            return redirect('index')
        else:
            return redirect('index')
    context = \
        {
            'Articleform': NewArticle,
            'SideContentform': SideContent
        }
    return render(request, 'WikiApp/NewArticle.html', context)


def renderArticle(request, articleID):
    ArticleToView = get_object_or_404(WikiArticleModel, pk=articleID)
    ArticleSideContent = ArticleSideContentModel.objects.filter(ArticleLink=ArticleToView)
    context = \
        {
            'article': ArticleToView,
            'sideContent': ArticleSideContent
        }
    return render(request, 'WikiApp/ReadArticle.html', context)


@login_required
def deleteArticle(request, articleID):
    ArticleToDelete = get_object_or_404(WikiArticleModel, pk=articleID)
    ArticleToDelete.delete()
    return render(request, 'WikiApp/DeleteArticle.html', )


@login_required
def editArticle(request, articleID):
    ArticleToEdit = get_object_or_404(WikiArticleModel, pk=articleID)
    formToAllowArticleEditing = ArticleForm(request.POST or None, request.FILES or None, instance=ArticleToEdit)
    ListOfSideContent = ArticleSideContentModel.objects.filter(ArticleLink=ArticleToEdit)
    if request.method == 'POST' and formToAllowArticleEditing.is_valid():
        formToAllowArticleEditing.Image = request.FILES
        formToAllowArticleEditing.save()
        context = \
            {
                'articleForm': formToAllowArticleEditing,
                'sideContentList': ListOfSideContent
            }
        return render(request, 'WikiApp/EditArticle.html', context)
    context = \
        {
            'articleForm': formToAllowArticleEditing,
            'sideContentList': ListOfSideContent
        }
    return render(request, 'WikiApp/EditArticle.html', context)


@login_required
def userArticleList(request):
    wikiEditor = WikiEditorModel.objects.get(Accountlink=request.user)
    listofArticles = WikiArticleModel.objects.filter(User=wikiEditor)
    context = \
        {
            'articleList': listofArticles
        }
    return render(request, 'WikiApp/UserArticleList.html', context)


def EditSideContent(request, sideContentID):
    SideContentToEdit = get_object_or_404(ArticleSideContentModel, pk=sideContentID)
    ArticleToGet = WikiArticleModel.objects.get(articlesidecontentmodel=SideContentToEdit)
    SideContentWithForm = SideContentForm(request.POST or None, request.FILES or None, instance=SideContentToEdit)
    if request.method == 'POST' and SideContentWithForm.is_valid():
        SideContentWithForm.SidePicture = request.FILES
        SideContentWithForm.save()
        context = \
            {
                'sideContentForm': SideContentWithForm,
                'article': ArticleToGet
            }
        return render(request, 'WikiApp/EditSideContent.html', context)
    context = \
        {
            'article': ArticleToGet,
            'sideContentForm': SideContentWithForm
        }
    return render(request, 'WikiApp/EditSideContent.html', context)


def NewSideContent(request):
    SideContent = SideContentForm(request.POST or None, request.FILES or None)
    ArticleToLink = WikiArticleModel.objects.get()
    if request.method == 'POST' and SideContent.is_valid():
        SideContentToSave = SideContent.save(commit=None)
        print(SideContentToSave)
        SideContentToSave.save()
        return redirect('index')
    context = \
        {
            'sideContentForm': SideContent
        }
    return render(request, 'WikiApp/NewSideContent.html', context)


def SearchWiki(request):
    return render(request, 'WikiApp/index.html')
