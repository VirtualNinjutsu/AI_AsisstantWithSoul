# AI_AsisstantWithSoul

Это мой первый масштабный проект на Python, в будующем планирую добавить под каждую задачу своего ассистента со своим характером 

## Как использовать:
1) Установить gguf модель например с Hugging Face (https://huggingface.co/models?library=gguf&sort=trending)
2) В файле chaters.py в переменной model_dir указать путь к скачанной модели
3) Установите зависимости: `pip install -r requirements.txt`

## Использование с GPU
По умолчанию все стоит для использования моделей через CPU, если вы хотите использовать GPU:
1) Удалить pytorch - `pip uninstall torch torchvision torchaudio`
2) Установить CUDA - по моим личным тестам, лучшим вариантом сейчас является CUDA 12.4
3) Установить pytorch с поддержкой CUDA - `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`
4) В файле chatter.py изменить значения переменной "llm" придерживаясь комментариев
P.S Вы можете установить другую версию CUDA, но важно прверить ее совместимость с pytorch (https://pytorch.org/) на этом же сайте можно посмотреть новую команду для 3 шага

## Планы:
1) Прописать код для действий ассистента
2) Добавить разные "личности" для ассистента
3) Графический интерфейс 
