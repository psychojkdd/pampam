from django.shortcuts import render,  redirect, get_object_or_404
from .models import ContentBlock, Post
from django.contrib.auth.decorators import login_required
from .forms import  RegistrationForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def home(request):
    content_blocks = ContentBlock.objects.all()
    return render(request, 'home.html', {'content_blocks': content_blocks})

def content_page(request):
    content = {
        'image_url': '/path/to/your/image.jpg',
        'description': 'Текст для категории или описания',
        'category': 'Категория страницы'
    }
    return render(request, 'content_page.html', content)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import RegistrationForm 

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
    
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_list2(request, pk):
    # Получаем конкретный контентный блок по его ID (pk)
    content_block = get_object_or_404(ContentBlock, pk=pk)
    return render(request, 'post_list2.html', {'content_block': content_block})


def search_view(request):
    query = request.GET.get('q')  # Получаем запрос из формы
    results = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)  # Фильтруем по заголовку и содержимому
    return render(request, 'search_results.html', {'results': results, 'query': query})