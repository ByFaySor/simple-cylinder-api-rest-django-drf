from rest_framework import serializers
from django.contrib.auth.models import User
from inventory.common.models import (
    TpsCylinder,
    DtsCylinder,
    DtsPerson,
    DtsCylinderPerson,
)

class DynamicFieldSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        context = kwargs.get('context', None)
        fields = None
        if context:
            fields = context.get('fields')

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

class TpsCylinderSerializer(serializers.ModelSerializer):

    name = serializers.CharField(min_length=10)
    dts_user = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TpsCylinder
        fields = ('id', 'name')
        read_only_fields = ('id', 'created_at', 'updated_at', 'dts_user')

class DtsCylinderSerializer(DynamicFieldSerializer):

    size = serializers.CharField(min_length=10)
    weight = serializers.IntegerField(min_value=10)
    price = serializers.FloatField(min_value=1)
    dts_user = serializers.ReadOnlyField(source='owner.username')
    tps_cylinder = TpsCylinderSerializer()
    dts_user = UserSerializer()

    class Meta:
        model = DtsCylinder
        fields = '__all__'

class DtsPersonSerializer(serializers.ModelSerializer):

    dni = serializers.IntegerField(min_value=5, max_value=100000000) # Expresión regular
    first_name = serializers.CharField(min_length=3)
    surname = serializers.CharField(min_length=3)
    dts_user = serializers.ReadOnlyField(source='owner.username')
    dts_user = UserSerializer()

    class Meta:
        model = DtsPerson
        fields = '__all__'

class DtsCylinderPersonSerializer(serializers.ModelSerializer):

    dts_user = serializers.ReadOnlyField(source='owner.username')
    dts_user = UserSerializer()

    class Meta:
        model = DtsCylinderPerson
        fields = '__all__'
        depth = 1