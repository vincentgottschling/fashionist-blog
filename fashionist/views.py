from django.shortcuts import render
from django.utils import timezone
from .models import Post, About_Me, Events
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, InfoForm, EventsForm
from django.shortcuts import redirect


#Neuen Beitrag erstellen
def new_news(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'fashionist/news_edit.html', {'form': form})

#Detailansicht des Beitrags
def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'fashionist/news_detail.html', {'post': post})

#Beitrag bearbeiten
def news_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,    request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'fashionist/news_edit.html', {'form': form})


#Startseite - Übersicht über Blogeinträge
def frontpage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    query=request.GET.get("q")
    if query:
        posts=posts.filter(category=query)
    return render(request, 'fashionist/frontpage.html', {'posts': posts})

#Seite zur Nutzerin des Blogs, Bild und Text können hier hochgeladen werden
#Erstellter Objekt des Models About_Me wird immer mit pk=1 gespeichert, da es nur eine Nutzerin gibt
def about_me(request):
    if not About_Me.objects.filter(pk=1).exists():
        if request.method == "POST":
            form = InfoForm(request.POST, request.FILES)
            if form.is_valid():
                info = form.save(commit=False)
                info.pk=1
                info.save()
                return redirect('about_me')
        else:
            form = InfoForm()
        return render(request, 'fashionist/edit_info.html', {'form': form})
    else:
        info=About_Me.objects.get(pk=1)
        return render(request, 'fashionist/about_me.html', {'info': info})

#About_Me bearbeiten
def edit_info(request):
        info = get_object_or_404(About_Me, pk=1)
        if request.method == "POST":
            form = InfoForm(request.POST, request.FILES, instance=info)
            if form.is_valid():
                info = form.save(commit=False)
                info.save()
                return redirect('about_me')
        else:
            form = InfoForm(instance=info)
        return render(request, 'fashionist/edit_info.html', {'form': form})

#Eventpage
def events(request):
    events = Events.objects.filter(event_date__gte=timezone.now()).order_by('event_date')
    return render(request, 'fashionist/events.html', {'events': events})

#Event erstellen
def new_events(request):
    if request.method == "POST":
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            events = form.save(commit=False)
            events.author = request.user
            events.save()
            return redirect('events')
    else:
        form = EventsForm()
    return render(request, 'fashionist/events_edit.html', {'form': form})

#Event bearbeiten
def events_edit(request, pk):
    event = get_object_or_404(Events, pk=pk)
    if request.method == "POST":
        form = EventsForm(request.POST, request.FILES,instance=event)
        if form.is_valid():
            events = form.save(commit=False)
            events.author = request.user
            events.save()
            return redirect('events')
    else:
        form = EventsForm(instance=event)
    return render(request, 'fashionist/events_edit.html', {'form': form})
