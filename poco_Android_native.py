# -*- encoding=utf8 -*-
__author__ = "liyinchi"

import logging
from base64 import b64decode
from airtest.core.api import * # 导入airtest apoi
# Airtest IDE自动插入的初始化语句
from poco.drivers.android.uiautomation import AndroidUiautomationPoco# 导入poco 
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 日志配置
logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)
# airtest初始化
auto_setup(__file__)

# 唤醒屏幕
poco.device..wake()

# 启动指定app
#start_app(package="com.example.homeking.client",activity="com.example.homeking.client.controllers.intro.IntroActivity")

# 等待
# sleep(5)


# 获取元素对象
vClose=poco("com.example.homeking.client:id/ivClose")
# 判断是否已在登录页面
if vClose.exists():
    # 在给定时间内等待一个UI出现并返回这个UI，并进行点击
    vClose.wait(5).click()
# 点击
poco(text="我的").click()
# 判断是否已登录
if poco(text="个人信息").exists():
    logger.info("已是登录状态")
    poco(text="个人信息").click()
    # 上滑
    poco("android.widget.ScrollView").swipe("up")
    # 点击
    poco(text="退出登录").wait(2).click()
    poco(text="确定").wait(2).click()
    # 判断是否退出成功
    if poco(text="账号密码登录").exists():
        logger.info("退出登录成功")
        ad=poco("com.example.homeking.client:id/ivClose ")
        # 判断是否弹出广告弹窗
        if ad.exists():
            ad.click()
    else:
        logger.info("退出登录失败")
else:
    poco(text="账号密码登录").click()
    # 输入
    poco(text="请输入手机号码").set_text("12000001203")
    poco('com.example.homeking.client:id/etInputPassword').set_text("")
    # 点击
    poco("com.example.homeking.client:id/tvPasswordLogin").click()

    # 截图
    b64img, fmt = poco.snapshot(width=720)
    open('screen.{}'.format(fmt), 'wb').write(b64decode(b64img))

    # 点击

    # 获取控件的text属性值
    value = poco(text="个人信息").attr("text")
    # 断言
    assert_equal(value, "个人信息", "文本字体内容是：'个人信息'") #参数1实际值 参数2期望值

    # 获取屏幕大小
    screen_size=poco.get_screen_size()
    logger.info(screen_size)
    



