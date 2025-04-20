from django.views.generic import TemplateView
from .models import ReferralClick, OrderReferral
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "influencers/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        inf = getattr(self.request.user, "influencer", None)
        if inf:
            ctx["clicks"]      = ReferralClick.objects.filter(influencer=inf).count()
            ctx["orders"]      = OrderReferral.objects.filter(influencer=inf)
            ctx["total_commission"] = sum(o.amount for o in ctx["orders"])
        else:
            ctx["clicks"] = ctx["orders"] = ctx["total_commission"] = 0
        return ctx
