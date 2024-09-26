from rest_framework import serializers
from ..models import Watchlist,StreamPlatform,Reviews



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    Reviews = ReviewSerializer(many=True,read_only = True)

    class Meta:
        model = Watchlist 
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True,read_only=True)
    watchlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"  



# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = '__all__' 
#             # object level validation
    
#     def get_len_name(self, object):
#         return len(object.name) 

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError({'name':'name and description cannot be same'})
#         return data
    
#     # field level validation
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name must be at least 2 characters long")
#         else:
#             return value




# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name must be at least 2 characters long.')
#     return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(seld,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     # object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError({'name':'name and description cannot be same'})
#         return data
    
#     # field level validation
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name must be at least 2 characters long")
#         else:
#             return value


