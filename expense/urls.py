from  django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('expenses/',views.expense_list,name="expenses"),
    path('balance/',views.current_balance,name="balance"),
]