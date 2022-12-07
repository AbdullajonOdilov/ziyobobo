from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('news/', NewsView.as_view()),
    path('news1/', News1View.as_view()),
    path('mehnat/', MehnatView.as_view()),
    path('qabul/', QabulView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", set_language, name="set-language"),
]