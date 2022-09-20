from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListview.as_view(), name='post_blog'),
    path('add/', views.AddPost.as_view(), name='add_post_blog'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail_blog'),
    path('<int:pk>/edit/', views.PostEit.as_view(), name='post_edit_blog'),
    path('<int:pk>/delete/', views.PostDelete.as_view(),
         name='post_delete_blog'),
]

# urlpatterns = [
#     path('', views.Post_Blog, name='post_blog'),
#     path('add/', views.Add_Post_Blog, name='add_post_blog'),
#     path('<int:pk>/', views.Post_Detail_Blog, name='post_detail_blog'),
#     path('<int:pk>/edit', views.Post_edit_Blog, name='post_edit_blog'),
#     path('<int:pk>/delete', views.Post_Delete_Blog, name='post_delete_blog'),
# ]
