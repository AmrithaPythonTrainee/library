from . import views
from django.urls import path,include,re_path
from .views import addBookView,addBook,editBook,editBookView,deleteBookView,index1
urlpatterns = [
    path('',views.index),
    path("loginandregister.html",index1),
    path('add-book/',addBookView),
    re_path('add-book/add',addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView),
  ]
