from django.db import models

# Enums
class Incorporacion(models.TextChoices):
    INMEDIATAMENTE = 'INMEDIATAMENTE', 'Inmediatamente'
    _15_DIAS = '_15_DIAS', '_15_Dias'
    _7_DIAS = '_7_DIAS', '_7_Dias'

class Sector(models.TextChoices):
    IT = 'IT', 'It'
    SALUT = 'SALUT', 'Salut'
    OTRO = 'OTRO', 'Otro'

# Modelo para representar un usuario
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Nombre de usuario único
    password = models.CharField(max_length=128)  # Contraseña del usuario
    nombre = models.CharField(max_length=255)  # Nombre completo del usuario

# Modelo para representar el perfil de un usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el modelo User
    direccion = models.CharField(max_length=255)  # Dirección del usuario
    telefono = models.CharField(max_length=20)  # Teléfono del usuario
    correo_electronico_1 = models.EmailField()  # Primer correo electrónico del usuario
    correo_electronico_2 = models.EmailField(blank=True, null=True)  # Segundo correo electrónico opcional
    dni = models.CharField(max_length=20, unique=True)  # DNI único del usuario
    url = models.URLField(blank=True, null=True)  # URL opcional del usuario
    biografia = models.TextField(blank=True, null=True)  # Biografía opcional del usuario
    open_to_work = models.BooleanField(blank=False) 
    vehicle = models.BooleanField(blank=False, null= True)
    disability =  models.BooleanField(blank=False)
    disability_percentage = models.IntegerField(blank= True, null= True)
    incorporation = models.CharField(max_length=50, choices=Incorporacion.choices)  # Incorporación
    sector = models.CharField(max_length=50, choices=Sector.choices)  # Sector


    # Relaciones muchos a muchos con otros modelos
    experiencias_laborales = models.ManyToManyField("ExperienciaLaboral", blank=True)  # Experiencias laborales
    hard_skills = models.ManyToManyField("HardSkill", blank=True)  # Habilidades duras
    soft_skills = models.ManyToManyField("SoftSkill", blank=True)  # Habilidades blandas
    idiomas = models.ManyToManyField("Idioma", blank=True)  # Idiomas

    # Relaciones uno a muchos con otros modelos
    formaciones_academicas = models.ForeignKey("FormacionAcademica", on_delete=models.CASCADE)  # Formaciones académicas
    voluntariados = models.ForeignKey("Voluntariado", on_delete=models.CASCADE, blank=True, null=True)  # Voluntariados
    proyectos = models.ForeignKey("Proyecto", on_delete=models.CASCADE, blank=True, null=True)  # Proyectos
    publicaciones = models.ForeignKey("Publicacion", on_delete=models.CASCADE, blank=True, null=True)  # Publicaciones
    reconocimientos_premios = models.ForeignKey("ReconocimientoPremio", on_delete=models.CASCADE, blank=True, null=True)  # Reconocimientos y premios
    certificaciones_cursos = models.ForeignKey("CertificacionCurso", on_delete=models.CASCADE, blank=True, null=True)  # Certificaciones y cursos

# Modelo para representar una experiencia laboral
class ExperienciaLaboral(models.Model):
    puesto_trabajo = models.CharField(max_length=255)  # Puesto de trabajo
    fecha_inicio = models.DateField()  # Fecha de inicio
    fecha_final = models.DateField(blank=True, null=True)  # Fecha de finalización opcional
    nombre_empresa = models.CharField(max_length=255)  # Nombre de la empresa
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional
    logros_obtenidos = models.TextField(blank=True, null=True)  # Logros obtenidos opcionales
    referencias = models.TextField(blank=True, null=True)  # Referencias opcionales

# Modelo para representar una formación académica
class FormacionAcademica(models.Model):
    titulo = models.CharField(max_length=255)  # Título de la formación
    nombre_academia = models.CharField(max_length=255)  # Nombre de la academia
    fecha_inicio = models.DateField()  # Fecha de inicio
    fecha_fin = models.DateField(blank=True, null=True)  # Fecha de finalización opcional
    referencias = models.TextField(blank=True, null=True)  # Referencias opcionales

# Modelo para representar una habilidad dura
class HardSkill(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre de la habilidad
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional

# Modelo para representar una habilidad blanda
class SoftSkill(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre de la habilidad
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional

# Modelo para representar un idioma
class Idioma(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del idioma
    nivel = models.CharField(max_length=50)  # Nivel de dominio del idioma
    certificaciones = models.TextField(blank=True, null=True)  # Certificaciones opcionales

# Modelo para representar un voluntariado
class Voluntariado(models.Model):
    puesto_voluntariado = models.CharField(max_length=255)  # Puesto de voluntariado
    fecha_inicio = models.DateField()  # Fecha de inicio
    fecha_final = models.DateField(blank=True, null=True)  # Fecha de finalización opcional
    nombre_entidad = models.CharField(max_length=255)  # Nombre de la entidad
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional
    logros_obtenidos = models.TextField(blank=True, null=True)  # Logros obtenidos opcionales
    referencias = models.TextField(blank=True, null=True)  # Referencias opcionales

# Modelo para representar un proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del proyecto
    descripcion = models.TextField()  # Descripción del proyecto
    enlace = models.URLField(blank=True, null=True)  # Enlace opcional al proyecto

# Modelo para representar una publicación
class Publicacion(models.Model):
    doi = models.CharField(max_length=100, blank=True, null=True)  # DOI opcional
    url = models.URLField(blank=True, null=True)  # URL opcional
    rol = models.CharField(max_length=255)  # Rol en la publicación
    nombre = models.CharField(max_length=255)  # Nombre de la publicación

# Modelo para representar un reconocimiento o premio
class ReconocimientoPremio(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del reconocimiento o premio
    entidad = models.CharField(max_length=255)  # Entidad que otorga el reconocimiento o premio
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional

# Modelo para representar una certificación o curso
class CertificacionCurso(models.Model):
    titulo = models.CharField(max_length=255)  # Título de la certificación o curso
    nombre_academia = models.CharField(max_length=255)  # Nombre de la academia
    fecha_inicio = models.DateField()  # Fecha de inicio
    fecha_fin = models.DateField(blank=True, null=True)  # Fecha de finalización opcional
