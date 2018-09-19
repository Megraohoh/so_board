from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    # path works for 'games', don't change-- model after it
    path('profile/<pk>/', views.get_user_profile, name='user_profile'),
    path('friend/', views.Profile_List_View.as_view(), name='list_friend'),
    path('friend/<int:pk>', views.Profile_Detail_View.as_view(), name='friend_detail'),
    path('games/<int:pk>/favorite', views.favorite_game, name='favorite_game'),
    path('games/', views.Game_List_View.as_view(), name='game_list'),
    path('games/<int:pk>/', views.Game_Detail_View.as_view(), name='game_detail'),
    path('games/<int:pk>/update', views.Game_Update_View.as_view(), name='game_update'),
    path('games/<int:pk>/delete', views.Game_Delete_View.as_view(), name='game_delete'),
    path('games/new/', views.Game_Form_View.as_view(), name='game_form'),

]