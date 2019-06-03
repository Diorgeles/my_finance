from rest_framework import serializers
from . import models


class ExpenseAndReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpenseAndReceive
        fields = '__all__'
