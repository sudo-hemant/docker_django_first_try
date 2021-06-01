from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import TodoList


router = DefaultRouter()

router.register('todo', TodoList)


urlpatterns = [
    # path('', views.ListTodo.as_view()),
    # path('<int:pk>/', views.DetailTodo.as_view()),
]

urlpatterns += router.urls