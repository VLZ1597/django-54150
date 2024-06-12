from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('prueba/', views.probando,name='probando'),
    path('crear_auto/', views.crear_auto, name='crear_auto'),
    path('autos/', views.autos,name='autos'),
    path('autos/eliminar/<int:id>', views.eliminar_auto,name='eliminar_auto'),
    path('autos/editar/<int:id>', views.editar_auto,name='editar_auto'),
    path('autos/ver/<int:id>', views.ver_auto,name='ver_auto'),
]
