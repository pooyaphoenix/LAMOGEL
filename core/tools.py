from config import Config
from core.color import color


class Tools():
    def log(self, text: str, bold: bool = False):
        if Config.DEBUG_MODE:
            if bold:
                print(color.BOLD + color.BLUE +
                      text +
                      color.END
                      )
            else:
                print(text)


tls = Tools()
