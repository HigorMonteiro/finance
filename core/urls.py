from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from core import views


router = routers.DefaultRouter()
router.register(r'bills', views.BillView, 'bills')
router.register(r'card_bills', views.BillCardView, 'card_bills')
router.register(r'cred_cards', views.CreditCardView, 'cred_cards')
router.register(r'categories', views.CategoryView, 'categories')

urlpatterns = [
    path("v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Finance API')),
]