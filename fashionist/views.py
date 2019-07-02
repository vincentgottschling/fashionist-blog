from django.shortcuts import render
from django.utils import timezone
from .models import Post, About_Me
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, InfoForm
from django.shortcuts import redirect


def frontpage(request):
    return render(request, 'fashionist/frontpage.html')

def trends(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    isEvenNumber={}
    return render(request, 'fashionist/trends.html', {'posts': posts,'isEvenNumber':isEvenNumber})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'fashionist/news_detail.html', {'post': post})

def new_news(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'fashionist/news_edit.html', {'form': form})

def news_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'fashionist/news_edit.html', {'form': form})

def about_me(request):
    info=About_Me.objects.get(pk=1)
    return render(request, 'fashionist/about_me.html', {'info': info})

def edit_info(request):
    if not About_Me.objects.filter(pk=1).exists():
        if request.method == "POST":
            form = InfoForm(request.POST)
            if form.is_valid():
                info = form.save(commit=False)
                info.save()
                return redirect('about_me')
        else:
            form = InfoForm()
        return render(request, 'fashionist/edit_info.html', {'form': form})
    else: 
        info = get_object_or_404(About_Me, pk=1)
        if request.method == "POST":
            form = InfoForm(request.POST, instance=info)
            if form.is_valid():
                info = form.save(commit=False)
                info.save()
                return redirect('about_me')
        else:
            form = InfoForm(instance=info)
        return render(request, 'fashionist/edit_info.html', {'form': form})




