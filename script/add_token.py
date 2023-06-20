from mongoengine import Document, StringField, DateTimeField, connect
import datetime

# 当前时间
current_time = datetime.datetime.now()

# 连接本地 MongoDB 数据库
connect('your_database_name')


# # 连接远程 MongoDB 数据库
# from mongoengine import connect
# from urllib.parse import quote_plus
#
# connect('novel_api_h5', host="mongodb://%s:%s@%s" % (quote_plus("aiwaves"), quote_plus("bxzn2023"), "47.96.122.196"))

class Access_token_pool(Document):
    access_token = StringField()
    now_time = DateTimeField()


access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJqaWF0a2IwNjU2QHdlcC5lbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlfSwiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS9hdXRoIjp7InVzZXJfaWQiOiJ1c2VyLWdGV3RRS2QxYkJuWmNsbWgzeXdrNllzSCJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiYXV0aDB8NjQ0YTFiMmUxZGVjOGQyZWRhOGQxZmU0IiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4NjExMDMzNywiZXhwIjoxNjg3MzE5OTM3LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9yZ2FuaXphdGlvbi53cml0ZSJ9.0fI-3RYbF1eg_kRzE3Q3QYNGa6kgOgsaPvt4m9HREjRkYFKWGVP3lBWxGQkG3553imEr2vZjETn4hyHFGj-LLYg1XpLpa-_zvhjITyzzT4flUZijFp6tzZg185WIySeXrmoKmZTxL7ij1LF1Un6Y2IRPSIbvOvugr5wWvrPZtZD0xHcgmzmj-A1xJytjM7zhdlKtaJiK_VyeR6wlTv5fLdjPWxU5nutmxSnaV6i9drR9g8HCMk2_mtckyS_zAUJIW2KQVZ81d0OFijL2aiaQiaSOtNiV2jKRr0jrm9lysUkvKDwszQMGtOZXhPR2KMWEr_nLHZpryBJdYPf3yF8E7A"
# Access_token_pool(access_token=access_token,now_time=current_time).save()


token_obj = Access_token_pool.objects.first()
token_obj.access_token = access_token
token_obj.save()