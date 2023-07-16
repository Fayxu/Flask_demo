import logging

# 设置输出级别, 默认是 WARN ,
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='[%Y-%m-%d %H:%M:%S]',
#                     filename='./my_log',
#                     filemode='a')
#
# logging.critical('logging.critical message')
# logging.error('logging.error message')
# logging.warning('logging.warning message')
# logging.info('logging.info message')
#
# logging.debug('logging.debug message')



# 初始化日志对象
logger = logging.getLogger('mainModule')  # 获取main函数
logger.setLevel(level=logging.DEBUG)  # 设置级别
# 格式控制
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 1初始化文件对象
handle = logging.FileHandler('log_01.log', encoding='utf-8')  # 定义handler代表文件，选择FileHandler
handle.setFormatter(formatter)  # 设置格式

# 1初始化控制台对象
console = logging.StreamHandler()  # 定义console 代表控制台，选择StreamHandler
console.setFormatter(formatter)  # 设置格式


# 2把文件对象添加到日志handle中
logger.addHandler(handle)
# 2把控制台对象添加到日志handle中
logger.addHandler(console)

# 输入日志信息在控制台
# logger.critical('致命错误')
# logger.error('错误信息')
# logger.warning('警告信息')
# logger.info('提示信息')
