from django.urls import path
from . import views
from .views import EditCommentView

urlpatterns = [
    path('', views.index, name='index'),
    path('wines/', views.WineList.as_view(), name='wine_list'),
    path('wines/<slug:slug>/', views.WineDetail.as_view(), name='wine_detail'),
    # Reviews
    # path(
    #     '<slug:slug>/edit_user_review/<int:user_review_id>',
    #     views.user_review_edit, name='edit_user_reviews'),
    # path(
    #     '<slug:slug>/delete_user_review/<int:user_review_id>',
    #     views.user_review_delete, name='delete_user_reviews'),
    # comments
    # path(
    #     'wines/<slug:wine_slug>/comments/add/',
    #     views.CommentCreateView.as_view(),
    #     name="comment_create"
    # ),
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
    # path('', views.ReviewList.as_view(), name='reviewlist'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
]
