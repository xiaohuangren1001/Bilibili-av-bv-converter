### Bilibili-av-bv-converter
用户手册（中文版）

本转换器开源，可以自行把代码拿去研究

---
首先将avbv.py下载到python路径中的site-packages文件夹下 ~~（我不会pypi，所以没有弄到pypi）~~

使用方法：导入avbv模块，就可以用av2bv和bv2av来进行互转了

示例代码：
```python
from abv_py import av2bv, bv2av
print(av2bv(170001)) # BV17x411w7KC
print(bv2av('BV17x411w7KC')) # 170001
```
当在bv2av中输入不合法bv号（如bv1）会报错（TypeError）

但是下面的代码不会报错：
```python
from abv_py import bv2av
print(bv2av('BV17x411w7KC')) # 170001
```
