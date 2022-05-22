from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from hashtag_app.api.serializers.tag_post import TagsPostSerializer
from hashtag_app.models import Tags, PostTags


class PaginationTags(LimitOffsetPagination):
    default_limit =2
    offset_query_param = "offset"
    limit_query_param = 'limit'
    max_limit = 10000000


class TagsPostView(APIView):
    def get(self, request, tag):
        tags = Tags.objects.get(tag=tag)
        post = PostTags.objects.filter(tag=tags)
        posts = list()

        for i in post:
            posts.append(i.post)
        pg = PaginationTags()
        page_roles = pg.paginate_queryset(queryset=posts, request=request, view=self)
        serializer = TagsPostSerializer(instance = page_roles, many=True)
        return Response(serializer.data)
