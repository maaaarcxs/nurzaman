from rest_framework import serializers
from main.models import Apartment, Block, Object


# class ApartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Apartment
#         fields = ('id', 'number', 'floor', 'area', 'rooms_count', 'image')


class ObjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    address = serializers.CharField()
    image = serializers.ImageField(required=False, allow_null = True)

    def create(self, validated_data):
        return Object.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.address = validated_data.get("address", instance.address)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance
    

class ObjectListSerializer(serializers.Serializer):
    class Meta:
        model = Object 
        fields = {"id", "name", "image"}


class ObjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = "__all__"


class BlockSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    object = serializers.PrimaryKeyRelatedField(queryset=Object.objects.all())
    floors_count = serializers.IntegerField()

    def validate(self, attrs):
        print(attrs.get("name"))
        print(attrs)
        if attrs.get("floors_count") >= 70:
            raise serializers.ValidationError("Слишком много этажей")
        return super().validate(attrs)

    def create(self, validated_data):
        return Block.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.floors_count = validated_data.get("floors_count", instance.floors_count)
        instance.save()
        return instance
    

class BlockListSerializer(serializers.Serializer):
    object = ObjectSerializer(many=False)

    class Meta:
        model = Block
        fields = {"id", "name",}


class BlockDetailSerializer(serializers.ModelSerializer):
    object_name = serializers.CharField(source="object.name")
    object_id = serializers.IntegerField(source="object.id")

    class Meta:
        model = Block
        fields = "__all__"


class ApartmentListSerializer(serializers.Serializer):
    block = BlockSerializer(many=False)

    class Meta:
        model = Apartment
        fields = {"id", "number", "floor", "area", "image", "rooms_count", "block"}


class ApartmentDetailSerializer(serializers.ModelSerializer):
    block_name = serializers.CharField(source='block.name', read_only=True)
    block_id = serializers.IntegerField(source='block.id', read_only=True)
    object_name = serializers.CharField(source='object.name', read_only=True)

    class Meta:
        model = Apartment
        fields = '__all__'

    
class ApartmentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField()
    floor = serializers.IntegerField()
    area = serializers.FloatField()
    rooms_count = serializers.IntegerField()
    image = serializers.ImageField(required=False, allow_null=True)
    block = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all())

    def validate(self, attrs):
        print(attrs.get("number"))
        print(attrs)
        if attrs.get("area") >= 500:
            raise serializers.ValidationError("Слишком большая площадь квартиры")
        return super().validate(attrs)

    def create(self, validated_data):
        return Apartment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.number = validated_data.get("number", instance.number)
        instance.floor = validated_data.get("floor", instance.floor)
        instance.area = validated_data.get("area", instance.area)
        instance.rooms_count = validated_data.get("rooms_count", instance.rooms_count)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance