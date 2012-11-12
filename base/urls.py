from django.conf.urls import url, patterns
from django.views.generic import TemplateView

urlpatterns = patterns('base.views',
    url('^$', TemplateView.as_view(template_name="base/index.html"), name="home"),
)
