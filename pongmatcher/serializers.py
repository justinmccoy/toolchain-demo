from rest_framework import serializers
from pongmatcher.models import MatchRequest, Participant
from pongmatcher.finders import Match
import json

class MatchRequestSerializer(serializers.Serializer):
    id = serializers.CharField(source='uuid')
    player = serializers.CharField(source='player_uuid')
    match_id = serializers.CharField(required=False)

    def create(self, validated_data):
        match_request = MatchRequest.objects.create(**validated_data)
        match_request.persist_participants()
        return match_request

class MatchSerializer:
    def __init__(self, match):
        self.match = match
        self.data = {
                'id': match.uuid,
                'match_request_1_id': match.match_request_1_uuid,
                'match_request_2_id': match.match_request_2_uuid,
                }
