from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from client_api.models import ClientEntity, Request
from client_api.serializers import ClientSerializer, RequestSerializer


class ClientListCreateView(APIView):
    """
       API endpoint for listing and creating clients.
    """
    serializer_class = ClientSerializer

    def get(self, request):
        clients = ClientEntity.objects.all()
        serializer = self.serializer_class(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Client information has been added successfully.",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientGetUpdateDeleteView(APIView):
    """
        API endpoint for retrieving, updating, and deleting clients.
    """
    serializer_class = ClientSerializer

    def get(self, request, client_id):
        client = get_object_or_404(ClientEntity, pk=client_id)
        serializer = self.serializer_class(client)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, client_id):
        client = get_object_or_404(ClientEntity, pk=client_id)
        serializer = self.serializer_class(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Client information has been updated successfully.",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, client_id):
        client = get_object_or_404(ClientEntity, pk=client_id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RequestListCreateView(APIView):
    """
        API endpoint for listing and creating requests.
    """
    serializer_class = RequestSerializer

    def get(self, request):
        requests = Request.objects.all()
        serializer = self.serializer_class(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            client = get_object_or_404(ClientEntity, pk=serializer.data["client"])

            response = {
                "message": f"A request from {client.first_name} {client.last_name} was created successfully.",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
