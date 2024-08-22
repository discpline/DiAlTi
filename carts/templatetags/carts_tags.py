from django import template
from carts.models import Cart
from carts.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def user_carts(request):
    """
        Возвращает все корзины, связанные с текущим пользователем.

        Args:
            request (HttpRequest): Объект запроса, содержащий информацию о текущем пользователе.

        Returns:
            QuerySet: Набор данных, представляющий корзины пользователя.
    """
    # Вызов утилитной функции для получения корзин пользователя
    return get_user_carts(request)
