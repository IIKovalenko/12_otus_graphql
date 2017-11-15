# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse

from . import models


class ProductsListView(ListView):
    model = models.Product


class ProductsDetailView(DetailView):
    model = models.Product


class FormSubmitView(View):
    def post(self, request, *args, **kwargs):
        print(request.body)
        return JsonResponse({'status': 'ok'})
