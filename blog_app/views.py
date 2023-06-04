from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
# Create your views here.

def index(request):
	"""Home Page"""
	return render(request,"blog_app/index.html")

def posts(request):
	posts = Blog.objects.all()
	context= {"posts":posts}
	return render(request, "blog_app/posts.html",context)

def post(request, post_id):
	post = Blog.objects.get(id= post_id)
	context = {"post": post}
	return render(request, "blog_app/post.html", context)

def new_post(request):
	if request.method != "POST":
		form = BlogForm
		context = {"form": form}
	else:
		form = BlogForm(request.POST)
		if form.is_valid():
			form.title = form["title"]
			form.content = form["content"]
			form.save()
			return redirect("blog_app:posts")
	
	return render(request, "blog_app/new_post.html", context)

def delete_post(request, post_id):
	post = Blog.objects.get(id=post_id)
	post.delete()
	return redirect("blog_app:posts")
def edit(request, post_id):
	post=Blog.objects.get(id=post_id)
	if request.method != "POST":
		form = BlogForm(instance=post)
	else:
		form=BlogForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect ("blog_app:posts")
	context={"form":form, "post":post}
	return render(request, "blog_app/edit.html",context)

	
