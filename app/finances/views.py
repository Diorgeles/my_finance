from rest_framework import viewsets, decorators, response
from . import serializers
from . import models
import json

class ExpenseAndReceiveViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExpenseAndReceiveSerializer
    queryset = models.ExpenseAndReceive.objects.all()

    @decorators.detail_route(methods=['GET'])
    def expense(self, request, *args,  **kwargs):
        instance = self.get_object()
        return response.Response(serializers.ExpenseAndReceiveSerializer(instance).data)
