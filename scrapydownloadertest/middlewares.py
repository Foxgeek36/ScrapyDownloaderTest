import random
from scrapy import Request


class RandomUserAgentMiddleware():
    '''
    自定义的获取随机ua的中间件
    '''
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1'
        ]

    def process_request(self, request, spider):
        '''
        修改ua设置/ 随机做匹配
        :param request:
        :param spider:
        :return:
        '''
        request.headers['User-Agent'] = random.choice(self.user_agents)

    def process_response(self, request, response, spider):
        '''
        修改response的响应状态码
        :param request:
        :param response:
        :param spider:
        :return:
        '''
        response.status = 201
        return response

    # 亦可设置异常处理的函数/ 暂时不需要
    # def process_exception(self, request, exception, spider):
    #     pass