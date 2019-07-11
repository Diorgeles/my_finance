from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from app.finances import views

router = routers.DefaultRouter()
router.register(r'expense_and_receive', views.ExpenseAndReceiveViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/my_finance/', include(router.urls)),
    re_path('^home/', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
