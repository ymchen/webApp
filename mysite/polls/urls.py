# -*- coding: utf-8 -*-
# @Author: chenym
# @Date:   2019-12-17 10:43:50
# @Last Modified by:   chenym
# @Last Modified time: 2019-12-19 09:06:27
from django.urls import path

from . import views
app_name = 'polls' 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]