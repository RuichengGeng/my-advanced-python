from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #####################home_page###########################################
    path('', views.say_hello, name="hello"),
    path('index', views.index, name="todo"),
    path('list', views.all_todo_list, name="get_list"),
    ####################give id no. item_id name or item_id=i.id ############
    # pass item_id as primary key to remove that the todo with given id
    path('del/<str:item_id>', views.remove, name="del"),
    ########################################################################
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)