import sys
import time

template = '''Title: $$TITLE$$
Date: $$DATE$$
Modified: $$DATE$$
Tags: whatsapp, telegram
Slug: $$SLUG$$
Author: Doc
Status: Draft
'''

template.replace('$$TITLE$$', sys.argv[1:])
template.replace('$$DATE$$', time.strftime("%Y-%m-%d %H:%M:%S"))
