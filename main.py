from httpcli.output import output
from servercli.server import *
import configparser


# 读取本地的配置文件
current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, "./config/config.ini")
config = configparser.ConfigParser()  # 类实例化
config.read(config_path, encoding="utf-8")
room_list = config.get("server", "room_list")


def main():
    output("WechatBot Run ....")
    get_personal_info()
    bot()

def test():
    output("WechatBot Run ....")
    get_personal_info()
    bot()


if __name__ == "__main__":
    test()
