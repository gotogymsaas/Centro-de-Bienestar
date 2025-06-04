from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import ReferralClick, OrderReferral, Influencer
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InfluencerRegistrationForm

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


class InfluencerRegisterView(LoginRequiredMixin, CreateView):
    model = Influencer
    form_class = InfluencerRegistrationForm
    template_name = "influencers/register.html"
    success_url = reverse_lazy("influencers:dashboard")

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, "influencer"):
            return redirect("influencers:dashboard")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
