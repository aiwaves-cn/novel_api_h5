from django.http import StreamingHttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from revChatGPT.V1 import Chatbot
from .prompt import *
from utils.common_response import APIResponse


class NovelApiView(ViewSet, ListModelMixin, RetrieveModelMixin):
    # 获取所有小说接口
    def list(self, request, *args, **kwargs):
        data_list = []
        data1 = {
            "novel_id": 1,
            "novel_title": "我对总裁大人有偏见",
            "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
            "novel_tag": ["言情"],
            "novel_visit": '10.0万',
        }
        data2 = {
            "novel_id": 2,
            "novel_title": "出逃m78",
            "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
            "novel_tag": ["悬疑", "科幻"],
            "novel_visit": '10.0万',
        }
        data3 = {
            "novel_id": 3,
            "novel_title": "你是谁",
            "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
            "novel_tag": ["悬疑", "复古"],
            "novel_visit": '10.0万',
        }
        data_list.extend([data1, data2, data3])
        return APIResponse(data=data_list)

    # 获取单个小说详情接口
    def retrieve(self, request, *args, **kwargs):
        novel_id = kwargs.get('pk', '')
        data = {
            '1': {
                # 书籍表
                "novel_id": 1,
                "novel_title": "我对总裁大人有偏见",
                "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
                "novel_visit": '10.0万',

                # 书籍标签表
                "novel_tag": ["言情"],

                # 预设表
                "background": "现代言情，一个骄傲善良的女生遇到了一个冷酷理智的男性，彼此两人性格不和，产生了诸多误解和偏见，开始了一段相互嘲笑和争执的关系……",
                "relationship": """乔琳：女主角，获奖的新锐设计师，感情细腻，为人善良，非常感性，比较讨厌功利主义的人。说话时多用网络流行语和颜文字，喜好打抱不平，对自己的作品很自信有些小骄傲。

顾清：男主角，是一个自信且有野心的人，他习惯掌控一切，目标导向且工作狂。刚好是女主角讨厌的那种功利至上的人，他具有领导才能和决断力，但在外表之下隐藏着对自己能力的怀疑和渴望被认可的渴望。说话方式：没有一句废话，不喜欢说场面话，总是简明扼要的说出自己的需求和批评其他人。

慕蓉蓉：女配角，顾清的青梅竹马，喜欢迎合顾清，对于自己的性格宁可压抑住，所以当顾清选择乔琳时，她非常愤怒，会做出伤害乔琳的举动。说话方式非常温婉，温柔，淑女，不会说很俏皮的话，经常保持自己的端庄大方的人设。不会直接给对方难堪，说话有点拐弯抹角。

云哲：女主角的学长，也是顾清的朋友，心里一直对慕蓉蓉有好感，为人温和，内敛。善于理解他人和倾听。为人善良，有正确的价值观，在慕蓉蓉要求他帮助自己陷害乔琳时十分严肃的拒绝了慕蓉蓉。说话方式：能直接提出自己的需求，但是不能很直接的批评其他人。除非是非常严重的事情，不然不会很直接的批评一个人。""",
                "characters": ['乔琳', '顾清', '慕蓉蓉', '云哲'],
                "character": '乔琳',
                "question": """你对顾清的看法是：""",
                "choice": ["A、太咄咄逼人了，有点得理不饶人（讨厌）", "B、对于做错事的人就该不留情面（欣赏）", "C、没有什么看法（无所谓）"],
                "summary": "你被自己的云哲学长邀请参加了一个小型聚会，在宴会上遇到了顾清。一个服务生不小心撞到了顾清，弄脏了顾清的衣服。顾清很冷酷的批评了这个服务生。",
                "content": """我刚一进入宴会厅，就注意到了那个人，如果要我来形容他的气质，我只能蹦出一句话——确认过眼神，是我见过最帅的人。就在我还在欣赏帅哥美貌，纠结要不要去搭讪的时候。
突然出现了一个小小的插曲，一个笨拙的服务生被另一位小姐碰了一下，我看到他托盘上的红酒在空中画出了一个完美的弧线最后落在了帅哥的西服上。
这时候上去搭讪会很奇怪吧？我正这样想着，就听到了一个冷冷清清犹如四月海水的声音。
“你弄脏了我的衣服。”
“这么简单的工作你居然也能出错？”
       那个人眉宇之间闪过一丝不悦，他的眼神严厉的像冰川。
      “对不起，对不起，先生，我马上帮你擦干净。”
      “别碰我。”他的声音中充满了不容置疑的权威。
     我看着那个人心中不由得腾出了一种想法
……""",
            },
            '2': {
                # 书籍表
                "novel_id": 2,
                "novel_title": "出逃m78",
                "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
                "novel_visit": '10.0万',

                # 书籍标签表
                "novel_tag": ["悬疑", "科幻"],

                # 预设表
                "background": default_background_2,
                "relationship": default_relationship_2,
                "characters": ['艾丽', '张强', '毛毛', '杨教授'],
                "character": default_character_2,
                "question": init_question_2,
                "choice": [init_choice_2_1, init_choice_2_2, init_choice_2_3],
                "summary": init_summary_2,
                "content": init_content_2,
            },
            '3': {
                # 书籍表
                "novel_id": 3,
                "novel_title": "你是谁",
                "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
                "novel_visit": '10.0万',

                # 书籍标签表
                "novel_tag": ["悬疑", "复古"],

                # 预设表
                "background": default_background_3,
                "relationship": default_relationship_3,
                "characters": ['赵磊', '赵国平', '老马', '马艳梅'],
                "character": default_character_3,
                "question": init_question_3,
                "choice": [init_choice_3_1, init_choice_3_2, init_choice_3_3],
                "summary": init_summary_3,
                "content": init_content_3,
            },
        }
        # data = {
        #     '1': {
        #         # 书籍表
        #         "novel_id": 1,
        #         "novel_title": "夏烟之约",
        #         "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
        #         "novel_visit": '10.0万',

        #         # 书籍标签表
        #         "novel_tag": ["悬疑", "恐怖", "爱情"],

        #         # 预设表
        #         "background": default_background_1,
        #         "relationship": default_relationship_1,
        #         "characters": ['林月', '简伊', '张强', '陈琳'],
        #         "character": default_character_1,
        #         "question": init_question_1,
        #         "choice": [init_choice_1_1, init_choice_1_2, init_choice_1_3],
        #         "summary": init_summary_1,
        #         "content": init_content_1,
        #     },
        #     '2': {
        #         # 书籍表
        #         "novel_id": 2,
        #         "novel_title": "出逃m78",
        #         "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
        #         "novel_visit": '10.0万',

        #         # 书籍标签表
        #         "novel_tag": ["悬疑", "科幻"],

        #         # 预设表
        #         "background": default_background_2,
        #         "relationship": default_relationship_2,
        #         "characters": ['艾丽', '张强', '毛毛', '杨教授'],
        #         "character": default_character_2,
        #         "question": init_question_2,
        #         "choice": [init_choice_2_1, init_choice_2_2, init_choice_2_3],
        #         "summary": init_summary_2,
        #         "content": init_content_2,
        #     },
        #     '3': {
        #         # 书籍表
        #         "novel_id": 3,
        #         "novel_title": "你是谁",
        #         "novel_image": "https://cn.bing.com/images/search?view=detailV2&ccid=Bq5jD730&id=E91F2971887D91E927CE16AB8F45BEB8C1185543&thid=OIP.Bq5jD730RoSsMF3c1yWIWwHaJ4&mediaurl=https%3A%2F%2Fstatic.zongheng.com%2Fupload%2Fcover%2Fshucheng%2F16%2F15416195.jpg&exph=3200&expw=2400&q=%e5%b0%8f%e8%af%b4%e5%9b%be%e7%89%87&simid=608000767812436123&form=IRPRST&ck=ADD7A0A91334D779ECBD217BF7F86F67&selectedindex=2&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
        #         "novel_visit": '10.0万',

        #         # 书籍标签表
        #         "novel_tag": ["悬疑", "复古"],

        #         # 预设表
        #         "background": default_background_3,
        #         "relationship": default_relationship_3,
        #         "characters": ['赵磊', '赵国平', '老马', '马艳梅'],
        #         "character": default_character_3,
        #         "question": init_question_3,
        #         "choice": [init_choice_3_1, init_choice_3_2, init_choice_3_3],
        #         "summary": init_summary_3,
        #         "content": init_content_3,
        #     },
        # }
        if not novel_id:
            return APIResponse(msg='没有该书籍')
        # 通过id从数据库中查出书籍详情
        novel_data = data.get(novel_id, '')
        if novel_data:
            return APIResponse(data=novel_data)
        else:
            return APIResponse(code=1001, msg='没有该书籍')
