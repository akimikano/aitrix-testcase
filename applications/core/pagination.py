from rest_framework.pagination import PageNumberPagination, BasePagination
from rest_framework.response import Response
from collections import OrderedDict


class MainPagination(PageNumberPagination):
    page_size = 9

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))