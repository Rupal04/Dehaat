from django.conf.urls import url
from balancesheet import views

urlpatterns=[
    url('upload/', views.upload_sheet, name='upload_sheet'),
    url('data/', views.get_variable_data, name='variable_data')
]