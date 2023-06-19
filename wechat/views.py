from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

class WechatView(ViewSet):
    @action(methods=['post'], detail=False)
    def get_response(self, *args, **kwargs):
        return Response(data=123)
