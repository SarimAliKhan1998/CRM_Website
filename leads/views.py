from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Lead

# Create your views here.


def lead_list_view(request):

    queryset = Lead.objects.all()
    context = {
        "leads" : queryset
    }
    return render(request, "leads/lead_list.html", context)



def lead_detail_view(request, pk):

    obj = get_object_or_404(Lead, id = pk)

    context = {
        "object": obj,
    }
    return render(request, "leads/lead_detail.html", context)
