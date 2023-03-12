from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Reward,RedeemedReward
from .serializers import RedeemedReward , RedeemedRewardSerializer
from users.models import Profile
from users.serializers import ProfileSerializer


class RewardList(generics.ListAPIView):
    queryset = Reward.objects.all()
    serializer_class = RedeemedRewardSerializer
    permission_classes = [permissions.IsAuthenticated]


class RedeemReward(generics.CreateAPIView):
    queryset = RedeemedReward.objects.all()
    serializer_class = RedeemedRewardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        reward_id = request.data.get("reward")
        reward = Reward.objects.get(id=reward_id)
        if user.points >= reward.points:
            user.points -= reward.points
            user.save()
            RedeemedReward.objects.create(user=user, reward=reward)
            return Response(
                {"message": "Reward redeemed successfully"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "You don't have enough points"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
class NewQrRedeem(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request, *args, **kwargs):
        queryset = Profile.objects.all()
        user = self.request.user
        balance = queryset.filter(user=user).get(balance)
        new_points = request.data["points"]
        balance += new_points
        Profile.objects.filter(user=user).update(balance=balance)
        return Response(
            {   "status": "success",
                "message": "Points added successfully",
                "data": f"{new_points} points added to your account , your new balance is {balance}" },
            status=status.HTTP_200_OK,
        )
    
    

