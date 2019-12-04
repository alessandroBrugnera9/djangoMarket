from django.shortcuts import render
from django.views.generic import ListView

from services.models import service


class searchServiceView(ListView):
    queryset = service.objects.all()
    template_name = "services/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(serviceListView,self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return (context)
    def get_queryset(self,*args, **kwargs):
        request=self.request
        query = request.GET.get('q')
        print(query)
        if query is not None:
            return service.objects.filter(category__icontains=query)
        else:
            return service.objects.none()
