### In this readme file:

# 1- Project features.
# 2- Steps to start the project on your machine.

**Note: Rememer to flush the database if wanted, and create your own data :)**
### 1- Project Features:

- Shopping Cart.

- Storing carts in sessions `For more performance`.

- Using `cotext processor` for the cart and order_id.

- Asynchronous tasks using `Celery & Redis`.

- Integrating a payment gateway using `Stripe API`.

- A simple recommendation system using `Redis` that recommends products that have been bought with the product you want.

- A coupon system. after using the coupon it will be stored in the session.

### 2- Steps to start the project on your machine:

- Start a virtual environment:

  - `python -m venv env/myshop`

- Open the virtual environment:

  - `.\env\myshop\Scripts\activate`

- Install all the requirements:

  - `pip install -r requirements.txt`

- Start redis server to be able to start celery (redis is a message broker):

  - `redis-server`

- Start celery worker:

  - `celery -A myshop worker -l info -P gevent`

## Config settings.py:

# Redis settings

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

# Celery settings

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Stripe settings

**Use keys from your stripe account**
STRIPE_PUBLISHABLE_KEY = '' # Publishable key
STRIPE_SECRET_KEY = '' # Secret key
STRIPE_API_VERSION = ''
STRIPE_WEBHOOK_SECRET = ''
