# Made by www.Movsisyan.info
import json
import requests


class Bot:
    """A simple class to ease bot access"""

    def __init__(self, url, log=None):
        """
        url: bot endpoint\n
        log: bot log filepath
        """
        self.url = url
        self.log = log

    def set_log(self, filepath):

        self.log = filepath

    def log(self, text):
        if self.log is None:
            raise Exception(
                "Log file unspecified, use set_log(filepath) to specify log file path")
        with open(self.log, "a") as l:
            l.write(text + "\n")

    def send_message(self, chat_id, text, markup=None, reply_id=None, disable_notification=False, disable_preview=True):
        prms = {"chat_id": chat_id, "text": text}
        if(markup):
            prms["reply_markup"] = markup
        if(reply_id):
            prms["reply_to_message_id"] = reply_id
        prms["disable_notification"] = disable_notification
        prms["disable_web_page_preview"] = disable_preview

        r = requests.get(self.url + "sendMessage", params=prms)
        return r

    def send_photo(
        self,
        chat_id,
        photo,
        caption=None,
        disable_notification=False,
        reply_markup=None,
    ):
        prms = {"chat_id": chat_id, "photo": photo}
        if(caption):
            prms["caption"] = caption
        if(disable_notification):
            prms["disable_notification"] = disable_notification
        if(reply_markup):
            prms["reply_markup"] = reply_markup

        r = requests.get(self.url + "sendPhoto", params=prms)
        return r

    def ReplyKeyboardMarkup(
        self,
        keyboard,
        resize=True,
        oneTime=True,
        selective=False
    ):
        mrkup = {
            "keyboard": keyboard,
            "resize_keyboard": resize,
            "one_time_keyboard": oneTime,
            "selective": selective
        }
        return json.dumps(mrkup)

    def RemoveKeyboardMarkup(self):
        return '{"remove_keyboard":true}'

    def editMessageText(
        self,
        chat_id,
        message_id,
        text,
        parse_mode=None,
        reply_markup=None
    ):
        prms = {"chat_id": chat_id, "message_id": message_id, "text": text}
        if(parse_mode):
            prms["parse_mode"] = parse_mode
        if(reply_markup):
            prms["reply_markup"] = reply_markup

        r = requests.get(self.url + "editMessageText", params=prms)
        return r


if __name__ == "__main__":
    print("Debug version detected, diagnostics ahead...")

    bot = Bot(
        "https://api.telegram.org/bot{API_KEY}/", "log.txt")

    print("Sending a msg \"Test\"")

    msg = bot.sendMessage("{CHAT_ID}", "Test")
    print(msg)

    print()
    print()
    print()
    msg_id = msg.json()["result"]["message_id"]
    print("Editing text of msg:")
    print(msg_id)
    print(bot.editMessageText("{CHAT_ID}", msg_id, "BLAUBLALBAB"))

    print("Sending a photo of a doggo")

    msg = bot.sendPhoto(
        "{CHAT_ID}", "https://random.dog/a8a8f713-2afc-4f9b-8bee-67ad244e789d.jpg", "Test doggo")
    print(msg)
