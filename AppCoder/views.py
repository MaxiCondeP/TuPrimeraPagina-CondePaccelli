from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Post, User, Category
from .forms import UserForm, CategoryForm, PostForm, CommentForm, SearchForm

def home(request):
    posts = Post.objects.select_related("author", "category").order_by("-date")[:5]
    return render(request, "AppCoder/home.html", {"posts": posts})

def user_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Autor creado con éxito.")
        return redirect("home")
    return render(request, "AppCoder/user_create.html", {"form": form})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Categoría creada con éxito.")
        return redirect("home")
    return render(request, "AppCoder/category_create.html", {"form": form})

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Post creado con éxito.")
        return redirect("home")
    return render(request, "AppCoder/post_create.html", {"form": form})

def comment_create(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Comentario creado con éxito.")
        return redirect("home")
    return render(request, "AppCoder/comment_create.html", {"form": form})

def search(request):
    form = SearchForm(request.GET or None)
    results, selected = None, None
    if form.is_valid():
        selected = form.cleaned_data["target"]
        q = form.cleaned_data["q"].strip()
        if selected == "post":
            qs = Post.objects.select_related("author", "category")
            if q: qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))
            results = qs.order_by("-date")
        elif selected == "author":
            qs = User.objects.all()
            if q: qs = qs.filter(
                Q(username__icontains=q) | Q(name__icontains=q) |
                Q(surname__icontains=q) | Q(email__icontains=q)
            )
            results = qs.order_by("username")
        else:  # "category"
            qs = Category.objects.all()
            if q: qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))
            results = qs.order_by("name")
    return render(request, "AppCoder/search.html", {
        "form": form,
        "results": results if form.is_bound else None,
        "selected": selected,
    })
