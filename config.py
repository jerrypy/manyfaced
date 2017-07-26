#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseZfConfig:
    """
    正方教务系统爬虫配置基类。
    新增学校爬取时，继承该基类，修改与下面不同的条目即可。
    """

    have_captcha = False

    urls = {
        'base_url': 'http://jwxt.njupt.edu.cn/',  # 正方教务系统根地址
        'captcha_path': 'CheckCode.aspx',  # 验证码地址
        'login_path': '',  # 登录请求提交地址
        'login_success_path': 'xs_main.aspx',  # 登录成功后，跳转页面地址。用于判断是否登录成功。
        'info_path': 'xsgrxx.aspx',  # 个人信息页面地址
        'avatar_path': 'readimagexs.aspx',  # 头像地址
        'score_path': 'xscj_gc.aspx',  # 成绩地址
        'cet_score_path': 'xsdjkscx.aspx',  # 等级考试成绩地址
        'course_path': 'xskbcx.aspx'  # 课程表地址
    }


class BaseOpacConfig:
    """
    Opac图书馆系统爬虫配置基类。
    新增学校爬取时，继承该基类，修改与下面不同的url即可。
    """

    have_captcha = False

    base_url = 'http://202.119.228.6:8080/'  # opac系统根地址
    captcha_path = 'reader/captcha.php'  # 验证码地址
    login_path = 'reader/redr_verify.php'  # 登录请求提交地址
    login_success_path = 'reader/redr_info.php'  # 登录成功后，跳转页面地址。用于判断是否登录成功。
    info_path = 'reader/redr_info_rule.php'  # 个人信息页面地址
    current_list_path = 'reader/book_lst.php'  # 当前借阅图书列表
    history_path = 'reader/book_hist.php'   # 借阅历史
    book_review_path = 'reader/book_rv.php'  # 书评
    search_history_path = 'reader/search_hist.php'  # 检索历史
    recommend_path = 'reader/asord_lst.php'  # 推荐历史
    reserve_path = 'reader/preg.php'  # 预约历史
    book_shelf_path = 'reader/book_shelf.php'  # 书架信息
    loss_path = 'reader/book_loss.php'  # 丢失历史
    fine_path = 'reader/account.php'  # 罚款
    find_detail_path = 'reader/fine_pec.php'  # 罚款明细


class NjuptJwConfig(BaseZfConfig):
    """南邮教务系统配置"""
    pass


class NjuptLibConfig(BaseOpacConfig):
    """南邮图书馆系统配置"""
    pass


if __name__ == '__main__':
    pass
