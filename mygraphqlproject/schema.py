import graphene
from graphene import ObjectType, List, Int, String, Field
import csv
import os
from django.conf import settings

class ChallengeType(ObjectType):
    challenge_id = Int()
    challenge_name = String()
    challenge_success_rate = Int()

class Query(ObjectType):
    challenges = List(ChallengeType)

    def resolve_challenges(self, info):
        csv_file_path = os.path.join(settings.BASE_DIR, 'data', 'challenges.csv')

        challenges = []
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                challenges.append({
                    'challenge_id': int(row['ChallengeID']),
                    'challenge_name': row['ChallengeName'],
                    'challenge_success_rate': int(row['ChallengeSuccessRate']),
                })

        return challenges

schema = graphene.Schema(query=Query)