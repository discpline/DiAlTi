from django.contrib import admin
from carts.models import Cart


# Админский табличный интерфейс для управления элементами корзины
class CartTabAdmin(admin.TabularInline):
    model = Cart  # Указывает, что эта вкладка будет работать с моделью Cart
    fields = ("product", "quantity", "created_timestamp")  # Поля, отображаемые в админке
    search_fields = ("product", "quantity", "created_timestamp")  # Поля, по которым можно осуществлять поиск
    readonly_fields = ("created_timestamp",)  # Поля, которые нельзя редактировать
    extra = 1  # Количество пустых строк для добавления новых объектов


# Регистрация модели Cart в админке с пользовательскими настройками
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Конфигурация отображения модели Cart в административной панели.
    """
    list_display = [
        'user_display',  # Отображение пользователя
        'product_display',  # Отображение названия продукта
        'quantity',  # Отображение количества
        'created_timestamp'  # Отображение времени создания
    ]
    list_filter = [
        'created_timestamp',  # Фильтрация по времени создания
        'user',  # Фильтрация по пользователю
        'product__name',  # Фильтрация по названию продукта
    ]

    def user_display(self, obj):
        """
        Возвращает имя пользователя или 'Анонимный пользователь', если пользователь не указан.

        Args:
            obj (Cart): Объект корзины.

        Returns:
            str: Имя пользователя или 'Анонимный пользователь'.
        """
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    def product_display(self, obj):
        """
        Возвращает название продукта, связанного с объектом корзины.

        Args:
            obj (Cart): Объект корзины.

        Returns:
            str: Название продукта.
        """
        return str(obj.product.name)

    # Установка пользовательских заголовков для колонок в административной панели
    user_display.short_description = "Пользователь"
    product_display.short_description = "Товар"

