from django import forms
from .models import Post, Category,Comment

choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "category","body","snippet","header_image")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'user','type': 'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body","snippet")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name',"body",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user',}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),


        }