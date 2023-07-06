from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.say_hello),
    path("hello/", views.say_hello),
    path("time/", views.report_time),
    path("add/", views.add),
    path("all_models/", views.all_models),
    path("js_all_models/", views.model_list),
    path("js_all_models/<str:pk>", views.model_detail),
    path("model-delete/<int:pk>", views.model_detail, name="model delete"),
]

urlpatterns = format_suffix_patterns(urlpatterns)


