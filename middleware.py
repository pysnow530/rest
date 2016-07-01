# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import json

from django.core.exceptions import ObjectDoesNotExist

from .models import Profile


class RestMiddleware(object):

    def process_request(self, request):
        """如果http请求头有PRIVATE-TOKEN
        1. 匹配Profile并将赋值request.user
        2. 如果类型为application/json，解析并赋值request.POST或request.PUT
        """
        private_token = request.META.get('HTTP_PRIVATE_TOKEN', None)

        if private_token is None:
            return None

        # 根据PRIVATE-TOKEN加载用户
        try:
            user_info = Profile.objects.get(private_token=private_token)
            request.user = user_info.user
        except ObjectDoesNotExist:
            pass

        # 解析json
        content_type = request.META['CONTENT_TYPE']

        if re.match('application/json', content_type):
            method = request.method
            if method == 'POST':
                request.POST = json.loads(request.body)
            elif method == 'PUT':
                request.PUT = json.loads(request.body)

        return None
