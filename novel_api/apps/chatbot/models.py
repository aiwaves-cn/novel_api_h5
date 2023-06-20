import mongoengine
import datetime


class Memory(mongoengine.Document):
    novel = mongoengine.StringField(max_length=32)
    Memory = mongoengine.ListField()  # 文章的memory


class Access_token_pool(mongoengine.Document):
    access_token = mongoengine.StringField()
    now_time = mongoengine.DateTimeField()

    @classmethod
    def get_oldest_token(cls):
        current_time = datetime.datetime.now()
        oldest_token = cls.objects.order_by('now_time').first()  # 取不到token则为None
        if oldest_token:
            oldest_token.now_time = current_time
            oldest_token.save()
            return oldest_token  # 如果不存在会为None


class Paragraph(mongoengine.Document):
    text = mongoengine.ListField()


class Choice(mongoengine.Document):
    text = mongoengine.ListField()


