# my_package/__init__.py

# 可以导入子模块
# __init__.py
from .crud import *
from .database import *
from .dependencies import *
from .main import *
from .models import *
from .schemas import *


# 定义包内变量或常量
VERSION = '1.0'

# 执行初始化代码（示例：设置日志）
import logging
logging.basicConfig(level=logging.INFO)
