# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from apps.gcd.views import accounts as account_views
from apps.mycomics import views as mycomics_views

urlpatterns = patterns('',
    url(r'^$', mycomics_views.index, name='home'),
    url(r'^accounts/login/$', account_views.login,
        {'template_name': 'mycomics/index.html',
        'landing_view': 'collections_list'},
        name='my_login'),
    url(r'^collection/list/$',
        mycomics_views.collections_list,
        name='collections_list'),
    url(r'^collection/(?P<collection_id>\d+)/',
        mycomics_views.view_collection,
        name='view_collection'),
    url(r'^collection/add/$',
        mycomics_views.edit_collection,
        name='add_collection'),
    url(r'^collection/edit/(?P<collection_id>\d+)/$',
        mycomics_views.edit_collection,
        name='edit_collection'),
    url(r'^collection/delete/(?:(?P<collection_id>\d+)?)$',
        mycomics_views.delete_collection,
        name='delete_collection'),

    url(r'^issue/(?P<issue_id>\d+)/collection/(?P<collection_id>\d+)/view/$',
        mycomics_views.view_issue_in_collection, name='view_issue_in_collection'),
    url(r'^issue/(?P<issue_id>\d+)/save/$',
        mycomics_views.save_issue, name='save_issue'),
    url(r'^issue/(?P<issue_id>\d+)/collection/(?P<collection_id>\d+)/delete/$',
        mycomics_views.delete_collection_item, name='delete_collection_item'),

    url(r'^series/(?P<series_id>\d+)/add_to_collection/$',
     mycomics_views.add_series_issues_to_collection, name='my_series_issues'),
    url(r'^issue/(?P<issue_id>\d+)/add_to_collection/$',
     mycomics_views.add_single_issue_to_collection, name='my_issue'),

    url(r'^mycomics_search/$',
      mycomics_views.mycomics_search, name='mycomics_search'),

    url(r'message/$', mycomics_views.display_message, name='display_message'),

)