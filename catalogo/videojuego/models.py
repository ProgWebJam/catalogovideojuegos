from django.db import models


# Create your models here.

class Plataformas(models.Model):
    LISTA_TIPO = (
        ('c','consola'),
        ('p','pc'),
        ('m','movil')
    )
    marca = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=30)
    tipo = models.CharField(max_length=1, choices=LISTA_TIPO)
    generacion = models.CharField(max_length=30)
    capacidad_disco = models.CharField(max_length=30)
    gpu = models.CharField(max_length=30)
    soporte = models.CharField(max_length=30)
    web_oficial = models.URLField(max_length=200)

    def __str__(self):
        return self.marca + " - " +self.fabricante

class VideoJuego(models.Model):
    LISTA_GENERO = (
        ('a','accion'),
        ('d','deportes'),
        ('e','estrategia'),
        ('c','carreras')
    )

    LISTA_CLASIFICACION = (
        ('n','E10+(niño)'),
        ('a','T(Adolecente)'),
        ('m','M+17(Maduro)'),
        ('a','A0+18(Adulto)')
    )

    LISTA_JUGABILIDAD = (
        ('1','Primera Persona'),
        ('3','Tercera Persona')
    )

    nombre = models.CharField(max_length=100, unique=True, help_text='Ya existe el nombre del videojuego')
    genero = models.CharField(max_length=1, choices=LISTA_GENERO)
    fabricante = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=1, choices=LISTA_CLASIFICACION)
    ano_lanzamiento = models.DateField()
    max_jugadores = models.IntegerField()
    jugabilidad = models.CharField(max_length=1, choices=LISTA_JUGABILIDAD)
    #plataformas = models.ForeignKey(Plataformas, null=True, blank=True,on_delete=models.CASCADE)
    plataformas = models.ManyToManyField(Plataformas)
    web_oficial = models.URLField(max_length=200)
    imagen = models.FileField(upload_to='myFolder/', blank=True, null=True)
    trailer = models.URLField(max_length=200)
    ranking = models.DecimalField(max_digits=5, decimal_places=2)

    def only_year(self):
        return self.ano_lanzamiento.strftime('%Y')
    

    
    def __str__(self):
        return self.nombre




