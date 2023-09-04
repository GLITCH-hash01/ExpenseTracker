from  django.urls import path
from . import views


"""


category 
    -reason
    -day
"""

urlpatterns =[
    path('',views.home,name="home"),
    path('get-balance/',views.get_balance,name="balance"),
    path('add-expense/',views.add_expense,name="add_expenses"),
    path('get-expenses/',views.get_expense,name="get_expense"),

]