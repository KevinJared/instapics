from django import forms
from .models import *

class NewPostForm(forms.ModelForm):
    class Meta :
        model = Post
        exclude = ['user', 'post_date','liker']

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','user_name','bio')

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget=forms.TextInput()
        self.fields['text'].widget.attrs['placeholder']='Add a comment...'

    class Meta:
        model = Comment
        fields = ('text',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


