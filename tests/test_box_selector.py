import pytest

from products.models import Product
from boxes.models import Box
from boxes.services.box_selector import BoxSelector


@pytest.mark.django_db
def test_small_box_selected():
    product = Product.objects.create(
        name="Laptop",
        length=30,
        width=20,
        height=5,
        weight=2
    )

    Box.objects.create(
        name="Small Box",
        inner_length=35,
        inner_width=25,
        inner_height=10,
        max_weight=5,
        cost=40
    )

    result = BoxSelector().recommend([
        {"product_id": product.id, "quantity": 1}
    ])

    assert result["recommended_box"]["name"] == "Small Box"


@pytest.mark.django_db
def test_medium_box_selected_due_to_weight():
    product = Product.objects.create(
        name="Laptop",
        length=30,
        width=20,
        height=5,
        weight=2
    )

    Box.objects.create(
        name="Small Box",
        inner_length=35,
        inner_width=25,
        inner_height=10,
        max_weight=5,
        cost=40
    )

    Box.objects.create(
        name="Medium Box",
        inner_length=50,
        inner_width=40,
        inner_height=20,
        max_weight=10,
        cost=60
    )

    result = BoxSelector().recommend([
        {"product_id": product.id, "quantity": 3}
    ])

    assert result["recommended_box"]["name"] == "Medium Box"


@pytest.mark.django_db
def test_no_box_found():
    product = Product.objects.create(
        name="Heavy Machine",
        length=100,
        width=100,
        height=100,
        weight=100
    )

    result = BoxSelector().recommend([
        {"product_id": product.id, "quantity": 1}
    ])

    assert result["recommended_box"] is None