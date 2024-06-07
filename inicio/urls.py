from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('template1/<str:nombre>/<str:apellido>/<int:edad>/', views.template1),
    path('template2/<str:nombre>/<str:apellido>/<int:edad>/', views.template2),
    path('template3/<str:nombre>/<str:apellido>/<int:edad>/', views.template3),
    path('saludo/<str:nombre>/<str:apellido>/<int:edad>/', views.template4,name='saludo'),
    path('prueba/', views.probando,name='probando'),
    # path('auto/<str:marca>/<str:modelo>', views.auto, name='crear'),
    path('crear_auto/', views.crear_auto, name='crear_auto'),
    path('autos/', views.autos,name='autos')
]
