from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from graphene_django.views import GraphQLView

from shop.schema import schema
from products import views as products_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),

    url(r'^submit_order/', products_views.SubmitOrderView.as_view()),
    url(r'^products/$', products_views.ProductsListView.as_view()),
    url(
        r'^products/(?P<pk>[0-9]+)/$',
        products_views.ProductsDetailView.as_view(),
        name='product_detail',
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
