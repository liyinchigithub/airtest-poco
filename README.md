# airtest-poco

游戏自动化测试框架airtest+poco

## 安装

### 本地环境

在电脑上安装poco，并把poco-sdk集成到游戏里

```shell
pip install pocoui
```

```shell
pip install poco
```

```shell
pip install airtest
```
### 集成SDK

把sdk集成到游戏里请参考 [Integration Guide](https://poco.readthedocs.io/en/latest/source/doc/integration.html)

![image](https://user-images.githubusercontent.com/19643260/152683375-7af7bff9-310a-4a3c-9a03-13ea506e0a54.png)

## 使用Poco选择UI对象

### 基本选择器(Basic Selector)

>在poco实例后加一对括号就可以进行UI选择了。选择器会遍历所有UI，将满足给定条件的UI都选出来并返回。

括号里的参数就是所给定的条件，用属性名值对表示，其中第一个参数固定表示 节点名 其余可选参数均表示节点的属性及预期的属性值。



## 常用操作

### 点击
```python
# text属性
poco(text="我的").click()
# name属性
poco("com.example.homeking.client:id/ivClose").click()
# type属性
poco("android.widget.TextView").click()
# anchorPoint属性（坐标）
poco([0.5, 0.5]).click()
```

### 输入
```python
# 获取元素对象
phone_input=poco(text="请输入手机号码")
# 输入手机号
phone_input.set_text("12000001203")
```


### 断言
```python
# 获取控件的text属性值
value = poco(text="个人信息").attr("text")
# 断言
assert_equal(value, "个人信息", "文本字体内容是：'个人信息'") # 参数1实际值 参数2期望值
```


### 判断元素是否存在
```python
# 判断是否在登录页
if poco(text="账号密码登录").exists():
        logger.info("退出登录成功")
        ad=poco("com.example.homeking.client:id/ivClose ")
        # 判断是否弹出广告弹窗
        if ad.exists():
            ad.click()
    else:
        logger.info("退出登录失败")
```


### 获取屏幕大小
```python
screen_size=poco.get_screen_size()
```

### 上滑
```python
poco("android.widget.ScrollView").swipe("up") #
```

### 滑动
```python
# 从A滑动到B
point_a = [0.1, 0.1]
center = [0.5, 0.5]
poco.swipe(point_a, center)

# swipe 从A滑动到给定方向
direction = [0.1, 0]
poco.swipe(point_a, direction=direction)

```

### 日志引入
```python
import logging
# 日志配置
logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)
# 使用
logger.info("登录成功")
```

### 截图
```python
b64img, fmt = poco.snapshot(width=720)
open('screen.{}'.format(fmt), 'wb').write(b64decode(b64img))
```

### 唤醒屏幕
```python
poco.device..wake()
```


## 注意事项：

### 1.断处理断言失败
不论是airtest提供的断言接口，还是Airtest-selenium提供的断言接口，如果断言失败，都会引发AssertionError，从而导致脚本执行终止；
如果不想脚本因为一个断言失败就终止，可以将断言用try语句包起来

```python
value =poco("com.miui.calculator:id/btn_8_s").attr("text")
try:
    assert_equal(value, "8", "按钮值为8")
except 
    AssertionError:
print("按钮值断言失败")
```

### 2.


### 3.


### 4.


### 5.


### 6.



