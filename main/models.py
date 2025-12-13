from django.db import models
from django_resized import ResizedImageField


class Object(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название объекта")
    address = models.CharField(max_length=255, verbose_name="Адрес объекта")
    image = ResizedImageField(size=[800, 600], upload_to="objects/", verbose_name="Фото объекта",
                              null=True, blank=True, quality=90, crop=['middle', 'center'])
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class ObjectImage(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name="images")
    image = ResizedImageField(size=[800, 600], upload_to='objects/', verbose_name="Изображение объекта", quality=90, crop=['middle', 'center'])

    class Meta:
        verbose_name = "Изображение объекта"
        verbose_name_plural = "Изображеия объекта"

    def __str__(self):
        return f"Изображение объекта '{self.object.name}'"


class Block(models.Model):
    BLOCK_TYPES = (
        ("Elite", "Элитный"),
        ("Brick-made", "Кирпичный"),
        ("Skyscraper", "Небоскрёб"),
        ("Khrushchev-era", "Хрущёвка"),
        ("Standard", "Стандартный")
    )
    name = models.CharField()
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    floors_count = models.IntegerField(verbose_name="Количество этажей")
    type = models.CharField(max_length=20, choices=BLOCK_TYPES, verbose_name="Тип блока")

    def __str__(self):
        return f"{self.type} блок {self.name} объекта {self.object}"
    
    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'


class Apartment(models.Model):
    APARTMENT_TYPES = (
    ("Studio", "Студия"),
    ("Standard", "Стандартная"),
    ("Commercial", "Коммерческая"),
    ("Penthouse", "Пентхаус"),
    )
    number= models.IntegerField(verbose_name="номер квартиры")
    floor = models.IntegerField(verbose_name="Этаж")
    rooms_count = models.IntegerField(verbose_name="Количество комнат")
    area = models.FloatField(verbose_name="Площадь в квадратных метрах")
    image = ResizedImageField(size=[800, 600], upload_to='apartments/', verbose_name="Изображение квартиры",
                              blank=True, null=True, quality=90, crop=['middle', 'center'])
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="apartments", verbose_name="Блок", null=True, blank=True)
    type = models.CharField(max_length=20, choices=APARTMENT_TYPES, verbose_name="Тип квартиры")
    
    def __str__(self):
        return f"Квартира {self.number} на {self.rooms_count} комнат на {self.floor} этаже"
    
    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"