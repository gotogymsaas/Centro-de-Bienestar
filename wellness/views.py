from django.views.generic import TemplateView
from django.db.models.functions import TruncMonth
from django.db.models import Sum, Avg
import json
from .models import PhysicalActivity  # Asegúrate de importar el modelo correctamente


class ChartView(TemplateView):
    template_name = "wellness/chart_tem.html"  # Ruta del template

    def get_context_data(self, **kwargs):
        # Obtiene el contexto base
        context = super().get_context_data(**kwargs)

        # Consulta y agrupación por mes para el usuario logueado
        user = self.request.user  # Obtén el usuario actual
        activities = (
            PhysicalActivity.objects.filter(user=user)  # Filtra por el usuario logueado
            .annotate(month=TruncMonth("date"))  # Agrupa por mes
            .values("month")  # Obtén solo los meses
            .annotate(
                total_steps=Sum("steps"),  # Suma total de pasos
                average_active_time=Avg("active_time"),  # Promedio de tiempo activo
            )
            .order_by("month")  # Ordena por fecha
        )

        # Extrae los datos para el gráfico
        labels = [entry["month"].strftime("%B %Y") for entry in activities]
        ventas = [entry["total_steps"] for entry in activities]
        gastos = [
            entry["average_active_time"].total_seconds() / 3600 for entry in activities
        ]  # Convierte a horas

        # Agrega los datos al contexto
        context["labels"] = json.dumps(labels)  # Etiquetas para el eje X
        context["ventas"] = json.dumps(ventas)  # Pasos totales como "ventas"
        context["gastos"] = json.dumps(gastos)  # Tiempo activo promedio como "gastos"

        return context
