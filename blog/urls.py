from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),

     path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('south-west/', views.south_west, name='south_west'),
    path('wine-review-2/', views.wine_review_2, name='wine_review_2'),
    path('wine-review-3/', views.wine_review_3, name='wine_review_3'),
    path('wine-review-4/', views.wine_review_4, name='wine_review_4'),
    path('wine-review-5/', views.wine_review_5, name='wine_review_5'),
]