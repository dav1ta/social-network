from django import forms
from .models import Post



class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','title','description']

        widgets = {
          'description': forms.Textarea(attrs={'rows':6, 'cols':15}),
        }
