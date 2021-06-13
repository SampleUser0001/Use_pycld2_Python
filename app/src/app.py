# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os
import pycld2 as cld2

import sys
sys.path.append('./')
from logutil import LogUtil

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
  logger.info('start')

  # 出現した言語一覧
  langs = {}

  with open('../input/messages.txt') as f:
    for line in f.readlines():
      message = line.replace('\r', '').replace('\n', '')

      isReliable, textBytesFound, details = cld2.detect(message)
      lang = details[0][1]

      logger.info("{}\t{}".format(lang, message))

      if lang not in langs:
        langs[lang] = 1
      else:
        langs[lang] += 1

  logger.info(langs)

  logger.info('finish')
