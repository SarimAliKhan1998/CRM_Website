from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Lead, Agent
from .forms import LeadForm

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

    form = LeadForm()

    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name_field = form.cleaned_data["first_name"]
            last_name_field = form.cleaned_data["last_name"]
            age_field = form.cleaned_data["age"]
            agent_field = Agent.objects.first()

            Lead.objects.create(
                                first_name = first_name_field,
                                 last_name = last_name_field,
                                 age = age_field,
                                 agent = agent_field
                                 )
            return redirect("/leads")
    context = {
        "form" : form
    }
    return render(request, "leads/lead_create.html", context)
