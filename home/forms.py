from django import forms
from .models import Message, Comment, EmailSend


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailSend
        fields = ('email',)