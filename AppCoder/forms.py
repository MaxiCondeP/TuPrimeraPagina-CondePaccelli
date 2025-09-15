# AppCoder/forms.py
from django import forms
from .models import User, Category, Post, Comment

# Opciones para el buscador
TARGET_CHOICES = [
    ("post", "Posts (por título o contenido)"),
    ("author", "Autores"),
    ("category", "Categorías"),
]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "name", "surname", "email"]
        labels = {
            "username": "Usuario",
            "name": "Nombre",
            "surname": "Apellido",
            "email": "Correo electrónico",
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "usuario"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "surname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "nombre@ejemplo.com"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        labels = {"name": "Categoría", "description": "Descripción"}
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de la categoría"}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Descripción (opcional)"}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author", "category"]  
        labels = {
            "title": "Título",
            "content": "Contenido",
            "author": "Autor",
            "category": "Categoría",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Escribí el contenido..."}),
            "author": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["author"].empty_label = "Seleccioná un autor"
        self.fields["category"].empty_label = "Seleccioná una categoría"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["post", "author", "content"]
        labels = {"post": "Post", "author": "Autor", "content": "Comentario"}
        widgets = {
            "post": forms.Select(attrs={"class": "form-select"}),
            "author": forms.Select(attrs={"class": "form-select"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Escribí tu comentario"}),
        }


class SearchForm(forms.Form):
    target = forms.ChoiceField(
        label="Dónde buscar",
        choices=TARGET_CHOICES,
        initial="post",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    q = forms.CharField(
        label="Buscar",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribí algo..."}),
    )
