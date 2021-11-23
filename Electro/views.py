from rest_framework import generics
from .models import Electro
from .serializer import ElectroSerializer
from .permissions import IsAuthorOrReadOnly


class ElectroListView(generics.ListCreateAPIView):
    queryset = Electro.objects.all()
    serializer_class = ElectroSerializer


class ElectroDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Electro.objects.all()
    serializer_class = ElectroSerializer
