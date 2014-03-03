from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin
from preview_forms import AddEventFormPreview
from web.forms.event_form import AddEvent

admin.autodiscover()

urlpatterns = patterns(
	'web.views',
	url(r'^$', 'events.index', name='web.index'),
	url(r'^add/$', 'events.add_event', name='web.add_event'),
	url(r'^edit/(?P<event_id>\d+)/$', 'events.edit_event', name='web.edit_event'),
	url(r'^view/(?P<event_id>\d+)/(?P<slug>[-\w]+)/$', 'events.view_event', name='web.view_event'),
	url(r'^thankyou/$', 'events.thankyou', name='web.thankyou'),
	url(r'^approved/(?P<country_code>\w{2,3})/$',"events.list_approved_events",name="web.list_events"),
	url(r'^pending/(?P<country_code>\w{2,3})/$', "events.list_pending_events",name="web.pending_events"),
	url(r'^guide/$', 'events.guide', name='web.guide'),	
	url(r'^login/$', 'users.login', name='web.login'),
	url(r'^ambassadors/$', 'users.ambassadors', name='web.ambassadors'),
	 url(r'^change_status/(?P<status>\w+)/(?P<event_id>\d+)/$','events.change_status',name='web.change_status'),
	)

urlpatterns+= patterns(
	'',
	url(r'^add/$',AddEventFormPreview(AddEvent),name='web.preview_event'),
	)
