from django.shortcuts import render
from .models import Car, About, Footer
from django.views.generic import ListView
# Create your views here.


class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        cars = Car.objects.all()
        return render(request, self.template_name, {'cars':cars})


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        about = About.objects.all()
        return render(request, self.template_name, {'about':about})

class FooterListView(ListView):
    template_name = '_footer.html'
    
    def get(self, request):
        footer = Footer.objects.all()
        return render(request, self.template_name, {'footer':footer})