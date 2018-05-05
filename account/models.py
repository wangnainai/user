from django.db import models


class User(models.Model):
    account_name = models.CharField(max_length=20, verbose_name="会员帐号")
    username = models.CharField(max_length=20, verbose_name="会员姓名")
    password = models.CharField(max_length=20, verbose_name="会员密码")
    cell_phone = models.CharField(max_length=11, verbose_name="会员手机号")
    email = models.EmailField( verbose_name="会员邮箱")
    ident_id = models.CharField(max_length=18, verbose_name="会员身份证号")
    is_turbo = models.BooleanField(verbose_name="是否是协会会员", choices=((True, u"是"), (False, u"不是")), default=False)
    is_valid = models.BooleanField(verbose_name="是否启用", choices=((True, u"启用"), (False, u"不启用")), default=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = u"注册会员"
