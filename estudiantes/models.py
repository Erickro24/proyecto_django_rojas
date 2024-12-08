from django.db import models
from django.core.exceptions import ValidationError

# Validacion
def validar_matricula(value):
    if not value.isnumeric() or len(value) != 4:
        raise ValidationError("La matrícula debe tener 4 dígitos numéricos.")

# Modelo_1: Estudiante
class Estudiante(models.Model):
    matricula = models.CharField(max_length=8, validators=[validar_matricula], unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo_2: Curso
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

# Modelo_3: Inscripcion
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante} inscrito en {self.curso}"

# Modelo_4: Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
