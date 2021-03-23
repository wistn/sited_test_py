# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-12
LastEditors:Do not edit
LastEditTime:2020-05-24
Description:
"""
import sited_test_py.conf


class Setting:
    @classmethod
    def isDeveloperModel(cls):
        if getattr(sited_test_py.conf, "isDeveloperModel", False):
            return bool(
                sited_test_py.conf.isDeveloperModel
            )  # 参数在sited_test_py/conf.py设置
        else:
            return False

