from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from Work.serializers import WorkSerializer
from Work.models import WorkModel
from Artist.models import ArtistModel
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WorkModel.objects.all()
        Artist = self.request.query_params.get("artist")
        work_type = self.request.query_params.get("work_type")
        # filtering based on the given parameters

        if Artist is not None:
            artistInstance = ArtistModel.objects.get(name=Artist)
            # retreving all the Work Instances linked to the artist
            queryset = artistInstance.work.all()

        if work_type is not None:
            w = {"YT": "Youtube", "IG": "Instagram", "OT": "Other"}
            queryset = queryset.filter(workType=w[work_type])
        return queryset


class WorkCreate(generics.CreateAPIView):
    serializer_class = WorkSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        workinstance = serializer.save()
        # Retriving the artist instance that is linked to the current User
        artist = ArtistModel.objects.get(userInstance=self.request.user)
        # Adding the work instance to the artist instance and saving it
        artist.work.add(workinstance)
        return super().perform_create(serializer)
