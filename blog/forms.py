from django import forms
from .models import Comment


#
class CommentForm(forms.ModelForm):
    class Meta:
        # get the profile model
        model = Comment
        # specify the fields
        fields = ['content']
