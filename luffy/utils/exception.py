from rest_framework.views import exception_handler

from .response import APIResponse
from .logger import log


def common_exception_handler(exc, context):
    log.error('view: %s, 错误: %s' % (context['view'].__class__.__name__, str(exc)))
    result = exception_handler(exc, context)

    if not result:
        if isinstance(exc, KeyError):
            return APIResponse(code=0, msg='key error', status=404)
        return APIResponse(code=0, msg='unknown error', result=str(exc))

    return APIResponse(code=0, msg='error', result=result.data, status=result.status_code)