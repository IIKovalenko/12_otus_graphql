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


class SubmitOrderView(View):
    def post(self, request, *args, **kwargs):
        print(request.body)
        # TODO: save order
        return JsonResponse(
            {'status': 'ok',
            'text': 'Ваш заказ оформлен и мы вам напишем в течении трёх часов.'
            }
        )
