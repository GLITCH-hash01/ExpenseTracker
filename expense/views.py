from django.shortcuts import render
from django.db.models import Max
from django.http import HttpResponse,JsonResponse
from .serializers import ExpenseSerializer
from .models import expense

# Create your views here.

def home(request):
    return HttpResponse("Hello World")

def expense_list(request):
    expenses=expense.objects.all()
    serializer=ExpenseSerializer(expenses,many=True)
    return JsonResponse(serializer.data,safe=False)

def current_balance(request):
    lastid=expense.objects.aggregate(max_id=Max('expid'))['max_id']
    balance_rcrd=expense.objects.get(expid=lastid)
    serializer=ExpenseSerializer(balance_rcrd)
    return JsonResponse(serializer.data,safe=False)