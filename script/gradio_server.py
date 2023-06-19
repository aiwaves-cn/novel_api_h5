# -- coding: utf-8 --**
import gradio as gr
import os
from revChatGPT.V1 import Chatbot
import re
from novel_prompt import *
import pandas as pd
import random
from sentence_transformers import SentenceTransformer
from sentence_transformers import  util
import torch
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
embedder = SentenceTransformer('multi-qa-mpnet-base-cos-v1')
# device = torch.device('cpu')
# embedder.to(device)
init_content = ""
init_question = ""
init_choice = ""
init_summary = ""
default_background = ""
default_relationship = ""
default_character = ""
long_memory = []
memory_index = None

use_dict = {"姜昱辰Eleanor": 0, "Fish Yu余腾": 1, "蓝茶": 2, "Victor Chou": 3,
            "树": 4, "云开雾散": 5, "昊达": 6, "饶十八": 7, "随风": 8, "The、one": 9,
            "从前有个王天楠": 10, "半吊子": 11, "彦薪": 12, "茶叶蛋": 13, "yygq": 14}
background_1 = [init_content_1, init_question_1, init_choice_1_1, init_choice_1_2,
                init_choice_1_3,init_summary_1, default_background_1, default_relationship_1, default_character_1]
background_2 = [init_content_2, init_question_2, init_choice_2_1, init_choice_2_2,
                init_choice_2_3,init_summary_2, default_background_2, default_relationship_2, default_character_2]
background_3 = [init_content_3, init_question_3, init_choice_3_1, init_choice_3_2,
                init_choice_3_3,init_summary_3, default_background_3, default_relationship_3, default_character_3]


def show_content():
    global all_content
    return all_content

def get_content_between_a_b(a, b, text):
    ret = re.search(f"{a}(.+){b}", text, re.DOTALL)
    if ret:
        return ret.group(1).strip()
    else:
        ret = re.search(f"{a}(.+)", text, re.DOTALL)
        if ret:
            return ret.group(1).strip()
        else:
            return ""


def get_response(chatbot, prompt):
    prev_text = ""
    for data in chatbot.ask(
            prompt
    ):
        message = data["message"][len(prev_text):]
        print(message, end="", flush=True)
        prev_text = data["message"]
    print()
    return prev_text

def back_choice(use_name, back_number, states):
    global init_content
    global init_question
    global init_choice
    global init_summary
    global default_background
    global default_relationship
    global default_character
    global long_memory
    global memory_index
    global embedder
    with open(r'E:\workspace\novel_api\script\acp.txt') as f:
        content = f.read()
        token_list = content.split(",")
        token_list[0] = token_list[0][1:]
        token_list[-1] = token_list[-1][:-1]
        if "visit" not in use_name:
            access_token = get_content_between_a_b("'access_token': '", "'}", token_list[use_dict[use_name]])
        else:
            access_token = get_content_between_a_b("'access_token': '", "'}",
                                                   token_list[int(use_name.split("visit")[1])])
    # data = pd.read_csv("/home/aiwaves/shid_zhu/interactive_fiction/Access_Token.csv", header=None)
    # Token_number = random.randint(0, 100)
    # access_token = data[0][Token_number]
    if back_number == "夏烟之约":
        init_content, init_question, init_choice_1, init_choice_2, init_choice_3, \
            init_summary, default_background, default_relationship, default_character = background_1
        states["all"] = init_content
        states["cur_content"] = init_content
    elif back_number == "出逃m78":
        init_content, init_question, init_choice_1, init_choice_2, init_choice_3, \
            init_summary, default_background, default_relationship, default_character = background_2
        states["all"] = init_content
        states["cur_content"] = init_content
    elif back_number == "你是谁":
        init_content, init_question, init_choice_1, init_choice_2, init_choice_3, \
            init_summary, default_background, default_relationship, default_character = background_3
        states["all"] = init_content
        states["cur_content"] = init_content
    background = "背景设定" + "\n" + default_background + "人物关系" + "\n" + default_relationship
    long_memory.append(init_content)
    memory_index = embedder.encode(init_content, convert_to_tensor=True).unsqueeze(0)
    # print(long_memory,'\n\n',memory_index)
    return background, init_content, states, init_summary, init_question, init_choice_1, init_choice_2, init_choice_3, access_token

def continue_write(is_init, access_secret, states, summary, question, choice, background=None, relationship=None,
                   character=None):
    global long_memory
    global memory_index
    if len(long_memory) >= 3:
        instruction_embedding = embedder.encode(question+choice, convert_to_tensor=True)
        memory_scores = util.cos_sim(instruction_embedding, memory_index)[0]  # 所有续写和问题选项的向量算分数
        top_k_idx = torch.topk(memory_scores, k=2)[1]  # 取相似度最高的2个的索引
        top_k_memory = [long_memory[idx] for idx in top_k_idx] # 通过索引取出long_memory
        input_long_term_memory = '\n'.join(
            [f"相关段落{i + 1} :" + selected_memory for i, selected_memory in enumerate(top_k_memory)])
    else:
        input_long_term_memory = None

    background = default_background if not background else background
    relationship = default_relationship if not relationship else relationship
    character = default_character if not character else character
    if is_init != 1:
        chatbot = Chatbot(config={
            "access_token": access_secret,
            "collect_analytics": True,
            # "proxy": "socks5h://127.0.0.1:1090"
        })
        next_summary = ""
        for data in chatbot.ask(
                prompt_summary(summary, str(states["cur_content"]), background, relationship, character)):
            written = data['message']
            next_summary = get_content_between_a_b("<start>", "<end>", written)
            if len(next_summary) == 0:
                next_summary = written
            yield is_init, None, None, None, None, None, None, next_summary
    else:
        is_init = 0
        next_summary = summary

    chatbot = Chatbot(config={
        "access_token": access_secret,
        "collect_analytics": True,
        # "proxy": "socks5h://127.0.0.1:1090"
    })
    _written_novel = "-----------------------------\n问题：" + question + \
                     "\n你的选择：" + choice + "\n-----------------------------\n"

    for data in chatbot.ask(
            prompt(background, relationship, character, next_summary, str(states["cur_content"]),
                             str(question), str(choice), input_long_term_memory)):
        written = data['message']
        cur_content = get_content_between_a_b("<start>", "<end>", written)
        yield is_init, None, _written_novel + cur_content, None, None, None, None, next_summary
    states["cur_content"] = cur_content
    states["all"] = states["all"] + "\n\n" + _written_novel + cur_content

    # do choice
    chatbot = Chatbot(config={
        "access_token": access_secret,
        "collect_analytics": True,
        # "proxy": "socks5h://127.0.0.1:1090"
    })
    for data in chatbot.ask(
            prompt_choice(background, relationship, character, next_summary, str(states["cur_content"]))):
        written = data['message']
        cur_question = get_content_between_a_b("问题：", "选项1：", written)
        cur_choice1 = get_content_between_a_b("选项1：", "选项2：", written)
        cur_choice2 = get_content_between_a_b("选项2：", "选项3：", written)
        cur_choice3 = get_content_between_a_b("选项3：", "<end>", written)
        yield is_init, None, cur_content, cur_question, cur_choice1, cur_choice2, cur_choice3, next_summary
    # states["all"] = states["all"] + "\n\n" + _written_novel + cur_content
    long_memory.append(cur_content)
    cur_memory_index = embedder.encode(cur_content, convert_to_tensor=True).unsqueeze(0)
    memory_index = torch.cat((memory_index, cur_memory_index), 0)
    yield is_init, states, states["all"], cur_question, cur_choice1, cur_choice2, cur_choice3, next_summary


def continue_ten_write(is_init, access_secret, states, summary, question, choice, background=None, relationship=None,
                   character=None):
    background = default_background if not background else background
    relationship = default_relationship if not relationship else relationship
    character = default_character if not character else character

    chatbot = Chatbot(config={
        "access_token": access_secret,
        "collect_analytics": True,
        # "proxy": "socks5h://127.0.0.1:1090"
    })
    if is_init != 1:
        next_summary = ""
        for data in chatbot.ask(prompt_summary(summary, str(states["cur_content"]), background, relationship, character)):
            written = data['message']
            next_summary = get_content_between_a_b("<start>", "<end>", written)
            if len(next_summary) == 0:
                next_summary = written
            yield is_init, None, None, None, None, None, None, next_summary
    else:
        is_init = 0
        next_summary = summary

    chatbot = Chatbot(config={
        "access_token": access_secret,
        "collect_analytics": True,
        # "proxy": "socks5h://127.0.0.1:1090"
    })
    _written_novel = "-----------------------------\n问题：" + question + \
        "\n你的选择：" + choice + "\n-----------------------------\n"

    for data in chatbot.ask(
            prompt_ten_begin(background, relationship, character, next_summary, str(states["cur_content"]), str(question), str(choice))):
        written = data['message']
        cur_content = get_content_between_a_b("<start>", "<end>", written)
        yield is_init,None, _written_novel + cur_content, None, None, None, None, next_summary
    states["cur_content"] = cur_content

    states["all"] = states["all"] + "\n\n" + _written_novel + cur_content

    for i in range(8):
        title = "第" + str(i+2) + "次输出" + "\n"
        chatbot = Chatbot(config={
            "access_token": access_secret,
            "collect_analytics": True,
            # "proxy": "socks5h://127.0.0.1:1090"
        })
        next_summary = ""
        for data in chatbot.ask(
                prompt_summary(next_summary, str(states["cur_content"]), background, relationship, character)):
            written = data['message']
            next_summary = get_content_between_a_b("<start>", "<end>", written)
            if len(next_summary) == 0:
                next_summary = written
            yield is_init, None, states["cur_content"], None, None, None, None, next_summary

        chatbot = Chatbot(config={
            "access_token": access_secret,
            "collect_analytics": True,
            # "proxy": "socks5h://127.0.0.1:1090"
        })
        for data in chatbot.ask(
                prompt_ten_continue(background, relationship, character, next_summary, str(states["cur_content"]))):
            written = data['message']
            cur_content = get_content_between_a_b("<start>", "<end>", written)
            yield is_init, None, title + cur_content, None, None, None, None, next_summary
        states["cur_content"] = cur_content
        states["all"] = states["all"] + "\n\n" + cur_content

    chatbot = Chatbot(config={
        "access_token": access_secret,
        "collect_analytics": True,
        # "proxy": "socks5h://127.0.0.1:1090"
    })
    next_summary = ""
    for data in chatbot.ask(
            prompt_summary(next_summary, str(states["cur_content"]), background, relationship, character)):
        written = data['message']
        next_summary = get_content_between_a_b("<start>", "<end>", written)
        if len(next_summary) == 0:
            next_summary = written
        yield is_init, None, "最后一次输出"+ "\n" + states["cur_content"], None, None, None, None, next_summary

    chatbot = Chatbot(config={
        "access_token": access_secret,
        "collect_analytics": True,
        # "proxy": "socks5h://127.0.0.1:1090"
    })

    for data in chatbot.ask(
            prompt_ten_end(background, relationship, character, next_summary, str(states["cur_content"]))):
        written = data['message']
        cur_content = get_content_between_a_b("<start>", "<end>", written)
        yield is_init, None, cur_content, None, None, None, None, next_summary
    states["cur_content"] = cur_content
    states["all"] = states["all"] + "\n\n" + cur_content

    # do choice
    chatbot = Chatbot(config={
        "access_token": access_secret,
        "collect_analytics": True,
        # "proxy": "socks5h://127.0.0.1:1090"
    })
    for data in chatbot.ask(
            prompt_choice(background, relationship, character, next_summary, str(states["cur_content"]))):
        written = data['message']
        cur_question = get_content_between_a_b("问题：", "选项1：", written)
        cur_choice1 = get_content_between_a_b("选项1：", "选项2：", written)
        cur_choice2 = get_content_between_a_b("选项2：", "选项3：", written)
        cur_choice3 = get_content_between_a_b("选项3：", "<end>", written)
        yield is_init, None, cur_content, cur_question, cur_choice1, cur_choice2, cur_choice3, next_summary
    # states["all"] = states["all"] + "\n\n" + _written_novel + cur_content
    yield is_init, states, states["all"], cur_question, cur_choice1, cur_choice2, cur_choice3, next_summary


def regenerate_choices(states):
    chatbot = states["chatbot"]

    written = ""
    for data in chatbot.ask_stream(prompt_regenerate):
        written += data
        choice1_text = get_content_between_a_b("选项1：", "选项2：", written)
        choice2_text = get_content_between_a_b("选项2：", "选项3：", written)
        choice3_text = get_content_between_a_b("选项3：", "", written)
        yield choice1_text, choice2_text, choice3_text


with gr.Blocks(title="互动式小说体验", css="footer {visibility: hidden}", theme="default") as demo:
    gr.Markdown(
        """
    # 第一人称互动式小说生成器
    """)
    with gr.Tab("一次生成一段"):
        states_cn = gr.State(value={})
        is_init_cn = gr.State(value=1)
        with gr.Row():
            with gr.Column():
                with gr.Box():
                    with gr.Row():
                        user_name = gr.Dropdown(
                            ["姜昱辰Eleanor", "Fish Yu余腾", "蓝茶", "Victor Chou",
                             "树", "云开雾散", "昊达", "饶十八", "随风", "The、one",
                             "从前有个王天楠", "半吊子", "彦薪", "茶叶蛋", "yygq",
                             "visit15", "visit16", "visit17", "visit18", "visit19",
                             "visit20", "visit21", "visit22", "visit23", "visit24",
                             "visit25", "visit26", "visit27", "visit28", "visit29"], label="用户名称")
                        back_number = gr.Dropdown(
                            ["夏烟之约", "出逃m78", "你是谁"], label="选择设定")
                        back_init = gr.Button(
                                 "确认", variant="primary")
                    access_secret = gr.Textbox(
                        label="access_token", max_lines=3, lines=3, interactive=True)
                    background = gr.Textbox(
                        label="小说背景", placeholder="请先选择设定后点击确认", max_lines=18, lines=18, interactive=True)
                    story = gr.Textbox(
                        label="小说开始", placeholder="请先选择设定后点击确认", max_lines=35, lines=35, interactive=True)
            with gr.Column():
                novel_summary = gr.Textbox(
                    label="内容总结", placeholder="请先选择设定后点击确认", max_lines=18, lines=13, interactive=True)
                written_novel = gr.Textbox(
                    label="小说生成内容", max_lines=35, lines=30, interactive=True)
                question = gr.Textbox(
                    label="问题", max_lines=3, lines=1, interactive=True)
                choice1_text = gr.Textbox(
                    label="选择1", max_lines=3, lines=1, interactive=True)
                choice2_text = gr.Textbox(
                    label="选择2", max_lines=3, lines=1, interactive=True)
                choice3_text = gr.Textbox(
                    label="选择3", max_lines=3, lines=1, interactive=True)
                with gr.Row():
                    choice1 = gr.Button("选择1", variant="primary")
                    choice2 = gr.Button("选择2", variant="primary")
                    choice3 = gr.Button("选择3", variant="primary")
                    # regenerate = gr.Button("重新生成选择", variant="primary")
        back_init.click(back_choice, inputs=[user_name, back_number, states_cn],
                        outputs=[background, story, states_cn, novel_summary, question, choice1_text, choice2_text, choice3_text, access_secret])
        choice1.click(continue_write,
                      inputs=[is_init_cn, access_secret, states_cn, novel_summary, question, choice1_text],
                      outputs=[is_init_cn, states_cn, written_novel, question, choice1_text, choice2_text, choice3_text, novel_summary])
        choice2.click(continue_write,
                      inputs=[is_init_cn, access_secret, states_cn, novel_summary, question, choice2_text],
                      outputs=[is_init_cn, states_cn, written_novel, question, choice1_text, choice2_text, choice3_text, novel_summary])
        choice3.click(continue_write,
                      inputs=[is_init_cn, access_secret, states_cn, novel_summary, question, choice3_text],
                      outputs=[is_init_cn, states_cn, written_novel, question, choice1_text, choice2_text, choice3_text, novel_summary])
    with gr.Tab("一次生成十段"):
        states_en = gr.State(value={})
        is_init_en = gr.State(value=1)
        with gr.Row():
            with gr.Column():
                with gr.Box():
                    with gr.Row():
                        user_name = gr.Dropdown(
                            ["姜昱辰Eleanor", "Fish Yu余腾", "蓝茶", "Victor Chou",
                             "树", "云开雾散", "昊达", "饶十八", "随风", "The、one",
                             "从前有个王天楠", "半吊子", "彦薪", "茶叶蛋", "yygq",
                             "visit15", "visit16", "visit17", "visit18", "visit19",
                             "visit20", "visit21", "visit22", "visit23", "visit24",
                             "visit25", "visit26", "visit27", "visit28", "visit29"], label="用户名称")
                        back_number = gr.Dropdown(
                            ["夏烟之约", "出逃m78", "你是谁"], label="选择设定")
                        back_init = gr.Button(
                            "确认", variant="primary")
                    access_secret = gr.Textbox(
                        label="access_token", max_lines=3, lines=3, interactive=True)
                    background = gr.Textbox(
                        label="小说背景", placeholder="请先选择设定后点击确认", max_lines=18, lines=18, interactive=True)
                    story = gr.Textbox(
                        label="小说开始", placeholder="请先选择设定后点击确认", max_lines=35, lines=35, interactive=True)
            with gr.Column():
                novel_summary = gr.Textbox(
                    label="内容总结", placeholder="请先选择设定后点击确认", max_lines=18, lines=13, interactive=True)
                written_novel = gr.Textbox(
                    label="小说生成内容", max_lines=35, lines=30, interactive=True)
                question = gr.Textbox(
                    label="问题", max_lines=3, lines=1, interactive=True)
                choice1_text = gr.Textbox(
                    label="选择1", max_lines=3, lines=1, interactive=True)
                choice2_text = gr.Textbox(
                    label="选择2", max_lines=3, lines=1, interactive=True)
                choice3_text = gr.Textbox(
                    label="选择3", max_lines=3, lines=1, interactive=True)

                with gr.Row():
                    choice1 = gr.Button("选择1", variant="primary")
                    choice2 = gr.Button("选择2", variant="primary")
                    choice3 = gr.Button("选择3", variant="primary")
                    # regenerate = gr.Button("重新生成选择", variant="primary")
        back_init.click(back_choice, inputs=[user_name, back_number, states_en],
                        outputs=[background, story, states_en, novel_summary, question, choice1_text, choice2_text,
                                 choice3_text, access_secret])
        choice1.click(continue_ten_write,
                      inputs=[is_init_en, access_secret, states_en, novel_summary, question, choice1_text],
                      outputs=[is_init_en, states_en, written_novel, question, choice1_text, choice2_text, choice3_text,
                               novel_summary])
        choice2.click(continue_ten_write,
                      inputs=[is_init_en, access_secret, states_en, novel_summary, question, choice2_text],
                      outputs=[is_init_en, states_en, written_novel, question, choice1_text, choice2_text, choice3_text,
                               novel_summary])
        choice3.click(continue_ten_write,
                      inputs=[is_init_en, access_secret, states_en, novel_summary, question, choice3_text],
                      outputs=[is_init_en, states_en, written_novel, question, choice1_text, choice2_text, choice3_text,
                               novel_summary])
    demo.queue(concurrency_count=1000)

if __name__ == "__main__":
    gr.close_all()
    demo.launch(server_port=8012, share=True,
                show_api=False)
