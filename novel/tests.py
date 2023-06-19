import gradio as gr
import os
from revChatGPT.V1 import Chatbot
import re
import pandas as pd
import random
from sentence_transformers import SentenceTransformer
from sentence_transformers import util
import torch  # torch11的库

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
embedder = SentenceTransformer('multi-qa-mpnet-base-cos-v1')
device = torch.device('cpu')
embedder.to(device)
init_content = ""
init_question = ""
init_choice = ""
init_summary = ""
default_background = ""
default_relationship = ""
default_character = ""
long_memory = []
memory_index = None

access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJqaWF0a2IwNjU2QHdlcC5lbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlfSwiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS9hdXRoIjp7InVzZXJfaWQiOiJ1c2VyLWdGV3RRS2QxYkJuWmNsbWgzeXdrNllzSCJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiYXV0aDB8NjQ0YTFiMmUxZGVjOGQyZWRhOGQxZmU0IiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4NjExMDMzNywiZXhwIjoxNjg3MzE5OTM3LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9yZ2FuaXphdGlvbi53cml0ZSJ9.0fI-3RYbF1eg_kRzE3Q3QYNGa6kgOgsaPvt4m9HREjRkYFKWGVP3lBWxGQkG3553imEr2vZjETn4hyHFGj-LLYg1XpLpa-_zvhjITyzzT4flUZijFp6tzZg185WIySeXrmoKmZTxL7ij1LF1Un6Y2IRPSIbvOvugr5wWvrPZtZD0xHcgmzmj-A1xJytjM7zhdlKtaJiK_VyeR6wlTv5fLdjPWxU5nutmxSnaV6i9drR9g8HCMk2_mtckyS_zAUJIW2KQVZ81d0OFijL2aiaQiaSOtNiV2jKRr0jrm9lysUkvKDwszQMGtOZXhPR2KMWEr_nLHZpryBJdYPf3yF8E7A"


def get_response(prompt, access_token):
    """
    Args:
        prompt:提示词
        access_token

    Returns:流式
    """
    chatbot = Chatbot(config={
        "access_token": access_token,
        "collect_analytics": True,
        # "proxy": "socks5h://127.0.0.1:1090"  # 本地服务器代理端口
    })
    result = chatbot.ask(prompt)
    return result


# 预设
init_content_1 = """简伊的养父死了，我听到这个消息的时候有点愣神。
“林……张小月，你在听吗？”眼前的警察突然大声的向我询问，他有点胖，还有大片的络腮胡子，看起来和张强一个样，我不喜欢他。警察都没什么用。从小我就知道。
“我在听，叔叔。”
“简伊在10月29号那天下午和你在一起吗？”他一直盯着我看，好了，现在我是有点讨厌他了。
我的手心都是汗，不仅他盯着我看，张强也一直盯着我看。
他为什么不被车撞死呢？或者路过大楼的时候被高空抛物砸死！或者吃东西噎死也好。
我能想到如果我回答了是，会发生什么。
可我需要简伊，我们之间的约定。我不能背叛他。
“是的……”我不知道自己的声音这个警察有没有听清楚，可我不敢大声说出来。张强就站在我的旁边，空气都像是枷锁。我感觉自己快要被憋死了。
警察问了很多问题，我只能一一作答。天知道他们问的都是一些什么狗屁不同的问题，如果他们能有用一点，也许我早都能离开这里了。

络腮胡警察终于走向了大门，张强站起来送他出去。他们在门口说了什么，真的很想过去听听。哪怕多一点信息也是好的。
我一秒也不想在客厅呆着了，快步走上楼回到了自己的房间，我知道接下来会发生什么。也许这里不是房间，这里是个妓院。
对，这里是个妓院。只属于张强的妓院。
为什么第一个死的不是他呢？我忍不住这样想。

吱————
门开了。

“简伊是你的男朋友吗？”张强走了进来。
“不是的，爸爸……”
我紧张的捏住了衣角，我知道会发生很么。
“你是个不乖的孩子，小月。”张强的气息喷在我的脸上，我感觉很想吐。
“说谎是不对的，说谎的坏孩子，需要被惩罚。”
……
"""

init_question_1 = "下一步你应该做什么？"
init_choice_1_1 = "逆来顺受"
init_choice_1_2 = "大声呼救"
init_choice_1_3 = "拿床头的台灯砸向张强"

init_summary_1 = "这是一个关于林月和简伊的故事。林月是一个月球孤儿院的小女孩，在被养父母领养后遭受猥亵。简伊是一个月球孤儿院的小男孩，被养父母领养的原因是养母为了追回他的养父，但收养后没有任何效果，所以养母经常打骂他。林月的养父张强是第二个死者，而简伊的养母陈琳是第三个死者。第一个死者是简伊的养父李布衣。"

default_background_1 = """林月和简伊是孤儿院的孩子，后来他们被领养到不同的家庭。林月的养父是个恋童的变态狂，而简伊的养母也经常对他家庭暴力。林月一直想要杀死她的养父张强，一直没有机会。简伊和林月他们偶然在10岁那年重逢了，但是没想到简伊家里出了事，他的养父毛不易以一种诡异的方式死在一个密室里…而林月心底泛起了一个计划……故事以林月作为女主角开展。
"""

default_relationship_1 = """林月：月球孤儿院的一个小女孩，被自己养父母领养之后一直被猥亵
简伊：月球孤儿院的一个小男孩，他被养父母领养的理由是养母为了追回他的养父，但是收养他之后却没有任何的效果，所以养母经常打骂他
张强：林月的养父，第二个死者
陈琳：简伊的养母，第三个死者
李布衣：第一个死者，是简伊的养父
"""

default_character_1 = "林月"

# 用于第一次续写添加预设
# 每次生成续写都用这个
prompt = lambda background, relationship, character, summary, content, question, choice, long_memory: f"""
现在你要作为一个经验丰富的网络小说作家，帮我续写下面这个网络小说，输出时输出你新创作的内容，不可输出之前小说之前的内容！！！
续写指的是接着小说的末尾创作出新的内容，创作出的新内容与小说之前的内容不矛盾，输出时不用将小说之前内容输出！！！

背景设定:
{background}

人物关系:
{relationship}

读者扮演的角色：
{character}

之前小说内容的总结：
{summary}

以下段落是你续写新的段落时要参考的前情提要，续写新的段落内容要和这些段落的内容相关
{long_memory}

当前小说内容（这部分内容禁止输出，你的任务是接着这部分小说内容续写）：
<start>
{content}
<end>

这是读者在上一步面对以下问题时替主角做出的选择：
问题：{question}
选择：{choice}

你需要做的是：
1. 续写小说内容，不超过200字；
2. 要求文风和上文的当前小说保持一致，并且剧情要吸引人，不要重复之前小说的内容！小说要是第一人称的，注意小说中的人物关系和背景设定。请注意这只是一个长篇小说中的一章，剧情不要发展太快。除非听到明确的指令，禁止书写结局，故事应该停在具有悬念的地方，让读者好奇故事接下来的发展。到故事的主人公可以做出选择的地方停止；

输出的格式为：

<start>
续写内容（不包含之前小说内容，不要超过200字！）
<end>


下面给出一些结尾的范例，你需要学习好的结尾，避免差的结尾：
好的结尾：
    1.他突然兴奋地说道：“小赵，我发现了一些线索，这与你父亲的过去有关！”

差的结尾（总结性文字）：
    1.我立刻离开了车间，踏上了寻找答案的道路。
    2.我匆忙离开家，心中充满了对线索的渴望和对真相的追寻。
    3.我决定深入调查，找到这份文件，揭开背后的真相。

注意，续写内容不要超过200字！续写内容要接着之前小说的内容，但是一定不要重复！
注意续写的内容一定不要超过200字！一定要保证生成到<end>!!
记住最重要的是续写内容不超过200字！记住续写内容的风格要和之前小说内容保持一致！语气和文字要符合网络小说的样子！不要太正经！不要简略！续写内容中只要出现一个情节就好，但是要详细展开这个情节的发生过程！至少要包含2个对话和2段细节描写！
"""

init_prompt_v1 = prompt(
    background=default_background_1,
    relationship=default_relationship_1,
    character=default_character_1,
    summary=init_summary_1,
    content=init_content_1,
    question=init_question_1,
    choice=init_choice_1_3,
    long_memory='',
)

# for i in get_response(init_prompt_v1, access_token):
#     print(i)


def continue_write(is_init, access_secret, states, summary, question, choice, background=None, relationship=None,
                   character=None):
    global long_memory
    global memory_index
    if len(long_memory) >= 3:  # 列表大于等于3
        # 输入问题和答案
        instruction_embedding = embedder.encode(question + choice, convert_to_tensor=True)
        memory_scores = util.cos_sim(instruction_embedding, memory_index)[0]
        top_k_idx = torch.topk(memory_scores, k=2)[1]
        top_k_memory = [long_memory[idx] for idx in top_k_idx]
        input_long_term_memory = '\n'.join(
            [f"相关段落{i + 1} :" + selected_memory for i, selected_memory in enumerate(top_k_memory)])
    else:
        input_long_term_memory = None
