import graphene
from .graphql_types import *
from graphql_relay import from_global_id
from graphql import GraphQLError


class CreateSrsMutation(relay.ClientIDMutation):
    srsfield = graphene.Field(SrsTypes)

    class Input:
        id = graphene.ID()
        age_year = graphene.Int()
        age_month = graphene.Int()
        r_name = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, age_year, age_month, r_name, id):
        std_obj = students.objects.get(pk=from_global_id(id)[1])
        if srs.objects.filter(childs_name=std_obj).exists():

            obj = srs(childs_name=std_obj, childs_age_month=age_month,
                      childs_age_year=age_year, raters_name=r_name)
            obj.save()
        return CreateSrsMutation(srsfield=obj)


class UpdateSrsMutation(relay.ClientIDMutation):
    srsfield = graphene.Field(SrsTypes)

    class Input:
        id = graphene.ID()
        age_year = graphene.Int()
        age_month = graphene.Int()
        r_name = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, age_year=None, age_month=None, r_name=None):
        obj = srs.objects.get(pk=from_global_id(id)[1])
        if age_year is not None:
            obj.childs_age_year = age_year
        if age_month is not None:
            obj.childs_age_month = age_month
        if r_name is not None:
            obj.raters_name = r_name
        obj.save()


class DeleteSrsMutation(relay.ClientIDMutation):
    srsfield = graphene.Field(SrsTypes)
    message = graphene.String()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        obj = srs.objects.filter(pk=from_global_id(id)[1]).delete()
        msg = "Srs Report deleted"
        return DeleteSrsMutation(srsfield=obj, message=msg)


class CreateRawScoreMutation(relay.ClientIDMutation):
    rawScore = graphene.Field(RawScoreType)

    class Input:
        id = graphene.ID()
        Awr = graphene.Int()
        Cog = graphene.Int()
        Com = graphene.Int()
        Mot = graphene.Int()
        RRB = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, Awr, Cog, Com, Mot, RRB):
        srs_obj = srs.objects.get(pk=from_global_id(id)[1])
        if raw_score.objects.filter(childs_name=srs_obj).exists():
            raise GraphQLError("Record already exist")

        else:
            q_1 = raw_score(Awr=Awr, Cog=Cog, Com=Com, Mot=Mot,
                            RRB=RRB, childs_name=srs_obj)
            q_1.save()

        return CreateRawScoreMutation(rawScore=q_1)


class UpdateRawScoreMutation(relay.ClientIDMutation):
    rawScore = graphene.Field(RawScoreType)

    class Input:
        id = graphene.ID()
        Awr = graphene.Int()
        Cog = graphene.Int()
        Com = graphene.Int()
        Mot = graphene.Int()
        RRB = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, Awr=None, Cog=None, Com=None, Mot=None, RRB=None):
        raw_obj = raw_score.objects.get(pk=from_global_id(id)[1])
        if Awr is not None:
            raw_obj.Awr = Awr
        if Cog is not None:
            raw_obj.Cog = Cog
        if Com is not None:
            raw_obj.Com = Com
        if Mot is not None:
            raw_obj.Mot = Mot
        if RRB is not None:
            raw_obj.RRB = RRB

        raw_obj.save()

        return UpdateRawScoreMutation(rawScore=raw_obj)


class CreateTScoreMutation(relay.ClientIDMutation):
    tScore = graphene.Field(TScoreType)

    class Input:
        id = graphene.ID()
        Awr = graphene.Int()
        Cog = graphene.Int()
        Com = graphene.Int()
        Mot = graphene.Int()
        RRB = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, Awr, Cog, Com, Mot, RRB):
        srs_obj = srs.objects.get(pk=from_global_id(id)[1])
        if t_score.objects.filter(childs_name=srs_obj).exists():
            raise GraphQLError("Record already exist")

        else:
            q_1 = t_score(Awr=Awr, Cog=Cog, Com=Com, Mot=Mot,
                          RRB=RRB, childs_name=srs_obj)
            q_1.save()

        return CreateTScoreMutation(tScore=q_1)


class UpdateTScoreMutation(relay.ClientIDMutation):
    tScore = graphene.Field(TScoreType)

    class Input:
        id = graphene.ID()
        Awr = graphene.Int()
        Cog = graphene.Int()
        Com = graphene.Int()
        Mot = graphene.Int()
        RRB = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, Awr=None, Cog=None, Com=None, Mot=None, RRB=None):
        t_obj = t_score.objects.get(pk=from_global_id(id)[1])
        if Awr is not None:
            t_obj.Awr = Awr
        if Cog is not None:
            t_obj.Cog = Cog
        if Com is not None:
            t_obj.Com = Com
        if Mot is not None:
            t_obj.Mot = Mot
        if RRB is not None:
            t_obj.RRB = RRB

        t_obj.save()

        return UpdateTScoreMutation(tScore=t_obj)
