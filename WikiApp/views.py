from django.shortcuts import render , redirect , get_object_or_404

# Create your views here.

def index(request):
    return render(request,'WikiApp/index.html',)

def createNewUser(request):
    return render(request,'WikiApp/NewUser.html',)

def createNewArticle(request):
    return render(request,'WikiApp/NewArticle.html',)

def editArticle(request, articleID):
    return render(request,'WikiApp/EditArticle.html',)

def deleteArticle(request, articleID):
    return render(request,'WikiApp/DeleteArticle.html',)

def renderArticle(request, articleID):
    return render(request,'WikiApp/ReadArticle.html',)

def userArticleList(request):
    return render(request,'WikiApp/UserArticleList.html',)