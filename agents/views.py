from django.http import request
from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoginAndOrganizerRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm

class AgentListView(LoginAndOrganizerRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'
    # queryset = Agent.objects.all()
    context_object_name = 'agents'

    def get_queryset(self):
        agent_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = agent_organisation)
        # return Agent.objects.all()


class AgentCreateView(LoginAndOrganizerRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list", args = ())

    def form_valid(self, form):
        agent = form.save(commit = False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginAndOrganizerRequiredMixin, DetailView):
    template_name = "agents/agent_detail.html"

    def get_queryset(self):
        agent_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = agent_organisation)


class AgentUpdateView(LoginAndOrganizerRequiredMixin, UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        agent_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = agent_organisation)

    def get_success_url(self):
        return reverse("agents:agent-detail", args = (self.object.id,))



class AgentDeleteView(LoginAndOrganizerRequiredMixin, DeleteView):
    template_name = "agents/agent_delete.html"

    def get_queryset(self):
        agent_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = agent_organisation)

    def get_success_url(self): 
        return reverse ("agents:agent-list")