from django.test import TestCase

from decimal import Decimal

from .models import Category, Product


class ProductModelTests(TestCase):
    """Tests for the ``Product`` model."""

    def test_in_stock_with_positive_stock(self):
        """``in_stock`` should return ``True`` when stock is greater than zero."""
        category = Category.objects.create(name="Test Category")
        product = Product.objects.create(
            name="Test Product",
            price=Decimal("10.00"),
            stock=5,
            category=category,
        )

        self.assertTrue(product.in_stock())
