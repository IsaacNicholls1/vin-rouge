from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.ReviewList.as_view(), name='reviewlist'),
    path('wines/', views.WineList.as_view(), name='wine_list'),
    path('wines/<slug:slug>/', views.WineDetail.as_view(), name='wine_detail'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
    path(
        '<slug:slug>/edit_user_review/<int:user_review_id>',
        views.user_review_edit, name='edit_user_reviews'),
    path(
        '<slug:slug>/delete_user_review/<int:user_review_id>',
        views.user_review_delete, name='delete_user_reviews'),
]
