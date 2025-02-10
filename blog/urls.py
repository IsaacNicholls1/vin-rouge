from django.urls import path
from . import views
from .views import EditCommentView

urlpatterns = [
    path('', views.index, name='index'),
    path('wines/', views.WineList.as_view(), name='wine_list'),
    path('wines/<slug:slug>/', views.WineDetail.as_view(), name='wine_detail'),
    path(
        'wines/<slug:wine_slug>/comments/add/',
        views.CommentCreateView.as_view(),
        name='comment_create'
    ),
    path(
        'comment/<int:pk>/edit/',
        EditCommentView.as_view(),
        name='edit_comment'
    ),
    path(
        'comment/delete/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment'
    ),
]
