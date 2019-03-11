from urllib import request
import re


class Spider:

    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.64.1vvodajpnbv'

    # 发送请求，获取响应HTML
    def __fetch_content(self):
        r = request.urlopen(self.__class__.url)
        htmls = str(r.read(), encoding='UTF-8')
        return htmls

    # <div class="video-info">
    #     <span class="video-title" title="S8小组赛FW vs AFS">
    #         S8小组赛FW vs AFS
    #     </span>
    #     <span class="video-nickname" title="S8全球总决赛">
    #         <i class="icon-hostlevel icon-hostlevel-vip"></i>
    #         S8全球总决赛
    #     </span>
    #     <span class="video-number">198.0万</span>
    #     <span class="video-station-info">
    #         <i class="video-station-num">281人</i>
    #     </span>
    # </div>
    # 分析获取的HTML
    @staticmethod
    def __analysis(htmls):
        # print(htmls)
        anchors = re.findall(
            '<div class="video-info">.*?<span class="video-nickname".*?</i>(.*?\
                )</span>.*?<span class="video-number">(.*?)</span>.*?\
                </div>', htmls, re.S)
        return anchors

    # 数据精炼
    @staticmethod
    def __refine(anchors):
        anchors = list(map(
            lambda x: {'name': x[0].strip(), 'number': x[1].strip()}, anchors))
        return anchors

    @staticmethod
    def __sort(anchors):
        anchors = sorted(anchors, key=Spider.__sort_seed, reverse=True)
        return anchors

    @staticmethod
    def __sort_seed(anchors):
        number_str = anchors['number']
        if number_str.endswith('万'):
            result = re.findall('[0-9]*\.*\d+', number_str)
            seed = float(result[0]) * 10000
        else:
            seed = float(number_str)
        return seed

    @staticmethod
    def __show(anchors):
        print('\n=============================\n')
        print('name\tnumber\torder')
        for i in range(0, len(anchors)):
            print(
                anchors[i]['name'] + '\t' + anchors[i]['number'] + '\t' + str(
                    i + 1))
            print('\n=============================\n')

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__class__.__analysis(htmls)
        anchors = self.__class__.__refine(anchors)
        anchors = self.__class__.__sort(anchors)
        self.__class__.__show(anchors)


spider = Spider()
spider.go()
