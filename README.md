# AI-Assisted Box Selection System

## Overview

This project is a Django REST Framework application that recommends the most suitable shipping box for an ecommerce order.

The system evaluates products and available shipping boxes based on dimensions, volume, weight capacity, and cost, then selects the cheapest valid box that can accommodate the order.

---

## Features

* Product management
* Shipping box management
* Box recommendation API
* Swagger/OpenAPI documentation
* Cost-optimized box selection
* Automated test cases using pytest
* Django Admin support

---

## Tech Stack

* Python 3.10+
* Django 5
* Django REST Framework
* SQLite
* drf-spectacular (Swagger/OpenAPI)
* pytest
* pytest-django

---

## Project Structure

```text
box_recommender_project/
│
├── api/
├── boxes/
├── orders/
├── products/
├── tests/
│
├── manage.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
└── pytest.ini
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd box_recommender_project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/api/docs/
```

---

## API Endpoint

### Recommend Box

**POST**

```text
/api/recommend-box/
```

### Sample Request

```json
{
  "items": [
    {
      "product_id": 1,
      "quantity": 3
    }
  ]
}
```

### Sample Response

```json
{
  "recommended_box": {
    "id": 2,
    "name": "Medium Box",
    "cost": "60.00"
  }
}
```

---

## Assumptions

* One box is recommended per order.
* Products may be rotated to fit within box dimensions.
* Recommendation is based on:

  * Weight capacity
  * Product dimensions
  * Total volume
  * Lowest box cost
* Full 3D bin packing is not implemented.

---

## Testing

Run tests:

```bash
python -m pytest
```

Expected result:

```text
3 passed
```

---

## Verification

Verified through:

* Django migrations
* Swagger API testing
* Multiple recommendation scenarios
* Automated pytest test suite

### Test Scenarios

| Quantity  | Expected Box |
| --------- | ------------ |
| 1 Laptop  | Small Box    |
| 2 Laptops | Small Box    |
| 3 Laptops | Medium Box   |

---

## Author

Ansh Agrawal
