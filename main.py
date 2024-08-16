from telegram.client import Telegram


bot_token='7234382332:AAFfB0sxfJd7twC4RFEMhpT24NxnOlgUBG4'

def incoming_message_handler(update):
    print(update)


def bot_get_me():
    phone = '+919517677829'
    files_directory = '~/tdlib_files/' + phone
    tg = Telegram(
        api_id=22975272,
        api_hash='2dac9dffd65357e3040f2723ba3d1019',
        database_encryption_key="changeme1234",
	    phone=phone
    )
    # you must call login method before others
    tg.login()
    tg.add_message_handler(incoming_message_handler) 
    tg.idle()
 
if __name__ == "__main__":
    bot_get_me()
