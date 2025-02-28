from rest_framework import viewsets
from .models import Train
from .serializers import TrainSerializer


# Create your views here.


class UserTrainList(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


# * conflict becuase same implementing with UserTrainList Class
# class TrainsCountView(viewsets.ModelViewSet):
# queryset = Train.objects.all()
# serializer_class = TrainSerializer
