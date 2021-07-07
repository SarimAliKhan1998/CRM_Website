from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead
from .forms import LeadModelForm
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from agents.mixins import LoginAndOrganizerRequiredMixin



class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"               # "object_list" by default

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation = user.userprofile, agent__isnull = False)
        else:
            queryset = Lead.objects.filter(organisation = user.agent.organisation, agent__isnull = False)
            queryset = queryset.filter(agent__user = user)
        return queryset


    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user  
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation = user.userprofile, agent__isnull = True)
            context.update({"unassigned_leads" : queryset})

        return context



class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "object"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation = user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation = user.agent.organisation)
            queryset = queryset.filter(agent__user = user)
        return queryset




class LeadCreateView(LoginAndOrganizerRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    # context_object_name = "form"

    def get_success_url(self):
        return reverse("leads:lead-list", args=())


    def form_valid(self, form):
        
        lead = form.save(commit = False)
        lead.organisation = self.request.user.userprofile
        lead.save()

        send_mail(
            subject=f"New Lead Created by {self.request.user}",
            message=f"Check out the new lead : {lead}!!!",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)


    def get_form_kwargs(self):
        kwargs = super(LeadCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs




class LeadUpdateView(LoginAndOrganizerRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_success_url(self):     
        return reverse("leads:lead-detail", args=(str(self.object.id),))

    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.filter(organisation = user.userprofile)
        return queryset

    def get_form_kwargs(self):
        kwargs = super(LeadUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs



class LeadDeleteView(LoginAndOrganizerRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    context_object_name = "object"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list", args=())


    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.filter(organisation = user.userprofile)
        return queryset

