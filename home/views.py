from django.shortcuts import render
from django.views import View

from home.models import MiModelo

# Create your views here.


class Home(View):
    def get(self, request):

        MiModelo(nombre='Javier').save()
        
        return render(request, 'home.html', {})