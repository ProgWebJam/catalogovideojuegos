from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Plataformas, VideoJuego
from .forms import PlataformasForms, VideoJuegoForms
from django.db.models import Q

# -----------------------------------INICIO SIN LOGIN-----------------------------------------------
def inicio(request):
    top5 = VideoJuego.objects.order_by("-ranking")[:5]
    return render(request, 'index.html',{'top5':top5})
    #return render(request, 'index.html')

# -----------------------------------INICIO CON LOGIN-----------------------------------------------
def incio_admin(request):
    top5 = VideoJuego.objects.order_by("-ranking")[:5]
    return render(request, 'videojuego/admin.html',{'top5':top5})
    #return render(request, 'videojuego/admin.html')

# -------------------------------------PLATAFORMAS--------------------------------------------------

#************CREAR PLATAFORMAS****************
class PlataformasCreate(CreateView):
    model = Plataformas
    form_class = PlataformasForms
    success_url = reverse_lazy('inicio_admin')

#************LISTAR PLATAFORMAS****************
class PlataformasList(ListView):
    model = Plataformas

#************BUSCAR PLATAFORMAS****************
class BuscarPlataformas(ListView):
    model = Plataformas
    template_name = 'plataformas_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Plataformas.objects.filter(
            Q(marca__icontains = query) | Q(fabricante__icontains = query)
        )
        return object_list

#************DETALLE PLATAFORMAS****************
class PlataformasDetalle(DetailView):
    model = Plataformas

#************ACTUALIZAR PLATAFORMAS****************
class PlataformasUpdate(UpdateView):
    model = Plataformas
    form_class = PlataformasForms
    success_url = reverse_lazy('inicio_admin')

#************ELIMINAR PLATAFORMAS****************
class PlataformasDelete(DeleteView):
    model = Plataformas
    success_url = reverse_lazy('inicio_admin')


# -------------------------------------VIDEOJUEGOS--------------------------------------------------

#************CREAR VIDEOJUEGOS****************
class VideoJuegoCreate(CreateView):
    model = VideoJuego
    form_class = VideoJuegoForms
    success_url = reverse_lazy('inicio_admin')


#************SUBIR ARCHIVOS****************
def upload_file(request):
    if request.method == 'POST':
        form = VideoJuegoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio_admin')
    else:
        form = VideoJuegoForms()
    return render(request, 'videojuego/videojuego_form.html', {
        'form': form
    })

#************LISTAR VIDEOJUEGOS****************
class VideojuegoList(ListView):
    model = VideoJuego

#************DETALLE VIDEOJUEGOS****************
class VideoJuegoDetalle(DetailView):
    model = VideoJuego

#************ACTUALIZAR VIDEOJUEGOS****************
class VideojuegoUpdate(UpdateView):
    model = VideoJuego
    form_class = VideoJuegoForms
    success_url = reverse_lazy('inicio_admin')

#************ELIMINAR VIDEOJUEGOS****************
class VideojuegoDelete(DeleteView):
    model = VideoJuego
    success_url = reverse_lazy('inicio_admin')

#************BUSCAR VIDEOJUEGOS****************
class SearchResultsView(ListView):
    model = VideoJuego
    template_name = 'videojuego_list.html'

    def get_queryset(self):
        genero = None
        query = self.request.GET.get('q')
        query2 = self.request.GET.get('lista')
        object_list = VideoJuego.objects.filter(
            Q(nombre__icontains = query) |  Q(plataformas__marca__icontains = query)
        )
        if query2:
            genero = VideoJuego.objects.filter(genero__exact=query2)
            return genero
        return object_list