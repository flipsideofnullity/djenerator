from models import *
from django.db.models import Q
from django.views.generic import *

class ProfileListView(ListView):
    model = Profile
    template_name='auth_profile_module/profile_list.html'
    paginate_by = 12

    def get_queryset(self):
        qs = super(ProfileListView, self).get_queryset()
        q = self.request.GET.get("q", None)

        if q:
            qs = qs.filter(
                Q(user__username__iexact=q) |
                Q(user__email__iexact=q) |
                Q(user__first_name__icontains=q) |
                Q(user__last_name__icontains=q) |
                Q(about__icontains=q)
            )

        return qs
