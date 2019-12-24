from django.test import TestCase
from core.models import Order, GraphicCard, Processor
from core.models import Memory, Brand, Motherboard
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from core.serializers import OrderSerializer
from core.serializers import ProcessorSerializer, MemorySerializer
from core.serializers import GraphicCardSerializer, MotherboardSerializer

ORDER_URL = reverse('core:order-list')
PROCESSOR_URL = reverse('core:processor-list')
MOTHERBOARD_URL = reverse('core:motherboard-list')
MEMORY_URL = reverse('core:memory-list')
GRAPHIC_CARD_URL = reverse('core:graphiccard-list')


class PublicOrderApiTests(TestCase):
    """Test order API public"""

    def setUp(self):
        self.client = APIClient()
        self.brand = Brand.objects.create(name="Intel")      

    def test_processor_list(self):
        """Test getting a list of processors"""
        res = self.client.get(PROCESSOR_URL)

        processors = Processor.objects.all()
        serializer = ProcessorSerializer(processors, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_motherboard_list(self):
        """Test getting a list of motherboards"""
        res = self.client.get(MOTHERBOARD_URL)

        motherboards = Motherboard.objects.all()
        serializer = MotherboardSerializer(motherboards, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_memory_list(self):
        """Test getting a list of memories"""
        res = self.client.get(MEMORY_URL)

        memories = Memory.objects.all()
        serializer = MemorySerializer(memories, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_graphic_card_list(self):
        """Test getting a list of graphic cards"""
        res = self.client.get(GRAPHIC_CARD_URL)

        graphic_cards = GraphicCard.objects.all()
        serializer = GraphicCardSerializer(graphic_cards, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_order_list(self):
        """Test getting a list of orders"""
        res = self.client.get(ORDER_URL)

        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
