import mongoengine


class User(mongoengine.Document):
    id = mongoengine.SequenceField(primary_key=True)
    username = mongoengine.StringField(max_length=30)
    password = mongoengine.StringField(max_length=30)
    my_collect = mongoengine.StringField()
    position = mongoengine.ListField()
