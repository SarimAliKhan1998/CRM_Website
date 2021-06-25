from django.urls import path

from .views import lead_create_view, lead_detail_view, lead_list_view, lead_update_view, lead_delete_view

app_name = "leads"

urlpatterns = [
        path('', lead_list_view),
        path("<int:pk>/", lead_detail_view),
        path("create/", lead_create_view),
        path("<int:pk>/update/", lead_update_view),
        path("<int:pk>/delete/", lead_delete_view)
]