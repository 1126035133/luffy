from logging import config
from logging import getLogger

from django.conf import settings

config.dictConfig(settings.LOGGING_DIC)

# 4、输出日志
log = getLogger('default')
