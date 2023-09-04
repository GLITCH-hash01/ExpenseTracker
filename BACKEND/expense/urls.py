from  django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('expenses/',views.expense_list,name="expenses"),
    path('balance/',views.current_balance,name="balance"),
    path('add_expenses/',views.add_expense,name="add_expenses"),
    path('get_expense_by/<str:reason>',views.get_expense_by,name="get_expense"),
]