from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .forms import SignupForm


def landing_page_view(request):

    return render(request, "landingpage.html", {})



class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignupForm

    def get_success_url(self):
        return reverse("login")