from decimal import Decimal, ROUND_HALF_UP

DEFAULT_PRICE_UNDERGRAD = Decimal('20.00') 
DEFAULT_PRICE_GRAD = Decimal('35.00')

MIN_PRICE = Decimal('15.70') # minimum wage
MAX_PRICE = Decimal('150.00')

def calc_price_suggestion(tutor):

    is_grad_student = getattr(tutor, 'is_graduate', False)

    try:
        from bookings.models import Available_Slots
        existing_prices = Available_Slots.objects.values_list('session_price', flat=True)
        valid_prices = [Decimal(str(p)) for p in existing_prices if p is not None]
    except Exception:
        valid_prices = None

    if not valid_prices:
        return DEFAULT_PRICE_GRAD if is_grad_student else DEFAULT_PRICE_UNDERGRAD

    suggested_price = sum(valid_prices) / len(valid_prices)
    return suggested_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

