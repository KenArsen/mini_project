from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls', namespace="account")),
    path('blog/', include('blog.urls', namespace="blog")),
]
