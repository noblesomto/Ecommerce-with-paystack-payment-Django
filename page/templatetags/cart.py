from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(post, cart):
    keys = cart.keys()
    for id in keys:
        if id == post.prod_id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(post, cart):
    keys = cart.keys()
    for id in keys:
        if id == post.prod_id:
            return cart.get(id)
    return 0


@register.filter(name='total_price')
def total_price(post, cart):
    return int(post.product_price) * cart_quantity(post, cart)


@register.filter(name='total_cart_price')
def total_cart_price(post, cart):
    sum = 0
    for i in post:
        sum += total_price(i, cart)
    return sum


@register.filter(name='currency')
def currency(price):
    return "₦" + str(price)


@register.filter(name="multiply")
def multiply(n1, n2):
    return n1 * n2
