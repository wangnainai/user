from django.apps import AppConfig
import os

default_app_config = "account.PrimaryBlogConfig"


def get_current_app_name(file):
    return os.path.split(os.path.dirname(file))[-1]


class PrimaryBlogConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = u'用户管理'