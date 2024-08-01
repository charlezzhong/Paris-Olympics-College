import graphene
from graphene_django.types import DjangoObjectType
from .models import Athlete, School, Sport, AthleteSchool, AthleteSport

class AthleteType(DjangoObjectType):
    class Meta:
        model = Athlete

class SchoolType(DjangoObjectType):
    class Meta:
        model = School

class SportType(DjangoObjectType):
    class Meta:
        model = Sport

class AthleteSchoolType(DjangoObjectType):
    class Meta:
        model = AthleteSchool

class AthleteSportType(DjangoObjectType):
    class Meta:
        model = AthleteSport

class Query(graphene.ObjectType):
    all_athletes = graphene.List(AthleteType)
    all_schools = graphene.List(SchoolType)
    all_sports = graphene.List(SportType)

    def resolve_all_athletes(self, info, **kwargs):
        return Athlete.objects.all()

    def resolve_all_schools(self, info, **kwargs):
        return School.objects.all()

    def resolve_all_sports(self, info, **kwargs):
        return Sport.objects.all()

schema = graphene.Schema(query=Query)