from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('asset', views.asset, name='asset'),
        path('asset/delete/<int:asset_id>/', views.delete_asset, name='delete_asset'),
        path('asset/add/', views.add_asset, name='add_asset'),

        path('income', views.income, name='income'),
        path('income/delete/<int:income_id>/', views.delete_income, name='delete_income'),
        path('income/add/', views.add_income, name='add_income'),

        path('outcome', views.outcome, name='outcome'),
        path('outcome/delete/<int:outcome_id>/', views.delete_outcome, name='delete_outcome'),
        path('outcome/add/', views.add_outcome, name='add_outcome'),
]
