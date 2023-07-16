import logging
# from unit import logging_util
import logging.config

# 1.初始化日志对象，调用logging_util.py 文件中的日志方法
# logger = logging.getLogger('mainModule.sub')  # 获取main函数


# 输出 日志信息
# logger.warning('公共配置.py文件：这是一个警告信息')
# logger.info('公共配置.py文件：这是一个提示信息')


# 2. 使用配置文件：调用 log.conf 文件的配置输出日志
# logging.config.fileConfig('log.conf')  # 对应的conf 文件名称
# logger = logging.getLogger('hand01')  # 对应的keys 的值


# 输出日志信息
# logger.warning('公共配置.cof文件：这是一个警告信息')
# logger.info('公共配置.cof文件：这是一个提示信息')


# 3.文件和控制台同时输出
logging.config.fileConfig('file_console_log.conf')  # 对应的conf 文件名称
root_logger = logging.getLogger('root')
root_logger.debug('test root logger...')
root_logger.info('双输出日志之控制台输出：提示信息~~~')


main_logger = logging.getLogger('main')
main_logger.info('双输出日志之文件输出：提示信息！！！！')

main_logger.info('test another')
