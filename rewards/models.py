from django.db import models
from users.models import User
class Reward(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.points} points"



class RedeemedReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} redeemed {self.reward} at {self.redeemed_at}"

    class Meta:
        verbose_name_plural = "Redeemed Rewards"        