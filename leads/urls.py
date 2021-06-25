from django.urls import path

from .views import lead_create_view, lead_detail_view, lead_list_view, lead_update_view, lead_delete_view

app_name = "leads"

urlpatterns = [
        path('', lead_list_view, name = "lead-list"),
        path("<int:pk>/", lead_detail_view, name="lead-detail"),
        path("create/", lead_create_view, name="lead-create"),
        path("<int:pk>/update/", lead_update_view, name="lead-update"),
        path("<int:pk>/deletion/", lead_delete_view, name='lead-delete')
]