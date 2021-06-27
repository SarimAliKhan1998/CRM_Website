from .models import Lead
from .forms import LeadModelForm
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"               # "object_list" by default




class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "object"




class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    # context_object_name = "form"

    def get_success_url(self):
        return reverse("leads:lead-list", args=())




class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):     
        return reverse("leads:lead-detail", args=(str(self.object.id),))




class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    context_object_name = "object"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list", args=())

