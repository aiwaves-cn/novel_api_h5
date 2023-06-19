import mongoengine


class Access_token_pool(mongoengine.Document):
    access_token = mongoengine.StringField()
    now_time = mongoengine.StringField()


class User(mongoengine.Document):
    id = mongoengine.StringField(max_length=100)


class Novel(mongoengine.Document):
    novel_id = mongoengine.SequenceField(primary_key=True)
    novel_title = mongoengine.StringField()
    novel_image = mongoengine.StringField()
    novel_tag = mongoengine.ListField()
    novel_visit = mongoengine.StringField()


class NovelDesc(mongoengine.Document):
    novel_desc_id = mongoengine.SequenceField(primary_key=True)
    novel_id = mongoengine.IntField()
    novel_title = mongoengine.StringField()
    novel_image = mongoengine.StringField()
    novel_visit = mongoengine.StringField()
    novel_tag = mongoengine.ListField()
    background = mongoengine.StringField()
    relationship = mongoengine.StringField()
    characters = mongoengine.ListField()
    character = mongoengine.StringField()
    question = mongoengine.StringField()
    choice = mongoengine.ListField()
    summary = mongoengine.StringField()
    content = mongoengine.StringField()


"""
{
    "novel_id": 1,
    "novel_title": "我对总裁大人有偏见",
    "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
    "novel_visit": "10.0万",
    "novel_tag": [
        "言情"
    ],
    "background": "现代言情，一个骄傲善良的女生遇到了一个冷酷理智的男性，彼此两人性格不和，产生了诸多误解和偏见，开始了一段相互嘲笑和争执的关系……",
    "relationship": "乔琳：女主角，获奖的新锐设计师，感情细腻，为人善良，非常感性，比较讨厌功利主义的人。说话时多用网络流行语和颜文字，喜好打抱不平，对自己的作品很自信有些小骄傲。\n\n顾清：男主角，是一个自信且有野心的人，他习惯掌控一切，目标导向且工作狂。刚好是女主角讨厌的那种功利至上的人，他具有领导才能和决断力，但在外表之下隐藏着对自己能力的怀疑和渴望被认可的渴望。说话方式：没有一句废话，不喜欢说场面话，总是简明扼要的说出自己的需求和批评其他人。\n\n慕蓉蓉：女配角，顾清的青梅竹马，喜欢迎合顾清，对于自己的性格宁可压抑住，所以当顾清选择乔琳时，她非常愤怒，会做出伤害乔琳的举动。说话方式非常温婉，温柔，淑女，不会说很俏皮的话，经常保持自己的端庄大方的人设。不会直接给对方难堪，说话有点拐弯抹角。\n\n云哲：女主角的学长，也是顾清的朋友，心里一直对慕蓉蓉有好感，为人温和，内敛。善于理解他人和倾听。为人善良，有正确的价值观，在慕蓉蓉要求他帮助自己陷害乔琳时十分严肃的拒绝了慕蓉蓉。说话方式：能直接提出自己的需求，但是不能很直接的批评其他人。除非是非常严重的事情，不然不会很直接的批评一个人。",
    "characters": [
        "乔琳",
        "顾清",
        "慕蓉蓉",
        "云哲"
    ],
    "character": "乔琳",
    "question": "你对顾清的看法是：",
    "choice": [
        "A、太咄咄逼人了，有点得理不饶人（讨厌）",
        "B、对于做错事的人就该不留情面（欣赏）",
        "C、没有什么看法（无所谓）"
    ],
    "summary": "你被自己的云哲学长邀请参加了一个小型聚会，在宴会上遇到了顾清。一个服务生不小心撞到了顾清，弄脏了顾清的衣服。顾清很冷酷的批评了这个服务生。",
    "content": "我刚一进入宴会厅，就注意到了那个人，如果要我来形容他的气质，我只能蹦出一句话——确认过眼神，是我见过最帅的人。就在我还在欣赏帅哥美貌，纠结要不要去搭讪的时候。\n突然出现了一个小小的插曲，一个笨拙的服务生被另一位小姐碰了一下，我看到他托盘上的红酒在空中画出了一个完美的弧线最后落在了帅哥的西服上。\n这时候上去搭讪会很奇怪吧？我正这样想着，就听到了一个冷冷清清犹如四月海水的声音。\n“你弄脏了我的衣服。”\n“这么简单的工作你居然也能出错？”\n       那个人眉宇之间闪过一丝不悦，他的眼神严厉的像冰川。\n      “对不起，对不起，先生，我马上帮你擦干净。”\n      “别碰我。”他的声音中充满了不容置疑的权威。\n     我看着那个人心中不由得腾出了一种想法\n……"
    }
"""
