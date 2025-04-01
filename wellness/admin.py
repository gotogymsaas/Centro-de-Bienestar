from django.contrib import admin
from .models import (
    PhysicalActivity,
    SleepQuality,
    StressLevel,
    Nutrition,
    SocialInteraction,
    Mood,
    CalendarUsage,
    HappinessIndex,
)

admin.site.register(PhysicalActivity)
admin.site.register(SleepQuality)
admin.site.register(StressLevel)
admin.site.register(Nutrition)
admin.site.register(SocialInteraction)
admin.site.register(Mood)
admin.site.register(CalendarUsage)
admin.site.register(HappinessIndex)
