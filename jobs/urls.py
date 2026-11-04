from django.urls import path
from .views import JobCreateView, JobListView

urlpatterns = [ 


    path('jobs/', JobCreateView.as_view(), name='create-job'),
    path('jobs/list/', JobListView.as_view(), name='list-job'),

]

