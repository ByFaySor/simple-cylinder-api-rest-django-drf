from inventory.common.models import (
    TpsCylinder,
    DtsCylinder,
    DtsPerson,
    DtsCylinderPerson,
)
from inventory.common.serializers import (
    TpsCylinderSerializer,
    DtsCylinderSerializer,
    DtsPersonSerializer,
    DtsCylinderPersonSerializer,
)
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class TpsCylinderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = TpsCylinder.objects.all()
    serializer_class = TpsCylinderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('name',)
    search_fields = ('name',)
    ordering_fields = '__all__'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        fields_common = ('name',)
        
        if (action == 'list'):
            context['fields'] = ('id',) + fields_common
        elif (action == 'retrieve'):
            context['fields'] = fields_common
        elif (action == 'create'):
            context['fields'] = ('id',) + fields_common
        elif (action == 'update'):
            context['fields'] = fields_common
        elif (action == 'partial_update'):
            context['fields'] = fields_common
        return context

    def perform_create(self, serializer):
        serializer.save(dts_user=self.request.user)


class DtsCylinderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = DtsCylinder.objects.all()
    serializer_class = DtsCylinderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ('size', 'weight', 'price',)
    ordering_fields = '__all__'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        fields_common = ('size', 'weight', 'price', 'tps_cylinder',)
        
        if (action == 'list'):
            context['fields'] = ('id',) + fields_common
        elif (action == 'retrieve'):
            context['fields'] = fields_common
        elif (action == 'create'):
            context['fields'] = ('id',) + fields_common
        elif (action == 'update'):
            context['fields'] = fields_common
        elif (action == 'partial_update'):
            context['fields'] = fields_common
        return context

    def perform_create(self, serializer):
        serializer.save(dts_user=self.request.user)


class DtsPersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = DtsPerson.objects.all()
    serializer_class = DtsPersonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ('dni', 'first_name', 'surname', 'sex',)
    ordering_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(dts_user=self.request.user)


class DtsCylinderPersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = DtsCylinderPerson.objects.all()
    serializer_class = DtsCylinderPersonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ('dts_cylinder', 'dts_person',)
    ordering_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(dts_user=self.request.user)