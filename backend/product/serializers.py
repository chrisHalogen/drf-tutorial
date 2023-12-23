from rest_framework import serializers
from .models import Product
from decimal import Decimal
from django.urls import reverse

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"



class ProductSerializer___(serializers.ModelSerializer):
    on_sale = serializers.SerializerMethodField(read_only=True)
    sale_price = serializers.SerializerMethodField(read_only=True)
    detail_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        exclude = ['id']

    def get_on_sale(self, obj):
        if obj:
            return True

    def get_sale_price(self, obj):
        if self.get_on_sale(self):
            original_price = obj.price
            sale_price = original_price - (Decimal('0.2') * original_price)
            return round(sale_price, 2)
        return None
    
    def get_detail_url(self, obj):
        return reverse("product_detail", kwargs={"pk": obj.pk})
