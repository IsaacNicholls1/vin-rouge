from django.urls import path
from . import views
from .views import EditWineReviewView

urlpatterns = [
    path('', views.index, name='index'),
    path('wines/', views.WineList.as_view(), name='wine_list'),
    path('wines/<slug:slug>/', views.WineDetail.as_view(), name='wine_detail'),
    path(
        'wines/<slug:wine_slug>/winereview/add/',
        views.WineReviewCreateView.as_view(),
        name='comment_create'
    ),
    path(
        'winereview/<int:pk>/edit/',
        EditWineReviewView.as_view(),
        name='edit_winereview'
    ),
    path(
        'winereview/delete/<int:winereview_id>/',
        views.delete_comment,
        name='delete_comment'
    ),
]
