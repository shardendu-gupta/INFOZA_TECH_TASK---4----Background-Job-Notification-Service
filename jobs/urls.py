from django.urls import path
from .views import JobCreateView, JobListView, JobDetailsView, JobStatusView


urlpatterns = [ 

    path('jobs/', JobCreateView.as_view(), name='create-job'),
    path('jobs/list/', JobListView.as_view(), name='list-job'),
    path("jobs/<int:pk>/", JobDetailsView.as_view(), name="job-detail"),
    path("jobs/<int:pk>/status/", JobStatusView.as_view(), name="job-status"),

]