# Scrapy settings for seleniumcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'seleniumcrawler'

SPIDER_MODULES = ['seleniumcrawler.spiders']
NEWSPIDER_MODULE = 'seleniumcrawler.spiders'

SPIDER_MIDDLEWARES = {
'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': True,
}

COOKIES_ENABLED = True
COOKIES_DEBUG = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36'
