import short_url

from django.conf import settings

from rest_framework import serializers

from core.models import URL


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    access_counter = serializers.IntegerField(read_only=True)

    class Meta:
        model = URL
        fields = "__all__"

    def create(self, validated_data):
        try:
            url = URL.objects.get(full_url=validated_data['full_url'])
        except URL.DoesNotExist:
            counter = len(URL.objects.all())
            slug = short_url.encode_url(counter + 1)
            while URL.objects.filter(slug=slug).exists():
                counter += 1
                slug = short_url.encode_url(counter + 1)
            url = URL(
                slug=slug,
                short_url=f'{settings.BASE_URL}/c/{slug}',
                full_url=validated_data['full_url']
            )
            url.save()
        return url
                