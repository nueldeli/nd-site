from django import forms
from .models import Post
from django.utils.translation import gettext_lazy as _

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'post_snippet', 'thumbnail_img', 'content')

		widgets = {
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
			'post_snippet':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Snippet'}),
			'thumbnail_img':forms.FileInput(),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing'})
		}

		labels = {
			'author':_(''),
			'title':_(''),
			'post_snippet':_(''),
			'thumbnail_img':_(''),
			'content':_('')
		}

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'post_snippet', 'thumbnail_img', 'content')

		widgets = {
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
			'post_snippet':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Snippet'}),
			'thumbnail_img':forms.FileInput(),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing'})
		}

		labels = {
			'author':_(''),
			'title':_(''),
			'post_snippet':_(''),
			'thumbnail_img':_(''),
			'content':_('')
		}