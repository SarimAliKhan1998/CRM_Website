from django.urls import path

from .views import lead_detail_view, lead_list_view

app_name = "leads"

urlpatterns = [
        path('', lead_list_view),
        path("<int:pk>/", lead_detail_view)
]