import time
from dateutil.parser import parse as date_parser
import re
"https://curl.trillworks.com/"
if __name__ == '__main__':
    html ="""<span class="url-icon"><img alt=[汗] src="//h5.sinaimg.cn/m/emoticon/icon/default/d_han-0e7b8aa6d1.png" style="width:1em; height:1em;" /></span>一直好喜欢"""""
    datetime_str = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(datetime_str)
