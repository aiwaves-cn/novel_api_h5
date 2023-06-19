import mongoengine


class Access_token_pool(mongoengine.Document):
    access_token = mongoengine.StringField()
    now_time = mongoengine.StringField()


class User(mongoengine.Document):
    id = mongoengine.StringField(max_length=100)
