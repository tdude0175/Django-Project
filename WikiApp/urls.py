from django.urls import path
from . import views

urlpatterns = \
    [
        path('', views.index, name='index'),
        path('NewUser/', views.createNewUser, name='NewUser'),
        path('NewArticle/', views.createNewArticle, name='NewArticle'),
        path('EditArticle/<int:articleID>/', views.editArticle, name='EditArticle'),
        path('DeleteArticle/<int:articleID>/', views.deleteArticle, name='DeleteArticle'),
        path('ReadArticle/<int:articleID>', views.renderArticle, name='ReadArticle'),
        path('ListUserArticles/',views.userArticleList,name='ListUserArticles'),
    ]
