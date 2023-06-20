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
        oldest_token = cls.objects.order_by('now_time').first()  # 未取到不会报错
        if oldest_token:
            oldest_token.now_time = current_time
            oldest_token.save()
            return oldest_token  # 如果不存在会为None


class User(mongoengine.Document):
    id = mongoengine.StringField(max_length=100)


class Paragraph(mongoengine.Document):
    text = mongoengine.ListField()


class Choice(mongoengine.Document):
    text = mongoengine.ListField()

# "novel_id": 1,
# "novel_title": "我对总裁大人有偏见",
# "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
# "novel_tag": ["言情"],
# "novel_visit": '10.0万',
