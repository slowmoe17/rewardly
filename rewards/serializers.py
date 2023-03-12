from rest_framework.serializers import ModelSerializer
from .models import Reward, RedeemedReward


class RewardSerializer(ModelSerializer):
    class Meta:
        model = Reward
        fields = "__all__"


class RedeemedRewardSerializer(ModelSerializer):
    class Meta:
        model = RedeemedReward
        fields = "__all__"

