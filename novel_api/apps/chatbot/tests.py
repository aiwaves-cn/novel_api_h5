import datetime
import threading
from rest_framework.exceptions import APIException
from mongoengine import Document, StringField, DateTimeField, connect

# 连接 MongoDB 数据库
connect('your_database_name')

class Access_token_pool(Document):
    access_token = StringField()
    now_time = DateTimeField()

    @classmethod
    def create_tokens(cls, num_tokens):
        current_time = datetime.datetime.now()
        for i in range(num_tokens):
            token = cls(access_token=str(i), now_time=current_time)
            token.save()

    @classmethod
    def get_oldest_token(cls):
        current_time = datetime.datetime.now()
        oldest_token = cls.objects.order_by('now_time').first()  # 未取到不会报错
        print(oldest_token)
        if oldest_token:
            oldest_token.now_time = current_time
            oldest_token.save()
        return oldest_token  # 如果不存在会为None

# token_lock = threading.Lock()  # 创建互斥锁

def concurrent_get_token():
    try:
        # with token_lock:  # 使用互斥锁
            oldest_token = Access_token_pool.get_oldest_token()
            print(oldest_token.access_token)
            return oldest_token
    except Exception as e:
        APIException("获取 token 出错:", str(e))


# 创建测试数据
# Access_token_pool.create_tokens(50)

# 模拟并发获取 token
threads = []
for _ in range(100):
    thread = threading.Thread(target=concurrent_get_token)
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()
