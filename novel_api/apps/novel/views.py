from rest_framework.viewsets import ViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from utils.common_response import APIResponse
from .models import Novel, NovelDesc
from .serializers import NovelSerializer, NovelDescSerializer
from rest_framework.decorators import action


class NovelApiView(ViewSet, ListModelMixin, RetrieveModelMixin):
    # 获取所有小说接口
    def list(self, request, *args, **kwargs):
        novel_list = Novel.objects.all()
        ser_obj = NovelSerializer(novel_list, many=True)
        return APIResponse(data=ser_obj.data)

    # 获取单个小说详情接口
    def retrieve(self, request, *args, **kwargs):
        novel_id = kwargs.get('pk', '')
        if not novel_id:
            return APIResponse(msg='没有该书籍')
        # 通过id从数据库中查出书籍详情
        novel_desc_obj = NovelDesc.objects(novel_id=novel_id).first()
        if novel_desc_obj:
            ser_obj = NovelDescSerializer(novel_desc_obj)
            return APIResponse(data=ser_obj.data)
        else:
            return APIResponse(code=1001, msg='没有该书籍')

    # 新增一个小说的接口
    def create(self, request, *args, **kwargs):
        novel_title = request.data.get('novel_title')
        novel_image = request.data.get('novel_image')
        novel_tag = request.data.get('novel_tag')
        novel_visit = request.data.get('novel_visit')
        novel_obj = Novel(novel_title=novel_title, novel_image=novel_image, novel_tag=novel_tag,
                          novel_visit=novel_visit)
        ser_obj = NovelSerializer(novel_obj)
        return APIResponse(data=ser_obj.data)

    # 新增一个小说详情
    @action(methods=['POST'], detail=False)
    def create_novel_desc(self, request, *args, **kwargs):
        novel_obj = NovelDesc(**request.data)
        novel_obj.save()
        ser_obj = NovelDescSerializer(novel_obj)
        return APIResponse(data=ser_obj.data)
