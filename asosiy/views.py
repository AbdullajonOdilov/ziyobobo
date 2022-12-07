from django.shortcuts import render
from django.views import View

from .models import *


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

class NewsView(View):
    def get(self, request):
        data = {
            "news":News.objects.all(),
        }
        return render(request, 'yangiliklar.html',data)


class News1View(View):
    def get(self, request):
        return render(request, 'news1.html')


class MehnatView(View):
    def get(self, request):
        return render(request, 'mehnat-m.html')

class QabulView(View):
    def get(self,request):
        return render(request, 'qabul.html')



#change language
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response