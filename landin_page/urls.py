from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('proyectos/', TemplateView.as_view(template_name='proyectos.html'), name='proyectos'),
]
