#defines URLS for blogapp
from django.urls import path
from . import views

app_name='blogapp'

urlpatterns = [
    #homepage
    path('',views.index,name='index'),
    #show all topics
    path('topics/',views.topics,name='topics'),
    #detail page for single topic
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    #newpost
    path('new_post/<int:topic_id>/',views.new_post,name='new_post'),
    #page for editing entry
    path('edit_post/<int:post_id>/',views.edit_post,name='edit_post'),
]