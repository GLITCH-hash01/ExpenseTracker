from rest_framework import serializers
from .models import expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=expense
        fields=('expid','crnt_bal','difference','reason')

