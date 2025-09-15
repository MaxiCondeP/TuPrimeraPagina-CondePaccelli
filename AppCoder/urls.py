from django.urls import path
from .views import home, search,user_create, category_create, post_create, comment_create



urlpatterns = [
    path("", home, name="home"),
    path("buscar/", search, name="search"),
    path("autor/", user_create, name="author_create"),
    path("categorias/", category_create, name="category_create"),
    path("posts/", post_create, name="post_create"),
    path("comentarios/", comment_create, name="comment_create"),
]
