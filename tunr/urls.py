from django.urls import path
from . import views
from django.urls import reverse
urlpatterns = [
    #path('', views.artist_list, name='artist_list'),
    path('', views.ArtistList.as_view(), name='artist_list'),
    #path('songs/', views.song_list, name='song_list'),
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    #path('songs/<int:pk>', views.song_detail, name='song_detail'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
    # path('artists/new', views.artist_create, name='artist_create'),
    path('artists/new', views.ArtistCreate.as_view(), name='artist_create'),
    #path('songs/new', views.song_create, name='song_create'),
    path('songs/new', views.SongCreate.as_view(), name='song_create'),
    path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
    #path('songs/<int:pk>/edit', views.song_edit, name='song_edit'),
    path('songs/<int:pk>/edit', views.SongEdit.as_view(), name='song_edit'),
    #path('songs/<int:pk>/delete', views.song_delete, name='song_delete'),
    path('songs/<int:pk>/delete', views.SongDelete.as_view(), name='song_delete'),
    path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
]
