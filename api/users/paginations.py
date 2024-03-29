from rest_framework.pagination import PageNumberPagination


class UserPagination(PageNumberPagination):
    page_size = 12
    page_query_param = "page_size"
    max_page_size = 1000
