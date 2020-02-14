from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404 as go404
from .models import *
from .forms import *

class ObjDetMix:
    model = None
    template = None
    context = None

    def get(self, request, slug):
        if self.context:
            return self.context
        else:
            self.context = self.model.__name__.lower()
        obj = go404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.context: obj})


class ObjListMix:
    model = None
    template = None

    def get(self, request):
        conmod = self.model.__name__.lower() + 's'
        obj = self.model.objects.all()
        return render(request, self.template, context={conmod: obj})


class NewObjMix:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class EditObjMix:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): new_obj})


class DelObjMix:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
