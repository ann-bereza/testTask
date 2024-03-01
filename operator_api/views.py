from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from client_api.models import Request
from operator_api.serializers import RequestSerializer


class RequestGetUpdateDeleteView(APIView):
    """
        API endpoint for retrieving, updating, and deleting requests.
    """
    serializer_class = RequestSerializer

    def get(self, request, request_id):
        request_obj = get_object_or_404(Request, pk=request_id)
        serializer = self.serializer_class(request_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, request_id):
        request_obj = get_object_or_404(Request, pk=request_id)
        serializer = self.serializer_class(request_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Request information has been updated successfully.",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, request_id):
        request = get_object_or_404(Request, pk=request_id)
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
