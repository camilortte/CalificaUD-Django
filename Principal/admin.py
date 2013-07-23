from django.contrib import admin
from Principal.models import Horario,Docente,Carrera,Materia,Facultad,Localidad,Estudiante
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EstudianteInline(admin.StackedInline):
    model = Estudiante
    can_delete = False
    verbose_name_plural = 'Estudiantes'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EstudianteInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Localidad)
admin.site.register(Facultad)
admin.site.register(Materia)
admin.site.register(Carrera)
admin.site.register(Docente)
admin.site.register(Horario)
#admin.site.register(Usuarios)
#admin.site.register(UsuarioBase)
#admin.site.register(Estudiante)
