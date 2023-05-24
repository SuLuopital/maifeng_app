#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from rest_framework import mixins
from rest_framework import serializers
from rest_framework.serializers import *

import os
import sys
from PIL import Image

from .models import *



class ImagesSerializer(serializers.ModelSerializer):
    url = serializers.ImageField(source='img', read_only=True)
    img_url = serializers.ImageField(source='img', read_only=True)
    created_by_name = serializers.CharField(source='created_by.realname', read_only=True)
    created_date = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S')
    last_edited_by_name = serializers.CharField(source='last_edited_by.realname', read_only=True)
    last_edited_date = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Images
        fields = "__all__"
    # def create(self, validated_data):
    #     '''序列化器重写创建实例'''
    #     newImages = Images()
    #     # 传入参数
    #     if 'with_models' in validated_data:
    #         newImages.with_models = validated_data["with_models"]
    #     if 'models_id' in validated_data:
    #         newImages.models_id = validated_data["models_id"]
    #     newImages.created_by = self.context['request'].user.extension
    #     newImages.last_edited_by = self.context['request'].user.extension
    #     picture = validated_data["img"]
    #     newImages.img = picture
    #     newImages.save()
    #     img = Image.open(os.path.dirname(__file__) +
    #                      '/../../media/' + str(newImages.img))
    #     if 'height' in validated_data:
    #         # print(validated_data['height'])
    #         x = img.height / int(validated_data['height'])
    #         w = int(img.width / x)
    #         new_img = img.resize((w, int(validated_data['height'])), Image.ANTIALIAS)
    #         new_img.save(os.path.dirname(__file__) +
    #                     '/../../media/' + str(newImages.img), quality = 95)
        
    #     # if img.height >= 240:
    #     #     x = img.height / 240
    #     #     w = int(img.width / x)
    #     #     new_img = img.resize((w, 240), Image.ANTIALIAS)
    #     #     new_img.save(os.path.dirname(__file__) +
    #     #                 '/../../media/' + str(newImages.img), quality = 95)
    #     else:
    #         pass
    #     return newImages
    
#first
class ImagesOptionSerializer(serializers.ModelSerializer):

    value = serializers.IntegerField(source='id')
    # label = serializers.CharField(source='name')

    class Meta:
        model = Images
        fields = ['value']
    
#first
class FilesSerializer(serializers.ModelSerializer):

    created_by_name = serializers.CharField(source='created_by.realname', read_only=True)
    created_date = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S')
    last_edited_by_name = serializers.CharField(source='last_edited_by.realname', read_only=True)
    last_edited_date = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Files
        fields = "__all__"
    
#first
class FilesOptionSerializer(serializers.ModelSerializer):

    value = serializers.IntegerField(source='id')
    # label = serializers.CharField(source='name')

    class Meta:
        model = Files
        fields = ['value',]
    