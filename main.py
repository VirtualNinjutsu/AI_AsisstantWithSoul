from deep_translator import GoogleTranslator
import chatter
from intent_classification import IntentClassifier

classifier = IntentClassifier()
def greeting():
    """
    RU: Функция приветствия и получения сообщения от пользователя.
    EN: Greeting function and user message retrieval.
    """
    print('AI Assistant готов к работе')
    user_message = str(input('Обратитесь к ассистенту: '))
    check_message(user_message)


def check_message(user_message):
   """
   RU: Функция определния намерения пользователя.
   EN: Function for determining the user's intent.
   """
   intent = classifier.predict(user_message)
   if intent == 'set_timer':
        print('Установить таймер') #пока что так, чтобы проверить работоспособность, когда допишу модули, перепишу эту часть кода
   elif intent == 'weather':
       print('Погода')
   elif intent == 'note':
       print('Заметка')
   elif intent == 'tell_joke':
       print('Колобок повесился')
   elif intent == 'music':
       print('*звуки гитары*')
   elif intent == 'search_web':
       print('Открыл паутину')
   elif intent == 'chat':
       chat_assistant(user_message)
   else:
       print('ты че несешь?')

def tr_user_input_ru_en(user_message):
   """
   RU:Функция перевода сообщения пользователя с русского на английский.
   EN: Function for translating user messages from Russian to English.
   """
   user_message_tr = GoogleTranslator(source='auto', target='en').translate(user_message)
   return user_message_tr

def tr_user_input_en_ru(ai_a):
   """
   RU: Функция перевода ответа бота с английского на русский.
   EN: Function for translating bot responses from English to Russian.
   """
   ai_a_tr = GoogleTranslator(source='auto', target='ru').translate(ai_a)
   return ai_a_tr

def chat_assistant(user_message):
   """
   RU: Функция общения с ботом.
   EN: Function for interacting with the bot.
   """
   while True:
       user_message_tr = tr_user_input_ru_en(user_message)
       try:
           ai_a = chatter.chat(user_message_tr)
       except Exception as e:
           print(f"Ошибка при получении ответа от бота: {e}")
           continue
       if ai_a == 'Упс!\nПамять переполнена':
           print("Упс!\nПамять переполнена")
           break

       ai_a_tr = tr_user_input_en_ru(ai_a)
       print(ai_a_tr)
       user_message = str(input('User: '))


if __name__ == '__main__':
    greeting()
    