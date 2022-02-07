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
### 集成Poco-SDK

把poco-sdk集成到到公司产品中游戏里请参考[Integration Guide](https://poco.readthedocs.io/en/latest/source/doc/integration.html)

![image](https://user-images.githubusercontent.com/19643260/152683375-7af7bff9-310a-4a3c-9a03-13ea506e0a54.png)

## 使用Poco选择UI对象

### 基本选择器(Basic Selector)

>在poco实例后加一对括号就可以进行UI选择了。选择器会遍历所有UI，将满足给定条件的UI都选出来并返回。

括号里的参数就是所给定的条件，用属性名值对表示，其中第一个参数固定表示 节点名 其余可选参数均表示节点的属性及预期的属性值。

## 初始化

* 切换Airtest IDE poco辅助窗口模式自动插入的初始化语句

### Android原生
```shell
from poco.drivers.android.uiautomation import AndroidUiautomationPoco# 导入poco 
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
```

### iOS原生
```shell
from poco.drivers.ios import iosPoco
poco = iosPoco()
```

### Unity3D
```python
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
```

### UE4
```python
from poco.drivers.ue4 import UE4Poco
poco = UE4Poco()
```

### cocos2dx-lua
```python
from poco.drivers.std import StdPoco
poco = StdPoco()
```

### cocos2dx-js
```python
from poco.drivers.cocosjs import CocosJsPoco
poco = CocosJsPoco()
```

![image](https://user-images.githubusercontent.com/19643260/152731956-57d1182e-db25-4431-a653-f0164641e281.png)


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

### 长按
```python
poco('star_single').long_click()
poco('star_single').long_click(duration=5)
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
poco("android.widget.ScrollView").swipe("up") # up/down/left/right
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

### 2.元素定位

在UI自动化测试中，最关键的就是将目标UI选择出来。一般情况下，通过名字选择是最简单的方式，但是在一些情况下，并不是每个UI控件都有命名，特别是通过代码动态生成和加载的UI，一般都没有一个有意义的名字。Poco提供了强大有效的各种选择方式，不仅可以通过UI单一的属性选择，还可以通过UI之间的层次关系和位置关系来选择出目标UI。更强大的是，以上三种模式可以进行任意串联或者组合使用，这样基本上能应付所有情况了。

* 如何在复杂层次里选出对应的UI控件

```python
from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()

items = poco('main_node').child('list_item').offspring('name'):
first_one = items[0]
print(first_one.get_text())  # => '1/2活力药剂'
first_one.click(
```

poco里的坐标的取值范围是相对于屏幕的，屏幕的宽和高都为单位1，因此也叫[百分比坐标]。
当你需要和某个UI控件附近的UI控件交互或者要点击某个按钮的边缘而不是中间时，那可以用[局部定位]

UI控件交互最终都是和坐标交互，例如:点击一个按钮实际上就是点击某个坐标。
局部定位 就可以基于某个UI的左上角进行偏移，然后可以实现点击到这个UI控件内的各个坐标甚至UI外面的其他坐标。

```python
import time
from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()

image = poco('fish').child(type='Image')
image.focus('center').long_click()
time.sleep(0.2)
image.focus([0.1, 0.1]).long_click()
time.sleep(0.2)
image.focus([0.9, 0.9]).long_click()
time.sleep(0.2)
image.focus([0.5, 0.9]).long_click()
time.sleep(0.2)
```
也可以在选中的UI外单击，通过它的名字标签点击一些模型是非常有用的

```python
# coding=utf-8

from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()

balloonfish_image = poco(text='balloonfish').focus([0.5, -3])
balloonfish_image.long_click()
```

### 3.如何使用拖动来滚动列表

```python
# coding=utf-8

import time
from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()

listView = poco('Scroll View')
listView.focus([0.5, 0.8]).drag_to(listView.focus([0.5, 0.2]))
time.sleep(1)
```


### 4.如何遍历拖动

Poco提供了非常简单的方式来处理一系列UI交互，直接用for循环进行迭代遍历即可。
在for循环中，每次迭代的对象都是一个UI代理，所以可以像之前说的那样，去访问对象的属性和进行对象操作。

```python
import time
from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()

poco('btn_start').click()
poco(text='drag drop').click()
time.sleep(1.5)

shell = poco('shell').focus('center')
for star in poco('star'):
    star.drag_to(shell)
time.sleep(1)

assert poco('scoreVal').get_text() == "100", "score correct."  # 这是另一种断言方法
poco('btn_back', type='Button').click()
```

* 遍历模型所有名称的示例

```python
# coding=utf-8

import time
from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()

for name in poco('plays').offspring('fish').child('name'):
    print(name.get_text())  # pearl/shark/balloonfish
```

### 5.如果从一个不存在的UI控件读取属性或控制它，那就会出现这个异常。

测试一个UI控件是否存在可以调用UI代理的 .exists() 方法

```python
from poco.drivers.unity3d import UnityPoco
from poco.exceptions import PocoNoSuchNodeException

poco = UnityPoco()

node = poco('not existed node')  # select永远不会引发任何异常
try:
    node.click()
except PocoNoSuchNodeException:
    print('oops!')

try:
    node.attr('text')
except PocoNoSuchNodeException:
    print('oops!')

print(node.exists())  # => 假的。此方法不会引发
```

这个异常只会在你主动等待UI出现或消失时抛出，和 PocoNoSuchNodeException 不一样，当你的操作速度太快，界面来不及跟着变化的话，你只会遇到 PocoNoSuchNodeException 而不是 PocoTargetTimeout ，其实就是在那个UI还没有出现的时候就想要进行操作。


### 6.测试脚本如何与UI保持同步，并处理 PocoTargetTimeout 异常

```python
# coding=utf-8

from poco.drivers.unity3d import UnityPoco
from airtest.core.api import connect_device
from poco.exceptions import PocoTargetTimeout


poco = UnityPoco()

# UI is very slow
poco('btn_start').click()
star = poco('star')
try:
    star.wait_for_appearance(timeout=3)  # wait until appearance within 3s
except PocoTargetTimeout:
    print('oops!')
    time.sleep(1)
```

### 7.一些复杂的测试用例中，不可能只是不断地主动控制或者读取属性，通过被动地获取UI状态改变的事件，这样有助于写出不混乱的测试脚本。

Poco提供了简单的轮询机制去同时轮询1个或多个UI控件，所谓轮询就是依次判断UI是否存在。

```python
# coding=utf-8

from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()

# start and waiting for switching scene
start_btn = poco('start')
start_btn.click()
start_btn.wait_for_disappearance()

# waiting for the scene ready then click
exit_btn = poco('exit')
exit_btn.wait_for_appearance()
exit_btn.click()
```

* 轮询UI时等待任意一个,UI出现就往下走

```python
# coding=utf-8

from poco.drivers.unity3d import UnityPoco
from poco.exceptions import PocoTargetTimeout

poco = UnityPoco()

bomb_count = 0
while True:
    blue_fish = poco('fish_emitter').child('blue')
    yellow_fish = poco('fish_emitter').child('yellow')
    bomb = poco('fish_emitter').child('bomb')
    fish = poco.wait_for_any([blue_fish, yellow_fish, bomb])
    if fish is bomb:
        # 跳过炸弹，数到3退出
        bomb_count += 1
        if bomb_count > 3:
            return
    else:
        # 否则点击鱼收集。
        fish.click()
    time.sleep(2.5)
```
* 轮询UI时等待 所有 UI出现才往下走

```python
# coding=utf-8

import time
from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()

poco(text='wait UI 2').click()

blue_fish = poco('fish_area').child('blue')
yellow_fish = poco('fish_area').child('yellow')
shark = poco('fish_area').child('black')

poco.wait_for_all([blue_fish, yellow_fish, shark])
poco('btn_back').click()
time.sleep(2.5)
```

### 8.加快UI操作速度的一种方法（即冻结UI）

只是对于复杂的选择和UI遍历有效，如果只是简单的按名字选择请不要用这种方法，因为一点效果都没有冻结UI其实就是将当前界面的层次结构包括所有UI的属性信息抓取并存到内存里，再跟UI交互时就直接从内存里读取UI属性，而不用在发送rpc请求到game/app里去操作UI。
好处就是一次抓取(消耗几百毫秒），可以使用多次，读取UI属性几乎不消耗时间，同时坏处就是，你需要手动处理UI同步，如果抓取了层次结构后，某个UI控件位置发生了变化，此时如果仍然点击这个UI的话，就会点击到原来的位置上，而不是最新的位置，这很容易导致奇怪的测试结果


使用了冻结UI和不使用冻结UI的效果区别

* Freezing UI
```python
import time
from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()
with poco.freeze() as frozen_poco:
    t0 = time.time()
    for item in frozen_poco('Scroll View').offspring(type='Text'):
        print item.get_text()
    t1 = time.time()
    print t1 - t0  # 大约6 ~ 8秒
```

* No Freezing UI
```python
import time
from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()
t0 = time.time()
for item in poco('Scroll View').offspring(type='Text'):
    print item.get_text()
t1 = time.time()
print t1 - t0  # 约50 ~ 60 s
```

### 9.


### 10.


### 11.


### 12.


