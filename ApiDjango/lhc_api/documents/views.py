from django.shortcuts import render
from django.contrib.auth.models import Document
from rest_framework import viewsets
from rest_framework import permissions
from lhc_api.documents import UserSerializer
# Create your views here.

class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = Document.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

