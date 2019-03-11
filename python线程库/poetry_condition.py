import threading


class Talker(threading.Thread):

    def __init__(self, name, cond, contents, said_first=None):
        super().__init__(name=name)
        self.name = name
        self.condition = cond
        self.said_first = said_first
        self.contents = contents

    def say(self, content):
        if self.said_first:
            print(self.name + "：" + content)
            self.condition.notify()
            self.condition.wait()
        else:
            self.condition.wait()
            print(self.name + "：" + content)
            self.condition.notify()

    def run(self):
        with self.condition:
            for content in self.contents:
                self.say(content)


if __name__ == '__main__':
    condition = threading.Condition()
    a = Talker(
        "天猫精灵", condition, said_first=True, contents=["嗨！小爱同学", "我们来玩对诗吧！", "我住长江头", "日日思君不见君", "此水几时休", "只愿君心似我心"])
    b = Talker(
        "小爱同学", condition, contents=["在", "好啊", "君住长江尾", "共饮长江水", "此恨何时已", "定不负相思意"])
    b.start()
    a.start()
    a.join()
    b.join()
