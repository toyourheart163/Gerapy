"""
Replace some settings.
"""

import os

import dj_database_url

from server.settings import *

INSTALLED_APPS.remove('gerapy.server.core')
INSTALLED_APPS.append('core')

ROOT_URLCONF = 'dev_server.urls'

MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASS = os.getenv('MONGO_PASS')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASS = os.getenv('MYSQL_PASS')

if os.getcwd() == '/app':
    DEBUG = False

    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL')
        )
    }
    # python manage.py collectstatic
    STATIC_ROOT = os.path.join(os.getcwd(), 'staticfiles')

    # 保持HTTPS连接的时间
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # 自动重定向到安全连接
    SECURE_SSL_REDIRECT = True

    # 避免浏览器自作聪明推断内容类型
    SECURE_CONTENT_TYPE_NOSNIFF = True

    # 避免跨站脚本攻击
    SECURE_BROWSER_XSS_FILTER = True

    # COOKIE只能通过HTTPS进行传输
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # 防止点击劫持攻击手段 - 修改HTTP协议响应头
    # 当前网站是不允许使用<iframe>标签进行加载的
    X_FRAME_OPTIONS = 'DENY'
