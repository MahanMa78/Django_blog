from rest_framework import serializers

class SinglePostSerializers(serializers.Serializer):
    title = serializers.CharField(required = True , allow_null = False , allow_blank = False , max_length = 128 )
    photo = serializers.ImageField(required = True ,   allow_null = False , allow_empty_file = False )
    body = serializers.CharField(required = True , allow_null = False , allow_blank = False , max_length = 2048 )
    date = serializers.DateField(required = True , allow_null = False)

    