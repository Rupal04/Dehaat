from django.conf.urls import url
from balancesheet import views

urlpatterns = [
    url('upload_csv/', views.upload_csv, name='upload_csv'),
    url('data/', views.get_variable_data, name='variable_data'),
    url('convert/', views.convert_pdf_to_csv, name='convert')
]