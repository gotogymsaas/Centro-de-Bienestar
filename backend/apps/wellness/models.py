from django.db import models
from django.contrib.auth.models import User

class PhysicalActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    steps = models.PositiveIntegerField()
    active_time = models.DurationField()  # Tiempo activo (horas/minutos)

    def __str__(self):
        return f"Physical Activity for {self.user.username} on {self.date}"

class SleepQuality(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()  # Tiempo total de sueño
    quality_score = models.DecimalField(max_digits=5, decimal_places=2)  # Índice de calidad de sueño (0-100)

    def __str__(self):
        return f"Sleep Quality for {self.user.username} on {self.date}"

class StressLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    heart_rate_variability = models.DecimalField(max_digits=10, decimal_places=2)  # Variabilidad de la frecuencia cardíaca
    stress_score = models.DecimalField(max_digits=5, decimal_places=2)  # Nivel de estrés derivado (0-10)

    def __str__(self):
        return f"Stress Level for {self.user.username} on {self.date}"

class Nutrition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    diet_quality_score = models.DecimalField(max_digits=5, decimal_places=2)  # Calidad de la dieta (0-100)

    def __str__(self):
        return f"Nutrition Quality for {self.user.username} on {self.date}"

class SocialInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    interaction_count = models.PositiveIntegerField()  # Número de interacciones
    quality_score = models.DecimalField(max_digits=5, decimal_places=2)  # Puntuación de calidad (0-10)

    def __str__(self):
        return f"Social Interaction for {self.user.username} on {self.date}"

class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    mood_score = models.DecimalField(max_digits=5, decimal_places=2)  # Autoevaluación del estado de ánimo (0-10)
    notes = models.TextField(blank=True, null=True)  # Notas opcionales

    def __str__(self):
        return f"Mood for {self.user.username} on {self.date}"

class CalendarUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    scheduled_events = models.PositiveIntegerField()  # Número de eventos programados
    active_time_spent = models.DurationField()  # Tiempo empleado en los eventos programados

    def __str__(self):
        return f"Calendar Usage for {self.user.username} on {self.date}"

class HappinessIndex(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField()
    happiness_score = models.DecimalField(max_digits=5, decimal_places=2)  # Índice final de felicidad (0-10)

    def __str__(self):
        return f"Happiness Index for {self.user.username} on {self.date}"

