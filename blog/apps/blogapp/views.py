from django.shortcuts import render
from django.shortcuts import get_object_or_404 as go404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .utils import *
from .forms import *
# from django.shortcuts import render_to_response
# from django.template import RequestContext


class Index(ObjListMix, View):
    model = Post
    template = 'blogapp/index.html'


class tag_list(ObjListMix, View):
    model = Tag
    template = 'blogapp/taglist.html'


class tag_detail(ObjDetMix, View):
    model = Tag
    template = 'blogapp/tag_det.html'


class tag_new(NewObjMix, View):
    model_form = TagForm
    template = 'blogapp/tag_new.html'

class tag_edit(EditObjMix, View):
    model = Tag
    model_form = TagForm
    template = 'blogapp/tag_edit.html'
    
class tag_delete(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        try:
            return render_to_response('/', {'tag': tag}, context_instance=RequestContext(request))
        except:
            return render(request, 'blogapp/taglist.html', context={'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tag_list'))


class post_new(NewObjMix, View):
    model_form = PostForm
    template = 'blogapp/post_new.html'


class PostDatail(ObjDetMix, View):
    model = Post
    template = 'blogapp/article.html' 

class post_edit(EditObjMix, View):
    model = Post
    model_form = PostForm
    template = 'blogapp/post_edit.html'
    

def Error_404(request, exception):
    return render(request, 'blogapp/404.html' )
