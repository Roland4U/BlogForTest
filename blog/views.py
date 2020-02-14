from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.views import defaults


def hello(request):
	return HttpResponse('<h1>Hello<h1/>')


def Error_404(request, exception):
    return render(request, 'blogapp/404.html')


# def Error_404(request, exception):
    # defaults.page_not_found(request, exception, template_name='blogapp/404.html')
    # context = RequestContext(request)
    # response = render_to_response('blogapp/404.html', context={'error404': context})
    # response.status_code = 404
    # return response
