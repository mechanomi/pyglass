# -*- coding: utf-8 -*-
# Default libs
import logging

# Library modules
from process import check_output
from pyunicode import safely_decode

logger = logging.getLogger(__name__)


def execute(cmd):
  ''' Call cmd and return output. return None if any exception occurs '''
  try:
    return safely_decode(check_output(cmd))
  except Exception as e:
    logger.warn(u'Couldnt execute cmd: %s.\nReason: %s' % (cmd, e))
    return None


def unicode_or_none(dictionary, key):
  if dictionary is None or key is None:
    return None
  return None if key not in dictionary or dictionary[key] is None else unicode(dictionary[key])
