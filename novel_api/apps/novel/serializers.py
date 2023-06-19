from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Novel, NovelDesc


class NovelSerializer(DocumentSerializer):  # 用于配合子序列化
    class Meta:
        model = Novel
        fields = ["novel_id", "novel_title", "novel_image", "novel_tag", "novel_visit"]


class NovelDescSerializer(DocumentSerializer):
    class Meta:
        model = NovelDesc
        fields = ["novel_id", "novel_title", "novel_image", "novel_visit", "novel_tag", "background", "relationship",
                  "characters", "character", "question", "choice", "summary", "content"]



