from django.contrib import admin
from django.urls import path
from rewards.views import RewardList , RedeemReward , NewQrRedeem
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rewards/', RewardList.as_view()),
    path('redeem/', RedeemReward.as_view()),
    path('qr-redeem/', NewQrRedeem.as_view()),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)