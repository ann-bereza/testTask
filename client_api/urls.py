from django.urls import path

from client_api.views import ClientListCreateView, ClientGetUpdateDeleteView, RequestListCreateView

urlpatterns = [
    path('clients', ClientListCreateView.as_view(), name='client_list_create'),
    path('clients/<int:client_id>', ClientGetUpdateDeleteView.as_view(), name='handle_client'),
    path('requests', RequestListCreateView.as_view(), name='request_list_create'),
]
