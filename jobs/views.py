from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Jobs
from .serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



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


class JobStatusView(APIView):

    def get(self, requst, pk):

        try:
            job = Jobs.objects.get(pk=pk)

        except Jobs.DoesNotExist:
            return Response({"error": "job not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({
        "job_id": job.id,
        "status": job.status,
        "attempts": job.attempts,
        "max_attempts": job.max_retries,
        "error_message": job.error_message,
        "completed_at": job.completed_at,
    })


