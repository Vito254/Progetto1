from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('<int:product_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:product_id>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:product_id>/delete/', views.DeleteView.as_view(), name='delete'),
]

