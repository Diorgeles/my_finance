from rest_framework import viewsets
from . import serializers
from . import models


class ExpenseAndReceiveViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExpenseAndReceiveSerializer
    queryset = models.ExpenseAndReceive.objects.all()
