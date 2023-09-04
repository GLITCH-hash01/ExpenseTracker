from rest_framework.decorators import api_view
from django.db.models import Max
from django.http import HttpResponse,JsonResponse
from .serializers import ExpenseSerializer
from .models import expense
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

# Create your views here.

def home(request):
    return HttpResponse("Hello World")


@api_view(['GET'])
def get_balance(request):
    lastid=expense.objects.aggregate(max_id=Max('expid'))['max_id']
    balance_rcrd=expense.objects.get(expid=lastid)
    serializer=ExpenseSerializer(balance_rcrd)
    return Response(serializer.data,status.HTTP_200_OK)  

@api_view(['POST'])
def add_expense(request):
    serializer=ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        print(serializer.data)


@api_view(['GET'])
def get_expense(request):

    reason_query=request.query_params.get('reason')
    dd_query=request.query_params.get('dd')
    mm_query=request.query_params.get('mm')
    yy_query=request.query_params.get('yy')

    expenses=expense.objects.all()
    serializer=ExpenseSerializer(expenses,many=True)

    if reason_query:
        try:
            expenses=expenses.filter(reason=reason_query)
        except expense.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)
       
    if mm_query and dd_query and yy_query:
        search_date=datetime(int(yy_query),int(mm_query),int(dd_query))
        try:
            expenses=expenses.filter(datetime__date=search_date)
        except expense.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)
       

    serializer=ExpenseSerializer(expenses,many=True)
    return Response(serializer.data,status.HTTP_200_OK)  
   

   
