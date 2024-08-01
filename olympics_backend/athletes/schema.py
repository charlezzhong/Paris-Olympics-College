
"""import graphene
from graphene_django import DjangoObjectType
from .models import ultitable

class AthleteType(DjangoObjectType):
    class Meta:
        model = ultitable

class Query(graphene.ObjectType):
    athlete = graphene.Field(AthleteType, id=graphene.Int())
    athletes = graphene.List(
        AthleteType,
        first_name=graphene.String(),
        last_name=graphene.String(),
        school=graphene.String(),
        conference=graphene.String(),
        division=graphene.String(),
        ncaa_sport=graphene.String(),
        olympic_sport=graphene.String(),
        country_team=graphene.String(),
        olympic_role=graphene.String()
    )
    
    all_athletes = graphene.List(AthleteType) 

    def resolve_athlete(self, info, id):
        return ultitable.objects.get(pk=id)

    def resolve_athletes(self, info, first_name=None, last_name=None, school=None, conference=None, division=None, ncaa_sport=None, olympic_sport=None, country_team=None, olympic_role=None):
        filters = {}
        if first_name:
            filters['first_name__icontains'] = first_name
        if last_name:
            filters['last_name__icontains'] = last_name
        if school:
            filters['school__icontains'] = school
        if conference:
            filters['conference__icontains'] = conference
        if division:
            filters['division__icontains'] = division
        if ncaa_sport:
            filters['ncaa_sport__icontains'] = ncaa_sport
        if olympic_sport:
            filters['olympic_sport__icontains'] = olympic_sport
        if country_team:
            filters['country_team__icontains'] = country_team
        if olympic_role:
            filters['olympic_role__icontains'] = olympic_role

        return ultitable.objects.filter(**filters)
    
    def resolve_all_athletes(self, info):
        return ultitable.objects.all()  # This returns all athletes

schema = graphene.Schema(query=Query)"""
import graphene
from graphene_django import DjangoObjectType
from .models import Ultitable

class UltitableType(DjangoObjectType):
    class Meta:
        model = Ultitable

class Query(graphene.ObjectType):
    ultitable = graphene.Field(UltitableType, id=graphene.Int())
    ultitables = graphene.List(
        UltitableType,
        first_name=graphene.String(),
        last_name=graphene.String(),
        school=graphene.String(),
        conference=graphene.String(),
        division=graphene.String(),
        ncaa_sport=graphene.String(),
        olympic_sport=graphene.String(),
        country_team=graphene.String(),
        olympic_role=graphene.String()
    )

    def resolve_ultitable(self, info, id):
        return Ultitable.objects.get(pk=id)

    def resolve_ultitables(self, info, first_name=None, last_name=None, school=None, conference=None, division=None, ncaa_sport=None, olympic_sport=None, country_team=None, olympic_role=None):
        filters = {}
        if first_name:
            filters['first_name__icontains'] = first_name
        if last_name:
            filters['last_name__icontains'] = last_name
        if school:
            filters['school__icontains'] = school
        if conference:
            filters['conference__icontains'] = conference
        if division:
            filters['division__icontains'] = division
        if ncaa_sport:
            filters['ncaa_sport__icontains'] = ncaa_sport
        if olympic_sport:
            filters['olympic_sport__icontains'] = olympic_sport
        if country_team:
            filters['country_team__icontains'] = country_team
        if olympic_role:
            filters['olympic_role__icontains'] = olympic_role

        return Ultitable.objects.filter(**filters)

schema = graphene.Schema(query=Query)