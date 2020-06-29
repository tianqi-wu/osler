from __future__ import unicode_literals
from django.urls import re_path

from osler.core.urls import wrap_url
from osler.inventory import views
from osler.inventory import models

unwrapped_urlconf = [
    re_path(
        r'^$',
        views.drug_list,
        name='drug-list'),
    re_path(
        r'^add-new-drug/$',
        views.DrugAddNew.as_view(),
        name='drug-add-new'),
    re_path(
        r'^pre-add-new-drug/$',
        views.PreDrugAddNew.as_view(),
        name='pre-drug-add-new'),
    re_path(
        r'^predrug-select/$',
        views.PreDrugSelect.as_view(),
        name="predrug-select"),
    re_path(
        r'^drug/update/(?P<pk>[0-9]+)/$',
        views.DrugUpdate.as_view(),
        name='drug-update'),
    re_path(
        r'^drug_delete/(?P<pk>[0-9]+)/$',
        views.drug_delete,
        name='drug-delete'),
    re_path(
        r'^drug-add/$',
        views.drug_add,
        name='drug-add'),
    re_path(
        r'^drug-dispense/$',
        views.drug_dispense,
        name='drug-dispense'),
]

wrap_config = {}
urlpatterns = [wrap_url(u, **wrap_config) for u in unwrapped_urlconf]
