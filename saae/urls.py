"""
URL configuration for saae project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from ocorrencias import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Tela de Login e Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Bairros
    path('bairros/', views.listar_bairros, name='listar_bairros'),
    path('bairros/novo/', views.criar_bairro, name='criar_bairro'),
    path('bairros/<int:pk>/editar/', views.editar_bairro, name='editar_bairro'),
    path('bairros/<int:pk>/excluir/', views.excluir_bairro, name='excluir_bairro'),

    # Ocorrências
    path('ocorrencias/nova/', views.criar_ocorrencia, name='criar_ocorrencia'),
    path('ocorrencias/<int:pk>/editar/', views.editar_ocorrencia, name='editar_ocorrencia'),
    path('ocorrencias/<int:pk>/excluir/', views.excluir_ocorrencia, name='excluir_ocorrencia'),
]
