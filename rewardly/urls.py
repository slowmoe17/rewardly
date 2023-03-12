from django.contrib import admin
from django.urls import path
from rewards.views import RewardList , RedeemReward , NewQrRedeem
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rewards/', RewardList.as_view()),
    path('redeem/', RedeemReward.as_view()),
    path('qr-redeem/', NewQrRedeem.as_view()),
]
