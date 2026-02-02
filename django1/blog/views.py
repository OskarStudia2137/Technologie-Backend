from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Category
from .forms import UserRegisterForm, ProfileUpdateForm

# --- WIDOKI Z ZADANIA 2 (Blog) ---

def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {
        'posts': posts, 
        'title': 'Najnowsze wpisy'
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, id):
    category = get_object_or_404(Category, id=id)
    posts = Post.objects.filter(categories=category, published=True)
    return render(request, 'blog/post_list.html', {
        'posts': posts, 
        'title': f'Kategoria: {category.name}'
    })

# --- WIDOKI Z ZADANIA 4 (Użytkownicy) ---

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto stworzone dla {username}! Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Twój profil został zaktualizowany!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'blog/profile.html', {'p_form': p_form})