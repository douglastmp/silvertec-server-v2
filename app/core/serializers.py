from core import models
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order object"""

    class Meta:
        model = models.Order
        fields = (
            'id',
            'client',
            'processor',
            'processor_name',
            'motherboard',
            'motherboard_name',
            'memory1',
            'memory1_name',
            'memory2',
            'memory2_name',
            'memory3',
            'memory3_name',
            'memory4',
            'memory4_name',
            'graphic_card',
            'graphic_card_name',
        )


class ProcessorSerializer(serializers.ModelSerializer):
    """Serializer for Processor object"""

    class Meta:
        model = models.Processor
        fields = (
            'id',
            'name',
            'brand',
            )


class MotherboardSerializer(serializers.ModelSerializer):
    """Serializer for Motherboard object"""

    class Meta:
        model = models.Motherboard
        fields = (
            'id',
            'name',
            'processor_suported',
            'ram_slots',
            'max_ram',
            'integrated_video',
            )


class MemorySerializer(serializers.ModelSerializer):
    """Serializer for Memory object"""

    class Meta:
        model = models.Memory
        fields = (
            'id',
            'name',
            'size',
            )


class GraphicCardSerializer(serializers.ModelSerializer):
    """Serializer for Graphi Card object"""

    class Meta:
        model = models.Motherboard
        fields = (
            'id',
            'name',
            )


class BrandSerializer(serializers.ModelSerializer):
    """Serializer for Brands object"""

    class Meta:
        model = models.Brand
        fields = (
            'id',
            'name',
            )
