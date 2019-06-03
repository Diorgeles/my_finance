from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from app.finances import views

router = routers.DefaultRouter()
router.register(r'expense_and_receive', views.ExpenseAndReceiveViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/my_finance/', include(router.urls))
]
