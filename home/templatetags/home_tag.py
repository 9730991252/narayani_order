from django import template
from owner.models import *
from django.db.models import Avg, Sum, Min, Max
from math import *
import math
from datetime import date
from order.models import *

register = template.Library()

@register.inclusion_tag('inclusion_tag/home/price_and_weight.html')
def price_and_weight(item_id):
    p = Price_and_weight.objects.filter(item_id=item_id, status=1).first()
    if p:
        return{
            'weight':p.weight,
            'price':p.price,
            'unit':p.unit,
            'item_id':item_id,
            'price_and_weight':Price_and_weight.objects.filter(item_id=item_id, status=1)
        }
        
@register.simple_tag()
def courier_charges(customer_id):
    customer = Customer.objects.filter(id=customer_id).first()
    total_weight_kg = 0
    for c in Cart.objects.filter(customer_id=customer.id):
        if c.price_and_weight.unit == 'KG':
            gm = (c.price_and_weight.weight * 1000)
        else:
            gm = c.price_and_weight.weight
        gm = (gm * c.qty)
        total_weight_kg += gm / 1000
    if int(customer.state) == 1:
        print(total_weight_kg)
        c = (total_weight_kg).is_integer()
        if c == False:
            return 45
        else:
            return 0
    else:
        return (int(math.ceil(total_weight_kg)) * 90)
    