from .models import ProductInBasket


def basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
        request.session.cycle_key()
    products_total_count = ProductInBasket.objects.filter(session_key=session_key).count()
    return locals()