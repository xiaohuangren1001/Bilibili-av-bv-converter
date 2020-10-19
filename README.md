### Bilibili-av-bv-converter
本转换器开源，可以自行把代码拿去研究

使用方法：导入avbv模块，就可以用av2bv和bv2av来进行互转了

示例代码：
```python
from avbv import av2bv, bv2av
print(av2bv('av170001')) # BV17x411w7KC
print(bv2av('BV17x411w7KC')) # av170001
```
当在bv2av中输入不合法bv号（如bv1）会报错（IndexError）

但是下面的代码不会报错：
```python
from avbv import bv2av
print(bv2av('DV17x411w7KC')) # av170001
```
