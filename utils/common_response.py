from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, code=1000, msg='成功', status=None, headers=None, **kwargs):
        data = {'code': code, 'msg': msg}
        if kwargs:  # 除了code、msg、status、headers这几个比较特殊的，其他都在data中
            data.update(kwargs)
        self._raw_data = kwargs
        super().__init__(data=data, status=status, headers=headers)
    @property
    def raw_data(self):
        return self._raw_data
