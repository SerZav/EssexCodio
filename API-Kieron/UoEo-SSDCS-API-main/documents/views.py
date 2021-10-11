from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Documents
from .serializers import DocumentSerializer
from .pagination import CustomPagination
from rest_framework import permissions
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]
# Create your views here.
class DocumentList(ListCreateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Documents.objects.filter(owner=self.request.user)


class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Documents.objects.filter(owner=self.request.user)
