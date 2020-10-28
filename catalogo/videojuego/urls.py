from .views import inicio, incio_admin, PlataformasCreate, VideoJuegoCreate, VideojuegoList, VideojuegoUpdate, VideojuegoDelete, VideoJuegoDetalle, SearchResultsView, PlataformasList, BuscarPlataformas, PlataformasDetalle, PlataformasUpdate, PlataformasDelete
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import upload_file
from django.conf.urls import url, include



urlpatterns = [
    path('',inicio , name='inicio'),
    path('index_admin/', incio_admin, name='inicio_admin'),
    #---------------------------------------URL PLATAFORMAS------------------------------------
    path('crear_plataformas/',PlataformasCreate.as_view(), name='crear_plataformas'),
    path('listar_plataformas/',PlataformasList.as_view(), name='listar_plataformas'),
    path('buscar_plataformas/',BuscarPlataformas.as_view(), name='buscar_plataformas'),
    path('detalle_plataformas/<int:pk>', PlataformasDetalle.as_view(), name='detalle_plataformas'),
    path('actualizar_plataformas/<int:pk>', PlataformasUpdate.as_view(), name='actualizar_plataformas'),
    path('eliminar_plataformas/<int:pk>', PlataformasDelete.as_view(), name='eliminar_plataformas' ),

    #---------------------------------------URL VIDEOJUEGOS------------------------------------
    path('crear_videojuego/', VideoJuegoCreate.as_view(),name='crear_videojuego'),
    url('cargar', upload_file, name='cargar_imagen'),
    path('listar_videojuego/', VideojuegoList.as_view(), name='listar_videojuego' ),
    path('actualizar_videojuego/<int:pk>', VideojuegoUpdate.as_view(), name='actualizar_videojuego' ),
    path('eliminar_videojuego/<int:pk>', VideojuegoDelete.as_view(), name='eliminar_videojuego' ),
    path('detalle_videojuego/<int:pk>', VideoJuegoDetalle.as_view(), name='detalle_videojuego'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
