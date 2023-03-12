from django.contrib import admin
from .models import Reward , RedeemedReward 


admin.site.site_header = "Rewardly Admin"
admin.site.site_title = "Rewardly Admin Portal"
admin.site.index_title = "Welcome to Rewardly Portal"


admin.site.register(Reward)
admin.site.register(RedeemedReward)

