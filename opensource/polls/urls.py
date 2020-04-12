from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:test_id>/', views.detail, name='detail'),
    path('<int:test_id>/results/<int:score>/', views.results, name='results'),
    path('<int:test_id>/vote/', views.vote, name='vote')
]