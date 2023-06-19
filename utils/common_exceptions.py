from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from utils.common_logger import logger


def exception_handler(exc, context):
    # 请求地址，请求方式，请求时间，如果登录了，记录用户id
    request = context.get('request')
    try:
        user_id = request.user.pk
        if not user_id:
            user_id = '匿名用户'
    except:
        user_id = '匿名用户'
    view = context.get('view')
    logger.error('用户：【%s】，使用：【%s】 请求，请求：【%s】 地址，视图函数是：【%s】，报错了，错误是：【%s】' % (
        user_id, request.method, request.get_full_path(), str(view), str(exc)
    ))
    res = drf_exception_handler(exc, context)
    if res:
        # drf异常
        res = Response(data={'code': 999, 'msg': res.data.get('detail', '服务器出错，请联系系统管理员')})
    else:
        # django异常
        res = Response(data={'code': 888, 'msg': str(exc)})

    return res
