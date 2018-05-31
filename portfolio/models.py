from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,help_text="Introduce tu nombre",verbose_name="Titulo")
    description = models.TextField(help_text="Introduce tu descripcion",verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen",upload_to="projects")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")


    class Meta:
        verbose_name  = "Proyecto"
        verbose_name_plural  =  "Proyectos"
        ordering =["-created"]
    
    def __str__(self):
        return self.title