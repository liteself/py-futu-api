# -*- coding: utf-8 -*-
from pprint import pprint

from futu import *

from futu.quote.quote_get_warrant import Request

from futu.quote.quote_stockfilter_info import SimpleFilter


def hk_filter(qt_ctx):
  """-------------------------------------------------"""

  field = SimpleFilter()
  field.filter_min = -101
  field.filter_max = -30
  field.stock_field = StockField.CHANGE_RATE_BEGIN_YEAR
  field.is_no_filter = False
  field.sort = SortDir.ASCEND

  field2 = SimpleFilter()
  field2.filter_min = 10
  field2.filter_max = 1000
  field2.stock_field = StockField.CUR_PRICE
  field2.is_no_filter = False
  # field2.sort = SortDir.DESCEND

  field3 = SimpleFilter()
  field3.filter_min = 10000000000
  field3.filter_max = 100000000000000
  field3.stock_field = StockField.MARKET_VAL
  # field3.sort = SortDir.ASCEND
  field3.is_no_filter = False
  #
  # field3 = SimpleFilter()
  # field3.stock_field = StockField.CUR_PRICE_TO_HIGHEST52_WEEKS_RATIO
  # field3.is_no_filter = True

  ret, ls = quote_ctx.get_stock_filter(Market.HK, [field, field2, field3])
  last_page, all_count, ret_list = ls
  pprint(all_count)
  pprint(ret_list)

  """-------------------------------------------------"""
  return ret_list

def us_filter(qt_ctx):
  """-------------------------------------------------"""

  field = SimpleFilter()
  field.filter_min = -101
  field.filter_max = -30
  field.stock_field = StockField.CHANGE_RATE_BEGIN_YEAR
  field.is_no_filter = False
  field.sort = SortDir.ASCEND

  field2 = SimpleFilter()
  field2.filter_min = 100
  field2.filter_max = 1000000000
  field2.stock_field = StockField.CUR_PRICE
  field2.is_no_filter = False
  # field2.sort = SortDir.DESCEND

  field3 = SimpleFilter()
  field3.filter_min = 10000000000
  field3.filter_max = 100000000000000
  field3.stock_field = StockField.MARKET_VAL
  # field3.sort = SortDir.ASCEND
  field3.is_no_filter = False
  #
  # field3 = SimpleFilter()
  # field3.stock_field = StockField.CUR_PRICE_TO_HIGHEST52_WEEKS_RATIO
  # field3.is_no_filter = True

  ret, ls = quote_ctx.get_stock_filter(Market.US, [field, field2, field3])
  last_page, all_count, ret_list = ls
  pprint(all_count)
  pprint(ret_list)

  """-------------------------------------------------"""
  return ret_list

def get_warrant(qt_ctx):
  req = Request()
  req.sort_field = SortField.CODE
  req.ascend = True
  req.type_list = [WrtType.BEAR, WrtType.CALL]
  req .issuer_list = [Issuer.CS, Issuer.CT, Issuer.EA]
  print(quote_ctx.get_warrant("HK.00700", req))

if __name__ == '__main__':
  quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)


  us_filter(quote_ctx)

  quote_ctx.close()


