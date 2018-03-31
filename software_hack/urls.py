"""software_hack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.shortcuts import render, redirect
# from kaala import result

d = {
    0: 'Rice',
    1: 'Cholam',
    2: 'Bajra',
    3: 'Ragi',
    4: 'BengalGram',
    5: 'Redgram'
}

def index(request):
    if request.method == 'GET':
        return render(request, 'base.html', {})
    if request.method == 'POST':

        # l = result()
        l = [0.0, 0.9666666666666667, 0.03333333333333333, 0.0, 0.0, 0.0]
        l = {i: j for i, j in enumerate(l)}

        l = [i for i, j in sorted(l.items(), key=lambda x: -x[1])]



        print(l)

        return render(request, 'result.html', {'data': l})




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]
