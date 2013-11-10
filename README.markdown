AssignPhoneticName.py
=====================

需求
----

- Mac OS X 10.5 (or other ScriptingBridge-capable systems)
- Python (Pre-installed in Mac OS X)

使用
----

### Python 版本

1. 关闭 Address Book。

2. 执行:

    python AssignPhoneticName.py

这个命令会给所有*包含中文*的地址簿项根据 First Name 和 Last Name
分别分配对应的汉语拼音作为 Phonetic First Name 和 Phonetic Last
Name。对于已经分配了 Phonetic Name 的，会跳过，除非使用 `-r`
参数调用这个脚本。

### 或者使用 Objective-C 版本

1. 关闭 Address Book。

2. 执行:

    make && ./apn

这个版本使用 Apple 的基于 ICU 的拼音数据，比 Python
版本更全而且带音调信息。

---

其他的问题请联系 gzjjgod@gmail.com。

Please use it at your own risk..
