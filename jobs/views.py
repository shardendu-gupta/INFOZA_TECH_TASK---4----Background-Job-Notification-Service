from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Jobs
from .serializers import JobSerializer


class JobCreateView(generics.CreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]



class JobListView(generics.ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]


class JobDetailsView(generics.RetrieveAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    