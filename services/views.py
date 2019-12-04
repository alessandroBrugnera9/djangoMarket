from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import service

class serviceListView(ListView):
    queryset = service.objects.all()
    template_name = "services/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(serviceListView,self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return (context)
    def get_queryset(self,*args, **kwargs):
        request=self.request
        return service.objects.all()


class serviceDetailView(DetailView):
    queryset = service.objects.all()
    template_name = "services/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(serviceDetailView,self).get_context_data(*args, **kwargs)
        print(context)
        return (context)