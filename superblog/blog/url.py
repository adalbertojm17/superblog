
from django.urls import path
from .views import HomeView, ArticlesView, AddPostView,EditPost, DeletePostView, CategoryView, CategoryListView,LikeView,AddCommentView

urlpatterns = [
 path('', HomeView.as_view(),name="home"),
 path('article/<int:pk>',ArticlesView.as_view(),name ='article'),
 path('add_post/', AddPostView.as_view(),name='add_post'),
 path('post/edit/<int:pk>',EditPost.as_view(),name ='edit_post'),
 path('category/<str:cats>/',CategoryView,name='category'),
 path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
 path('category_list/',CategoryListView, name = 'category_list'),
 path('like/<int:pk>', LikeView, name='like_post'),
 path('article/<int:pk>/comment/', AddCommentView.as_view(),name='add_comment'),


]