from django.db import models

# Create your models here.


class Brand(models.Model):
    """Create Brand to use in processors and motherboard"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Processor(models.Model):
    """Create processor to be used in orders"""
    name = models.CharField(max_length=255)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Motherboard(models.Model):
    """Create motherboard to be used in orders"""
    name = models.CharField(max_length=255)
    processor_suported = models.ForeignKey('Brand', on_delete=models.CASCADE)
    ram_slots = models.IntegerField()
    max_ram = models.IntegerField()
    integrated_video = models.BooleanField()

    def __str__(self):
        return self.name


class Memory(models.Model):
    """Create memory to be used in orders"""
    name = models.CharField(max_length=255)
    size = models.IntegerField()

    def __str__(self):
        return self.name


class GraphicCard(models.Model):
    """Create Graphic Card to be used in orders"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Create order based on components to be used in orders"""
    client = models.CharField(max_length=255)
    processor = models.ForeignKey('Processor', on_delete=models.CASCADE)
    processor_name = models.CharField(max_length=255, blank=True, null=True)
    motherboard = models.ForeignKey('Motherboard', on_delete=models.CASCADE)
    motherboard_name = models.CharField(max_length=255, blank=True, null=True)
    memory1 = models.ForeignKey('Memory',
                                related_name='memory_slot_1',
                                on_delete=models.CASCADE)
    memory1_name = models.CharField(max_length=255, blank=True, null=True)
    memory2 = models.ForeignKey('Memory',
                                related_name='memory_slot_2',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    memory2_name = models.CharField(max_length=255, blank=True, null=True)
    memory3 = models.ForeignKey('Memory',
                                related_name='memory_slot_3',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    memory3_name = models.CharField(max_length=255, blank=True, null=True)
    memory4 = models.ForeignKey('Memory',
                                related_name='memory_slot_4',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    memory4_name = models.CharField(max_length=255, blank=True, null=True)
    graphic_card = models.ForeignKey('GraphicCard',
                                     on_delete=models.CASCADE,
                                     blank=True,
                                     null=True)
    graphic_card_name = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.processor_name = self.processor.name
        self.motherboard_name = self.motherboard.name
        self.memory1_name = self.memory1.name
        try:
            self.memory2_name = self.memory2.name
        except Exception:
            pass
        try:
            self.memory3_name = self.memory3.name
        except Exception:
            pass
        try:
            self.memory4_name = self.memory4.name
        except Exception:
            pass
        try:
            self.graphic_card_name = self.graphic_card.name
        except Exception:
            pass
        super(Order, self).save()

    def __str__(self):
        return 'Pedido: {}'.format(self.id)
