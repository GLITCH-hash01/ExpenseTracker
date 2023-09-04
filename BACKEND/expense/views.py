from rest_framework.decorators import api_view
from django.db.models import Max
from django.http import HttpResponse,JsonResponse
from .serializers import ExpenseSerializer
from .models import expense
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def home(request):
    return HttpResponse("Hello World")

@api_view(['GET'])
def expense_list(request):
    expenses=expense.objects.all()
    serializer=ExpenseSerializer(expenses,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def current_balance(request):
    lastid=expense.objects.aggregate(max_id=Max('expid'))['max_id']
    balance_rcrd=expense.objects.get(expid=lastid)
    serializer=ExpenseSerializer(balance_rcrd)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def add_expense(request):
    serializer=ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        print(serializer.data)

@api_view(['GET'])
def get_expense_by(request,reason):
    try:
        expenses=expense.objects.filter(reason=reason)
        
    except expense.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)
    serializer=ExpenseSerializer(expenses,many=True)
    print(serializer.data)
    return Response(serializer.data,status=status.HTTP_200_OK)
    