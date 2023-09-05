from rest_framework import serializers
from .models import expense
from django.db.models import Sum


class DailyExpenseSerializer(serializers.Serializer):
    Totalexpense=serializers.IntegerField()

class ExpenseSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=expense
        fields=('expid','crnt_bal','difference','reason')

        

