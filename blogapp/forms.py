from django import forms
from . models import Topic,Post

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['topic']
        labels={'topic':''}

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','post']
        labels={'title':'Title','post':'Post'}
        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
            'post': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post', 'rows': 8})
        }


