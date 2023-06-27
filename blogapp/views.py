from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.shortcuts import render
from blogapp.models import Topic,Post
from .forms import TopicForm,PostForm
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #home page for blogapp
    return render(request,'blogapp/index.html')

@login_required
def topics(request):
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics':topics}
    return render(request,'blogapp/topics.html',context)

@login_required
def topic(request, topic_id):
    #Show a single topic and all its entries.
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    posts = topic.post_set.order_by('publication_date')

    context = {'topic': topic, 'posts': posts}

    return render(request, 'blogapp/topic.html', context)

@login_required
def new_topic(request):
    #Add a topic
    if request.method!='POST':
        #create a blank form
        form=TopicForm()
    else:
        #POST data submitted
        form=TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()
            return HttpResponseRedirect(reverse('blogapp:topics'))
        
    context={'form':form}
    return render(request,'blogapp/new_topic.html',context)


@login_required
def new_post(request,topic_id):
        #add new post for a topic
        topic=Topic.objects.get(id=topic_id)
        if topic.owner != request.user:
            raise Http404

        if request.method!='POST':
            #Create blank form if no data submitted
            form=PostForm()
        else:
            #process data
            form = PostForm(request.POST)
            if form.is_valid():
                new_post=form.save(commit=False)
                new_post.topic=topic
                new_post.save()
                return HttpResponseRedirect(reverse('blogapp:topic',args=[topic_id]))

        context={'topic':topic,'form':form} 
        return render(request,'blogapp/new_post.html',context)

@login_required
def edit_post(request,post_id):
    #edit existing post
    post=Post.objects.get(id=post_id)
    topic=post.topic
    if topic.owner != request.user:
        raise Http404

    if request.method!='POST':
        #initial request:pre-fill form with current post
        form=PostForm(instance=post)
    else:
        #POST data submitted and process data
        form=PostForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogapp:topic',args=[topic.id]))
    context={'post':post,'topic':topic,'form':form}
    return render(request,'blogapp/edit_post.html',context)
        

