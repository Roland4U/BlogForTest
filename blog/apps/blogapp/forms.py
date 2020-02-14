from django import forms
from django.core.exceptions import ValidationError
from django.core.exceptions import MultipleObjectsReturned
from .models import Tag, Post
from django.db.utils import IntegrityError

class TagForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # slug = forms.SlugField(max_length=50)

    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        # tag = Tag.objects.all()
        if new_slug == 'new':
            raise ValidationError('Slug may not be "new"')

        elif Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug alredy!'.format(str(new_slug).title()))
        return new_slug


    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data['title'], 
    #         slug=self.cleaned_data['slug']
    #     )
    #     return new_tag
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            # 'pub_date': forms.DateTimeField(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        
        if new_slug == 'new':
            raise ValidationError('Slug may not be "new"')

        # elif Post.objects.filter(slug__iexact=new_slug).count():
        #     raise ValidationError('Slug must be unique. We have "{}" slug alredy!'.format(str(new_slug).title()))

        return new_slug