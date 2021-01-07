import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from .graphql_types import *
from .models import *
from graphql_relay import from_global_id
from .mutations import CreateRawScoreMutation, CreateSrsMutation, UpdateRawScoreMutation, UpdateSrsMutation, CreateTScoreMutation, UpdateTScoreMutation, DeleteSrsMutation


class Query(graphene.ObjectType):
    srs_by_student = graphene.List(SrsTypes, id=graphene.ID(required=True))
    all_students = DjangoFilterConnectionField(StudentsTypes)
    all_srsreport = DjangoFilterConnectionField(SrsTypes)

    def resolve_srs_by_student(root, info, id):
        obj = students.objects.get(id=from_global_id(id)[1])
        if srs.objects.filter(childs_name=obj).exists():
            return srs.objects.filter(childs_name=obj)
        else:
            return None


class Mutation(graphene.ObjectType):
    create_rawscore = CreateRawScoreMutation.Field()
    create_srs = CreateSrsMutation.Field()
    update_srs = UpdateSrsMutation.Field()
    update_rawscore = UpdateRawScoreMutation.Field()
    create_tscore = CreateTScoreMutation.Field()
    update_tscore = UpdateTScoreMutation.Field()
    delete_srs = DeleteSrsMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
