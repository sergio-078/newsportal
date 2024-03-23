from django.urls import path
from . import views
from .views import PostDetail, PostList, PostCreate, PostSearch
from .forms import PostForm

urlpatterns = [
    #path('', views.home_func, name='newslist-home'),
    path('', PostList.as_view(), name='post_list'),
    #path('about/', views.about_func, name='about_portal'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    #path('addpost/', views.add_post_func, name='addPost'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('search/', PostSearch.as_view(), name='news_search'),

]
