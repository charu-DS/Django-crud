from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='crudop'),
    path('view/',views.view,name='view'),
    path('tables/',views.tables,name='tables'),
    path('view/tables/',views.tables,name='view/tables'),
    path('tables/crudop/',views.index,name='tables/crudop/'),
     path('tables/view/',views.view,name='view'),
]