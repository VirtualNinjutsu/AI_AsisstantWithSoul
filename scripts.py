from threading import Timer
import requests
from requests import Request
import speech_recognition as sr
from transformers import AutoProcessor, BarkModel
from decouple import config
import torch

api_key_weather = config('WEATHER_API_KEY')


class Countdown:
    '''
    RU: Класс для создания таймера.
    EN: Class for creating a timer.
    '''
    def __init__(self,time):
        print('Тест программы начался')
        func = self.notification
        self.timer(time, func)
    def notification(self):
        print('Время истекло!')
    def timer(self, time, func):
        t = Timer(time, func)
        t.start()


class Weather:
    '''
    RU: Класс для получения информации о погоде.
    EN: Class for obtaining weather information.
    '''
    def __init__(self):
        self.api = api_key_weather
        self.city = str(input('Введите свой город:')).lower()
        self.answer = self.parcing_weather(self.city)
    def parcing_city(self,city):
        try:
            url_find = 'http://api.openweathermap.org/data/2.5/find'
            params = {'q': self.city, 'type': 'like', 'units': 'metric', 'APPID': self.api}
            req = Request('GET', url_find, params=params)
            prepared = req.prepare()
            print("Сформированный URL:", prepared.url)
            res = requests.get(prepared.url)
            data = res.json()
            city_list = ['{} ({})'.format(d['name'], d['sys']['country'])
                    for d in data['list']]
            print('city:', city_list)
            city_id = data['list'][0]['id']
            print('city_id=', city_id)
        except Exception as e:
            print("Exception (find):", e)
    def parcing_weather(self,city):
        url_find = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': self.city, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': self.api}
        req = Request('GET', url_find, params=params)
        prepared = req.prepare()
        res = requests.get(prepared.url)
        data = res.json()
        cloud = data['weather'][0]['description']
        temp = data['main']['temp']
        feels = data['main']['feels_like']
        answer =  f'Облачность: {cloud}. Температура воздуха: {temp}℃, ощущается как {feels}℃.'
        return answer
    def __str__(self):
        return self.answer

        
class STT:
    '''
    RU: Класс для распознавания речи.
    EN: Class for speech recognition.
    '''
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognize()
    def recognize(self):
        try:
            with sr.Microphone() as source:
                print('Микрофон включен:')
                self.audio = self.recognizer.listen(source, timeout = 5, phrase_time_limit = 10)
            self.text = self.recognizer.recognize_google(self.audio, language = 'ru-RU')
            print(f'Распознанный текст: {self.text}')
            return self.text
        except sr.UnknownValueError:
            print("Не удалось распознать речь в аудиофайле.")
            return None
        except sr.RequestError as e:
            print(f"Ошибка сервиса Google Speech: {e}")
            return None
        except sr.AudioException as e:
            print(f"Ошибка при обработке аудиофайла: {e}")
            return None
    def __str__(self):
        return self.text


class Voice:
    '''
    RU: Класс для синтеза речи.
    EN: Class for speech synthesis.
    '''
    def __init__(self):
        self.model_path = config('BARK_MODEL_PATH')
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.voice_preset = "v2/ru_speaker_3"
        self.model = BarkModel.from_pretrained(self.model_path, torch_dtype=torch.float32).to(self.device)
        self.processor = AutoProcessor.from_pretrained(self.model_path)
        print(f"Используется устройство: {self.device}")
    def generate(self, text):
        '''
        RU: Функция для генерации речи.
        EN: Function for speech generation
        '''
        self.inputs = self.processor(text, voice_preset=self.voice_preset, return_tensors="pt",)
        self.inputs = self.inputs.to(self.device)
        self.inputs = {key: value.to(self.device) for key, value in self.inputs.items()}
        self.wav_maker()
    def wav_maker(self):
        '''
        RU: Функция для создания аудиофайла.
        EN: Function for creating an audio file.
        '''
        from scipy.io.wavfile import write as write_wav
        self.audio_array = self.model.generate(**self.inputs,do_sample=True)
        self.audio_array = self.audio_array.cpu().numpy().squeeze()
        self.sample_rate = self.model.generation_config.sample_rate
        write_wav("bark_generation.wav", self.sample_rate, self.audio_array)
        



if __name__ == '__main__':
    test = Voice()