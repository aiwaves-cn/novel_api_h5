from mongoengine import connect
from urllib.parse import quote_plus

connect('dev_test', host="mongodb://%s:%s@%s" % (quote_plus("aiwaves"), quote_plus("bxzn2023"), "47.96.122.196"))

question_1 = """
问题：你对顾清的看法是：
选项一：太咄咄逼人了，有点得理不饶人，去阻止顾清
选项二：对于做错事的人就该不留情面
选项三：没有什么看法
"""
question_2 = """
问题：此时：你对于顾清的顾虑是：
选项一：这么大公司的总裁应该是公私分明吧
选项二：这个人不好相处，日子怕是难过咯
选项三：管他呢，自己做好自己的事情就行
"""
question_3 = """
问题：此时你会怎么做：
选项一：你主动要求查看监控录像，以证清白
选项二：你直接要求顾清开除副总监
选项三：你当众宣布要与副总监展开一场设计能力的较量，少用下三滥的手段污蔑人。
"""
question_4 = """
问题：你此时对顾清感觉是……
选项一：有点喜欢
选项二：很喜欢
选项三：没感觉，甚至有点讨厌
"""
question_5 = """
问题：这时你会？
选项一：慌忙走开
选项二：偷偷听发生了什么
选项三：冲上去打一顿顾清
"""
question_6 = """
问题：你不打算什么都不做于是你决定……
选项一：去找顾清说清楚
选项二：去找云哲说说自己的想法
选项三：去找慕蓉蓉
"""
question_7 = """
问题：离开时，你会对慕蓉蓉说：
选项一：我并不知道顾清有未婚妻
选项二：祝你们幸福
选项三：什么都不说
"""
question_8 = """
问题：你决定……
选项一：有未婚妻还来撩人的渣男，不接
选项二：打了这么多个，还是接吧
选项三：直接去找顾清当面说清楚
"""
question_9 = """
问题：你得知了真相之后会接受顾清表白吗？
选项一：表示要考虑一下（你有点心动，顾清也看出了你的想法）
选项二：接受，并亲吻（你和顾清在一起了）
选项三：拒绝（顾清还是希望你能保留他追求你的机会，不要彻底从他的人生中消失）
"""
question_10 = """
问题：你会怎么做：
选项一：坏女人，我要离你远一点（攻击你）
选项二：祝福对方（慕蓉蓉祝福了你）
选项三：询问对方是一个人旅游吗？（慕蓉蓉告诉你她是和云哲学长一起出来的）
"""
paragraph_list = [question_1, question_2, question_3, question_4, question_5, question_6, question_7,
                  question_8, question_9, question_10]

import mongoengine


class Choice(mongoengine.Document):
    text = mongoengine.ListField()


# obj = Choice(text=paragraph_list)
# obj.save()


