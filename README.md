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


# EN
This is my first large-scale Python project. In the future, I plan to add a unique character for each task of the assistant.

## How to Use:
1)Install a GGUF model, for example, from Hugging Face (https://huggingface.co/models?library=gguf&sort=trending).
2)In the chaters.py file, specify the path to the downloaded model in the model_dir variable.
3)Install dependencies: pip install -r requirements.txt.

## Using with GPU:
By default, everything is set up for using models via CPU. If you want to use a GPU:

1) Uninstall PyTorch: pip uninstall torch torchvision torchaudio.
2) Install CUDA — based on my personal tests, the best option right now is CUDA 12.4.
3) Install PyTorch with CUDA support: pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124.
4) In the chatter.py file, modify the llm variable values, following the comments.
P.S. You can install a different CUDA version, but it’s important to check its compatibility with PyTorch (https://pytorch.org/). On the same site, you can find the updated command for step 3.

## Plans:
1)Write code for the assistant’s actions.
2)Add different "personalities" for the assistant.
3)Add a graphical interface.
