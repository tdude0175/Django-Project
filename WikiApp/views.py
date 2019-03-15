from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleSideContentModel, WikiEditorModel, \
    WikiArticleModel, ArticleForm, EditorForm, SideContentForm
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
# index Lists first seven articles to display i may rework it to display
def index(request):
    fullArticleList = WikiArticleModel.objects.all()  # grabs all articles made may add a limit to how many grabbed
    fullSideContentList = ArticleSideContentModel.objects.all()
    context = \
        {
            'ArticleList': fullArticleList,
            'SideContentList': fullSideContentList
        }
    return render(request, 'WikiApp/index.html', context)


# Gets the form for a new user to Put their information in
def createNewUser(request):
    NewUserForm = EditorForm()
    context = \
        {
            'UserForm': NewUserForm
        }
    return render(request, 'WikiApp/NewUser.html', context)


# Saves the form and makes the users page info to use
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


# if you want to make a new article you need to be signed in and you cna optionally put in sidecontent
# and on submitting the form it reruns this program and saves the article with the stuff.
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


# Gathers the articles information and all the sidecontent of that information to display
def renderArticle(request, articleID):
    ArticleToView = get_object_or_404(WikiArticleModel, pk=articleID)
    ArticleSideContent = ArticleSideContentModel.objects.filter(ArticleLink=ArticleToView)
    context = \
        {
            'article': ArticleToView,
            'sideContent': ArticleSideContent
        }
    return render(request, 'WikiApp/ReadArticle.html', context)


# simply deletes the article and it cascades to side content as well
@login_required
def deleteArticle(request, articleID):
    ArticleToDelete = get_object_or_404(WikiArticleModel, pk=articleID)
    ArticleToDelete.delete()
    return render(request, 'WikiApp/DeleteArticle.html', )


# to edit an article it gathers the article and form and fills out the form and then from there you can select the
# sidecontent
# you want to edit or if you want to add a new side content
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
                'sideContentList': ListOfSideContent,
                'article': ArticleToEdit
            }
        return render(request, 'WikiApp/EditArticle.html', context)
    context = \
        {
            'articleForm': formToAllowArticleEditing,
            'sideContentList': ListOfSideContent,
            'article': ArticleToEdit
        }
    return render(request, 'WikiApp/EditArticle.html', context)


# list of articles ther person signed in wants to make
@login_required
def userArticleList(request):
    wikiEditor = WikiEditorModel.objects.get(Accountlink=request.user)
    listofArticles = WikiArticleModel.objects.filter(User=wikiEditor)
    context = \
        {
            'articleList': listofArticles
        }
    return render(request, 'WikiApp/UserArticleList.html', context)


# Renders from edit article page with a link back to the article you were editing
@login_required
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


# form to add new sidecontent and takes the id of the article you are editing to add it as the foriegn key
@login_required
def NewSideContent(request, articleID):
    SideContent = SideContentForm(request.POST or None, request.FILES or None)
    ArticleToLink = get_object_or_404(WikiArticleModel, pk=articleID)
    print(ArticleToLink)
    if request.method == 'POST' and SideContent.is_valid():
        SideContentToSave = SideContent.save(commit=None)
        SideContentToSave.ArticleLink = ArticleToLink
        print(SideContentToSave)
        SideContentToSave.save()
        return redirect('index')
    context = \
        {
            'sideContentForm': SideContent,
            'article': ArticleToLink
        }
    return render(request, 'WikiApp/NewSideContent.html', context)


# deleteing side content works the same way that article delete does but it won't cascade
@login_required
def deleteSideContent(request, sideContentID):
    sideContentToDelete = get_object_or_404(ArticleSideContentModel, pk=sideContentID)
    ArticleToLink = get_object_or_404(WikiArticleModel, articlesidecontentmodel=sideContentToDelete)
    sideContentToDelete.delete()
    return redirect('EditArticle', articleID=ArticleToLink.id)


# filters through the wiki with search requirements and filters out body title and sidecontent title and body and renders them as clickable links
def SearchWiki(request):
    contentToShow = WikiArticleModel.objects.filter(
        Q(Title__contains=request.POST['SearchText']) | Q(Body__contains=request.POST['SearchText']))
    SideContentToShow = ArticleSideContentModel.objects.filter(
        Q(SideTitle__contains=request.POST['SearchText']) | Q(SideBody__contains=request.POST['SearchText']))
    print(contentToShow)
    print(SideContentToShow)
    context = \
        {
            'articleContent': contentToShow,
            'SideContent': SideContentToShow
        }
    return render(request, 'WikiApp/SearchWiki.html', context)
