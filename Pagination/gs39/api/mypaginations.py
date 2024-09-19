from rest_framework.pagination import CursorPagination
# from rest_framework.pagination import LimitOffsetPagination


# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5
#     limit_query_param = 'mylimit'
#     offset_query_param = 'myoffset'
#     max_limit = 6


class MyCursorPagination(CursorPagination):
    page_size = 10
    ordering = 'name'
    cursor_query_param = 'cu'
