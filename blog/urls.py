from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewList.as_view(), name='home'),  # Update the path for the review list
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
