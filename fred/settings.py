# -*- coding: utf-8 -*-

# Scrapy settings for fred project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fred'

SPIDER_MODULES = ['fred.spiders']
NEWSPIDER_MODULE = 'fred.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fred (+http://www.yourdomain.com)'
