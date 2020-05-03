from rest_framework import serializers
from balancesheet.models import BalSheet


class BalSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalSheet
        fields = '__all__'
