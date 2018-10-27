from . import index_blu


@index_blu.route('/')
def index():
    # # session["name"] = "baidu.com"
    # # 测试打印日志
    # logging.debug("测试debug")
    # logging.warning("测试warning")
    # logging.error("测试error")
    # logging.fatal("测试fatal")
    # # 根据项目应用logger 会根据应用程序的调试状态去调整日志级别
    # # current_app.logger.error("测试error")
    return 'index'