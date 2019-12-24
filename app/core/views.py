from rest_framework import viewsets, mixins, status, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core import models, serializers


class OrderViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin):
    """Manage orders in the database"""
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'client', 'processor', 'motherboard']
    search_fields = ['^client',]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        order_processor = models.Processor.objects.get(
            pk=request.data['processor']
            )
        order_motherboard = models.Motherboard.objects.get(
            pk=request.data['motherboard']
            )
        total_memory = 0
        """Validate memories in Motherboard"""
        try:
            order_memory4 = models.Memory.objects.get(
                pk=request.data['memory4']
                )
            if order_motherboard.ram_slots < 4:
                return Response({
                    'error': 'Placa mãe possui somente {} sockets para memória'
                    .format(order_motherboard.ram_slots)
                },
                 status=status.HTTP_400_BAD_REQUEST)
            total_memory += order_memory4.size
        except Exception:
            pass

        try:
            order_memory3 = models.Memory.objects.get(
                pk=request.data['memory3']
                )
            if order_motherboard.ram_slots < 4:
                return Response({
                    'error': 'Placa mãe possui somente {} sockets para memória'
                    .format(order_motherboard.ram_slots)
                },
                 status=status.HTTP_400_BAD_REQUEST)
            total_memory += order_memory3.size
        except Exception:
            pass

        try:
            order_memory2 = models.Memory.objects.get(
                pk=request.data['memory2']
                )
            total_memory += order_memory2.size
        except Exception:
            pass

        order_memory1 = models.Memory.objects.get(
            pk=request.data['memory1']
        )
        total_memory += order_memory1.size
        if total_memory > order_motherboard.max_ram:
            return Response(
                {'error': 'Total de RAM maior que o permitido pela placa mãe'},
                status=status.HTTP_400_BAD_REQUEST)

        """Validate Integrated video in Motherboard"""
        try:
            models.Motherboard.objects.get(pk=request.data['graphic_card'])
        except Exception:
            if (not order_motherboard.integrated_video):
                try:
                    request.data['graphic_card']
                except Exception:
                    pass
                return Response({
                    'error': 'Placa mãe não possui vídeo integrado'
                    },
                    status=status.HTTP_400_BAD_REQUEST)

        """Validate Processor Suporter by the motherboard"""
        if (order_motherboard.processor_suported != order_processor.brand and
                order_motherboard.processor_suported.name != 'Both'):
            return Response(
                {'error': 'Processador incompatível com placa mãe'},
                status=status.HTTP_400_BAD_REQUEST
                )
        """Validate Serializer field's"""
        if (serializer.is_valid() is False):
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class ProcessorViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin):
    """Manage processor in the database"""
    queryset = models.Processor.objects.all()
    serializer_class = serializers.ProcessorSerializer

    def perform_create(self, serializer):
        serializer.save()


class MemoryViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin):
    """Manage memory in the database"""
    queryset = models.Memory.objects.all()
    serializer_class = serializers.MemorySerializer

    def perform_create(self, serializer):
        serializer.save()


class MotherboardViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin):
    """Manage motherboard in the database"""
    queryset = models.Motherboard.objects.all()
    serializer_class = serializers.MotherboardSerializer

    def perform_create(self, serializer):
        serializer.save()


class GraphicCardViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin):
    """Manage GraphicCard in the database"""
    queryset = models.GraphicCard.objects.all()
    serializer_class = serializers.GraphicCardSerializer

    def perform_create(self, serializer):
        serializer.save()


class BrandViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    """Manage GraphicCard in the database"""
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

    def perform_create(self, serializer):
        serializer.save()
