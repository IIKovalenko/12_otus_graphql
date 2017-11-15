import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from . import models


class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category
        interfaces = (graphene.relay.Node, )
        filter_fields = ('title', )


class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product
        filter_fields = {
            'title': ['exact', 'icontains', ],
        }
        interfaces = (graphene.relay.Node, )


class Query(graphene.AbstractType):
    categories = DjangoFilterConnectionField(CategoryType)
    products = DjangoFilterConnectionField(ProductType)

    def resolve_categories(self, info, **kwargs):
        return models.Category.objects.all()

    def resolve_products(self, info, **kwargs):
        return models.Product.objects.select_related('category').all()


class CreateProduct(graphene.Mutation):
    class Arguments:
        title = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, title):
        product = models.Product(
            title=title,
            description='blah',
            category_id=1,
            is_published=True
        )
        product.save()
        return CreateProduct(ok=True)
