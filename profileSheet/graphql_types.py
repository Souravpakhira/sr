from graphene import relay
import graphene
from graphene_django.types import DjangoObjectType
from .models import srs, raw_score, t_score, students


class StudentsTypes(DjangoObjectType):
    class Meta:
        model = students
        filter_fields = '__all__'
        interfaces = (relay.Node,)


class SrsTypes(DjangoObjectType):
    class Meta:
        model = srs
        filter_fields = "__all__"
        interfaces = (relay.Node,)


class RawScoreType(DjangoObjectType):
    class Meta:
        model = raw_score
        filter_fields = "__all__"
        interfaces = (relay.Node,)


class TScoreType(DjangoObjectType):
    class Meta:
        model = t_score
        filter_fields = "__all__"
        interfaces = (relay.Node,)
