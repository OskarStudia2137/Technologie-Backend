from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts, 'title': 'Najnowsze posty'})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, id):
    category = get_object_or_404(Category, id=id)
    posts = Post.objects.filter(categories=category, published=True)
    return render(request, 'blog/post_list.html', {'posts': posts, 'title': f'Kategoria: {category.name}'})