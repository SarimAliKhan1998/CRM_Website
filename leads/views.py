from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.urls import reverse

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



def lead_create_view(request):
    
    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("leads:lead-list", args=()))
    context = {
        "form" : form
    }
    return render(request, "leads/lead_create.html", context)




def lead_update_view(request, pk):

    object = get_object_or_404(Lead, id = pk)
    form = LeadModelForm(instance=object)

    if request.method == "POST":

        form = LeadModelForm(request.POST, instance= object)
        if form.is_valid():

            form.save()
            return redirect(reverse("leads:lead-detail", args=(pk,)))

    context = {
        "object" : object,
        "form" : form
    }
    return render(request, "leads/lead_update.html", context)




def lead_delete_view(request, pk):

    object = get_object_or_404(Lead, id = pk)
    if request.method == "POST":
        object.delete()
        return redirect(reverse("leads:lead-list", args=()))
    context = {
        "object" : object
    }
    return render(request, "leads/lead_delete.html", context)