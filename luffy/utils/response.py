from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, code=1, msg='ok', result=None, status=None, content_type=None, **kwargs):
        dic = {
            'code': code,
            'msg': msg,
        }

        if result:
            dic['result'] = result

        dic.update(kwargs)

        super().__init__(data=dic, status=status, content_type=content_type)
