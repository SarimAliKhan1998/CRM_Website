
from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin

class LoginAndOrganizerRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organizer"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            return redirect("/leads")
        return super().dispatch(request, *args, **kwargs)
