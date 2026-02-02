from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class PostSerializer(serializers.ModelSerializer):
    # Relacja do wyświetlania (GET)
    categories = CategorySerializer(many=True, read_only=True)
    # Pole do zapisywania (POST/PUT) używając ID
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        many=True, 
        write_only=True, 
        source='categories'
    )

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'author', 
            'created_at', 'published', 'categories', 'category_ids'
        ]