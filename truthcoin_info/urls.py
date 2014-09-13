from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView
from django.conf import settings

class TextPlainView(TemplateView):
  def render_to_response(self, context, **kwargs):
    return super(TextPlainView, self).render_to_response(context, content_type='text/plain', **kwargs)


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'truthcoin_info.views.home', name='home'),
    url(r'^voting/$', 'truthcoin_info.views.voting', name='voting'),
    url(r'^faq/$', 'truthcoin_info.views.faq', name='faq'),
    url(r'^monetization/$', 'truthcoin_info.views.monetization', name='monetization'),
    url(r'^timeline/$', 'truthcoin_info.views.timeline', name='timeline'),
    url(r'^team/$', 'truthcoin_info.views.team', name='team'),
    url(r'^press/$', 'truthcoin_info.views.press', name='press'),

    url(r'^vote$', 'truthcoin_info.views.vote', name='vote'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # django static
  	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
  	url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
  	url(r'^favicon\.ico$', RedirectView.as_view(url='%simages/favicon.ico' % settings.STATIC_URL)),
)