"""
URL configuration for hello_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls")), # 👈 polls.urls points to the
                                           #    urls.py file inside the Django
                                           #    project's root folder. (AKA: Where
                                           #    manage.py is.) So, urls.py within
                                           #    hello_django is like a top-level
                                           #    router that forwards requests to
                                           #    instances of Django apps.
                                           #    "polls/" is the URL, and it can be
                                           #    named anything we'd like.
]
