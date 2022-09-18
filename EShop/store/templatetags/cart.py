from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(p ,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==p.id:
            return True
    return False

    # print(keys)
    # print(p,cart)
    # return True


@register.filter(name='cart_qty')
def cart_qty(p ,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==p.id:
            return cart.get(id)
    return 0


@register.filter(name='total')
def total(p ,cart):
    return p.price * cart_qty(p,cart)


@register.filter(name='total_price')
def total_price(products, cart):
    sum = 0
    for p in products:
        sum+= total(p, cart)
    return sum
