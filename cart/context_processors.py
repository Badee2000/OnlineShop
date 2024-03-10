from .cart import Cart


# Instantiate the cart using the request object and make it available for
# the templates as a variable named cart.
def cart(request):
    return {'cart': Cart(request)}
