from telegram.client import Telegram


bot_token='7234382332:AAFfB0sxfJd7twC4RFEMhpT24NxnOlgUBG4'
api_id=22975272
api_hash='2dac9dffd65357e3040f2723ba3d1019'
database_encryption_key="changeme1234"

def incoming_message_handler(update):
    print(update)


def bot_get_me():
    phone = '+919517677829'
    files_directory = '~/tdlib_files/' + phone
    tg = Telegram(api_id=api_id, api_hash=api_hash, database_encryption_key=database_encryption_key, phone=phone)
    tg.login()
    tg.add_message_handler(incoming_message_handler) 
    result = tg.get_chats()
    print(result.update)
    result.wait()
    chat_id1 = -1001740088159
    # send_message = tg.send_message(chat_id=chat_id1, text="Hello")
    # send_message.wait()
    chat_history = tg.get_chat_history(chat_id=-chat_id1)
    chat_history.wait()
    print(chat_history.update) 
    # for chat_id in result.update['chat_ids']:
    #     print(chat_id)
    #     chat_history = tg.get_chat_history(chat_id=chat_id)
    #     chat_history.wait()
    #     print(chat_history.update)
        
    tg.idle()
 
if __name__ == "__main__":
    bot_get_me()
