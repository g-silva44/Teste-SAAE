from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from ocorrencias import views
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),

    # Bairros
        path('bairros/', views.listar_bairros, name='listar_bairros'),
        path('bairros/novo/', views.criar_bairro, name='criar_bairro'),
        path('bairros/<int:pk>/editar/', views.editar_bairro, name='editar_bairro'),
        path('bairros/<int:pk>/excluir/', views.excluir_bairro, name='excluir_bairro'),
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Ocorrências
    path('ocorrencias/nova/', views.criar_ocorrencia, name='criar_ocorrencia'),
    path('ocorrencias/<int:pk>/editar/', views.editar_ocorrencia, name='editar_ocorrencia'),
    path('ocorrencias/<int:pk>/excluir/', views.excluir_ocorrencia, name='excluir_ocorrencia'),

    # Tela de Login e Logout
        path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
