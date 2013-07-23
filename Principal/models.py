#encoding:utf-8
from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
import datetime 
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager 
from django.contrib.auth.models import User
"""class UsuariosManager(BaseUserManager):
    def create_user(self, username, nombre, apellido, password=None):
        if not username:
            raise ValueError('El usuario debe tener un username')
        user = self.model(username=username, nombre=nombre, apellido=apellido)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nombre, apellido, password):
        user = self.create_user(username, nombre, apellido, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Usuarios(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=250, unique=True, db_index=True)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    get_full_name=True
    get_short_name=True
    is_active=True

    objects = UsuariosManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido']"""

#############################################################################################

class Localidad(models.Model):
    idLocalidad = models.IntegerField(primary_key=True,null=False,unique=True)
    nombre = models.CharField(max_length=100)   
    class Meta:
        verbose_name=u'Localidad'        
        verbose_name_plural = u'Localidades'    
    def __unicode__(self):
        return self.nombre     

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10,null=True,blank=True)
    nombre_decano = models.CharField(
    max_length=100,blank=True,null=True,help_text='Nombre completo del decano')
    correo = models.EmailField(null=True,blank=True)
    class Meta:
        verbose_name = u'Facultad'
        verbose_name_plural = u'Facultades'

    def __unicode__(self):
        return self.nombre

class Carrera(models.Model):
    codigo = models.IntegerField(primary_key=True,null=False,blank=False)
    nombre = models.CharField(max_length=100)
    coordinador = models.CharField(max_length=100,null=True,blank=True, help_text='Nombre del coordinado de carrera')
    telefono = models.CharField(max_length=10,null=True,blank=True) 
    facultad = models.ForeignKey(Facultad)
    class Meta:
        verbose_name = u'Carrera'
        verbose_name_plural = u'Carreras'

    def __unicode__(self):
        return self.nombre


class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    informacion = models.URLField(help_text='Url que contiene informacion sobre el profesor',null=True,blank=True)

    class Meta:
        verbose_name = u'Docente'
        verbose_name_plural = u'Docentes'

    def __unicode__(self):
        return self.nombre

class Horario(models.Model):
    lunes = models.CharField(max_length=15,null=True,blank=True)
    martes = models.CharField(max_length=15,null=True,blank=True)
    miercoles = models.CharField(max_length=15,null=True,blank=True)
    jueves = models.CharField(max_length=15,null=True,blank=True)
    viernes = models.CharField(max_length=15,null=True,blank=True)
    sabado = models.CharField(max_length=15,null=True,blank=True)    
    domingo = models.CharField(max_length=15,null=True,blank=True)       

    def save(self):
        if (self.lunes==None and self.martes==None and self.miercoles==None 
           and self.jueves==None and self.viernes==None and self.sabado==None 
           and self.domingo==None):
            return False
        else:
            super(Horario,self).save()

    class Meta:
        verbose_name = u'Horaio'
        verbose_name_plural = u'Horaios'

    def __unicode__(self):
        return "Horario"
   

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    numero_creditos = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(10)])
    intensidad_horaria_semanal = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(25)])
    temario = models.FileField(upload_to='temario_carrera/',null=True,blank=True)
    horario = models.ForeignKey(Horario,null=True,blank=True)
    profesor = models.ManyToManyField(Docente)
    carrera = models.ForeignKey(Carrera)

    class Meta:
        verbose_name = u'Materia'
        verbose_name_plural = u'Materias'

    def __unicode__(self):
        return self.nombre

class Criterio(models.Model):
    descripcion = models.TextField(help_text='Pregunta bien redactada')
    class Meta:
        verbose_name = u'Criterio'
        verbose_name_plural = u'Criterios'

    def __unicode__(self):
        return self.descripcion



class Estudiante(models.Model):
    user  = models.OneToOneField(User)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    email = models.EmailField(unique=True) 
    codigo = models.CharField(max_length=11)    
    carrera = models.ForeignKey(Carrera)
    localidad = models.ForeignKey(Localidad)

    def __unicode__(self):  
        return self.nombre


class Calificacion(models.Model):
    puntaje = models.IntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(5)],help_text='Un numero entre 0 y 5')    
    criterio = models.ManyToManyField(Criterio)
    docente = models.ForeignKey(Docente)
    estudiante = models.ForeignKey(Estudiante)

    class Meta:
        verbose_name = u'Calificacion'
        verbose_name_plural = u'Calificaciones'

    def __unicode__(self):
        return self.criterio.descripcion+"="+self.puntaje


class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(u"Date", default=datetime.date.today)
    estudiante = models.ForeignKey(Estudiante)
    docente = models.ManyToManyField(Docente)
    class Meta:
        verbose_name = u'Comentario'
        verbose_name_plural = u'Comentarios'

    def __unicode__(self):
        return self.contenido




    
    

    

   
