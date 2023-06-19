import mongoengine


class Memory(mongoengine.Document):
    novel = mongoengine.StringField(max_length=32)
    Memory = mongoengine.ListField()  # 文章的memory


class Access_token_pool(mongoengine.Document):
    access_token = mongoengine.StringField()
    now_time = mongoengine.StringField()


class User(mongoengine.Document):
    id = mongoengine.StringField(max_length=100)

class Paragraph(mongoengine.Document):
    text = mongoengine.ListField()


class Choice(mongoengine.Document):
    text = mongoengine.ListField()