from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns(
    'web.views',
    url(r'^$', 'events.index', name='web.index'),
    url(r'^map/$', 'events.map', name='web.map'),
    url(r'^add/$', 'events.add_event', name='web.add_event'),
    url(r'^edit/(?P<event_id>\d+)/$', 'events.edit_event', name='web.edit_event'),
    url(r'^view/(?P<event_id>\d+)/(?P<slug>[-\w]+)/$', 'events.view_event', name='web.view_event'),
    url(r'^view/(?P<event_id>[0-9]+)/$', 'events.view_event_by_id', name='web.view_event_by_id'),
    url(r'^view/(?P<country_code>\w+)/$', 'events.view_event_by_country', name='web.view_event_by_country'),
    url(r'^search/$', 'events.search_events', name='web.search_events'),
    url(r'^approved/(?P<country_code>\w{2,3})/$', 'events.list_approved_events', name='web.list_events'),
    url(r'^pending/(?P<country_code>\w{2,3})/$', 'events.list_pending_events', name='web.pending_events'),
    url(r'^my/$', 'events.created_events', name='web.created_events'),
    url(r'^guide/$', TemplateView.as_view(template_name="pages/guide.html"), name='web.guide'),
    url(r'^about/$', TemplateView.as_view(template_name="pages/about.html"), name='web.about'),
    url(r'^login/$', 'users.login', name='web.login'),
    url(r'^ambassadors/$', 'users.ambassadors', name='web.ambassadors'),
    url(r'^scoreboard/$', 'events.scoreboard', name='web.scoreboard'),
    url(r'^change_status/(?P<event_id>\d+)/$', 'events.change_status', name='web.change_status'),
    url(r'^reject_status/(?P<event_id>\d+)/$', 'events.reject_status', name='web.reject_status'),
    url(r'^(?P<country_code>[A-Z][A-Z])/?$', RedirectView.as_view(url='/#!%(country_code)s')),
    url(r'^map/(?P<country_code>[A-Z][A-Z])/?$', RedirectView.as_view(url='/#!%(country_code)s')),
)
