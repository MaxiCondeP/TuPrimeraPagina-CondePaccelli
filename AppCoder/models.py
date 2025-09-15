from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.email})"
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="posts",  null=True, blank=True,
    )
    def __str__(self):
        return f"{self.title} - {self.author}"


    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)