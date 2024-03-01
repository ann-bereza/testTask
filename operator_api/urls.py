from django.urls import path

from operator_api.views import RequestGetUpdateDeleteView

urlpatterns = [
    path('requests/<int:request_id>', RequestGetUpdateDeleteView.as_view(), name='handle_request'),
]
