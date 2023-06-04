from django.urls import path
from . import views

app_name = "blog_app"
urlpatterns = [
	path("", views.index, name="index"),
	path("posts/",views.posts, name="posts"),
	path("posts/<int:post_id>/", views.post,name="post"),
	path("new_post/", views.new_post, name="new_post"),
	path("delete_post/<int:post_id>/", views.delete_post, name="delete_post"),
	path("edit/<int:post_id>/",views.edit,name="edit"),
	]
