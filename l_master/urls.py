from l_master import views
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [
    path('', login_required(views.landing), name="landing"),
    path('add_case/', login_required(views.add_case), name="add_case"),
    path('view_case/', login_required(views.view_case), name="view_case"),
    path('add_client/', login_required(views.add_client), name="add_client"),
    path('view_client/', login_required(views.view_client), name="view_client"),
    path('delete_client/<int:client_id>', login_required(views.delete_client), name="delete_client"),
    path('delete_case/<int:case_id>', login_required(views.delete_case), name="delete_case"),

]
