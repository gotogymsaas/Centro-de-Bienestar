from django.db import models
from django.contrib.auth.models import (
    User,
)  # Assuming each user corresponds to a profile


class PhysicalActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    steps = models.PositiveIntegerField()
    active_time = models.DurationField()  # Time active in hours/minutes

    def __str__(self):
        return f"Physical Activity for {self.user.username} on {self.date}"


class SleepQuality(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()  # Total sleep time
    quality_score = models.DecimalField(
        max_digits=5, decimal_places=2
    )  # Sleep quality index (0-10)

    def __str__(self):
        return f"Sleep Quality for {self.user.username} on {self.date}"


class StressLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    heart_rate_variability = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Measure of stress variability
    stress_score = models.DecimalField(
        max_digits=5, decimal_places=2
    )  # Derived stress level (0-10)

    def __str__(self):
        return f"Stress Level for {self.user.username} on {self.date}"


class Nutrition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    diet_quality_score = models.DecimalField(
        max_digits=5, decimal_places=2
    )  # Quality of diet (0-10)

    def __str__(self):
        return f"Nutrition Quality for {self.user.username} on {self.date}"


class SocialInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    interaction_count = models.PositiveIntegerField()  # Number of interactions
    quality_score = models.DecimalField(
        max_digits=5, decimal_places=2
    )  # Quality score (0-10)

    def __str__(self):
        return f"Social Interaction for {self.user.username} on {self.date}"


class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    mood_score = models.DecimalField(
        max_digits=5, decimal_places=2
    )  # Mood self-assessment (0-10)
    notes = models.TextField(blank=True, null=True)  # Optional notes

    def __str__(self):
        return f"Mood for {self.user.username} on {self.date}"


class CalendarUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    scheduled_events = models.PositiveIntegerField()  # Number of events scheduled
    active_time_spent = models.DurationField()  # Time spent on scheduled events

    def __str__(self):
        return f"Calendar Usage for {self.user.username} on {self.date}"


class HappinessIndex(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField()
    happiness_score = models.DecimalField(
        max_digits=5, decimal_places=2
    )  # Final happiness index (0-10)

    def __str__(self):
        return f"Happiness Index for {self.user.username} on {self.date}"
