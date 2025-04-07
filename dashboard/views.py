from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.db.models.functions import TruncMonth
from django.db.models import Count, Avg, Sum

# Importar modelos de otras apps
from metric.models import NetPromoterScore
from orders.models import Order
from users.models import UserProfile
from products.models import Product
from service.models import Company
from wellness.models import HappinessIndex, PhysicalActivity

def auth_dashboard(request):
    """
    Vista del dashboard principal del administrador GoToGym.
    Resume el estado actual del ecosistema: usuarios, pedidos, bienestar, etc.
    """

    # Sección 1: Usuarios y Grupos
    user_count = User.objects.count()
    group_count = Group.objects.count()
    profile_count = UserProfile.objects.count()

    # Sección 2: Métrica de Satisfacción (NPS)
    nps_qs = NetPromoterScore.objects.values('date').annotate(total=Count('id')).order_by('date')
    nps_labels = [entry['date'].strftime("%Y-%m-%d") for entry in nps_qs if entry['date']]
    nps_data = [entry['total'] for entry in nps_qs]
    nps_avg = NetPromoterScore.objects.aggregate(avg_score=Avg('score'))['avg_score']

    # Sección 3: Pedidos (Estado de los pedidos)
    orders_qs = Order.objects.values('status').annotate(total=Count('id'))
    orders_labels = [entry['status'] for entry in orders_qs]
    orders_data = [entry['total'] for entry in orders_qs]

    # Sección 4: Productos
    product_count = Product.objects.count()

    # Sección 5: Compañías (clientes corporativos)
    company_count = Company.objects.count()

    # Sección 6: Datos de Bienestar
    avg_happiness = HappinessIndex.objects.aggregate(avg=Avg('happiness_score'))['avg']
    total_physical_activity = PhysicalActivity.objects.aggregate(total=Sum('steps'))['total']

    # Consolidar en el contexto para visualización
    context = {
        'user_count': user_count,
        'group_count': group_count,
        'profile_count': profile_count,
        'product_count': product_count,
        'company_count': company_count,
        'nps_labels': nps_labels,
        'nps_data': nps_data,
        'nps_avg': round(nps_avg or 0, 2),
        'orders_labels': orders_labels,
        'orders_data': orders_data,
        'avg_happiness': round(avg_happiness or 0, 2),
        'total_physical_activity': total_physical_activity or 0,
    }
    return render(request, 'dashboard/auth_dashboard.html', context)

