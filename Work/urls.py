from django.urls import path
from Work.views import WorkList,WorkCreate

urlpatterns = [
    path("works/", WorkList.as_view()),
    path("works/create/",WorkCreate.as_view())
]
