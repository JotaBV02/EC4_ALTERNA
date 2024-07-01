"""
URL configuration for proyecto001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from miapp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.layout, name = "layout"),
    path('listar-cursos/',views.listar_cursos,name="listar_cursos"),
    path('crear-curso/',views.crear_curso,name="crear_curso"),
    path('eliminar-curso/<int:idcourse>',views.eliminar_curso,name="eliminar_curso"),
    path('listar-carreras/',views.listar_carreras,name="listar_carreras"),
    path('crear-carrera/',views.crear_carrera,name="crear_carrera"),
    path('eliminar-carrera/<int:idcareer>',views.eliminar_carrera,name="eliminar_carrera"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)