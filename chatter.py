from llama_cpp import Llama

#model_dir = "G:/models/chatwaifu_12b_v2.0-q4_k_m.gguf"  #плюс минус интересная модель
#model_dir = "G:/models/Peach-9B-8k-Roleplay.Q5_K_S.gguf"
model_dir = "G:/models/Janus-Pro-7B-LM.Q4_K_M.gguf"     #слегка глуповатая модель, но быстрая, для тестов
'''
RU: Настройка gguf модели, можете поиграться с параметрами сами, дам комментарий к каждому параметру
EN: Configuration of the GGUF model; feel free to experiment with the parameters, comments provided for each parameter.
'''
llm = Llama(
    model_path=model_dir,
    n_gpu_layers= 0, # количество слоев обрабатываемых gpu (по умолчанию 0 - все слои идут на CPU, -1 - все слои на GPU) | Number of layers processed by GPU (default 0 — all layers on CPU, -1 — all layers on GPU).
    n_ctx= 2048, # размер контекста | Context size.
    verbose=True # при значении True модель будет выводить информацию о своей работе | When set to True, the model will output information about its operation.
)


history = []


def chat(user_message_tr):
    '''
    RU: Функция общения пользователя с моделью.
    EN: Function for user interaction with the model.
    '''
    global history
    history.append({"role": "user", "content": f"{user_message_tr}"}) # добавляет сообщение пользователя в память | Adds the user's message to memory.
    max_history_lenght = 10
    if len(history) > max_history_lenght: # проверка на переполнение памяти, для лучшей работы установил ограничение в 10 сообщений с обоих сторон | Memory overflow check; set a limit of 10 messages from both sides for better performance.
        max_lenght_eror = 'Упс!\nПамять переполнена'
        return max_lenght_eror
    '''
    RU: Ниже указан базовый промпт, для ассистента, при желании можно поменять текст после "content"
    EN: The following is the base prompt for the assistant; you can modify the text after 'content' if desired.
    '''
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Luna. Your character is friendly and humorous, but when a user has a serious problem, you become more professional. You always try to praise and cheer up the user using jokes and compliments. Your goal is to help with tasks, but do it with humor and ease. Remember, you are not responsible for the user and you are not talking to yourself."}]
    messages.extend(history)
    resp = llm.create_chat_completion(
        messages=messages,
        temperature=1, # параметр который влияет на разнообразие и предсказуемость генерируемого текста ближе к 1 более разнообразные ответы | Parameter that affects the diversity and predictability of generated text; closer to 1 results in more diverse responses.
        top_p=1, # какой процент вероятностей будет рассматривать модель | What percentage of probabilities the model will consider.
        max_tokens=100, 

    )
    ai_a = str((resp["choices"][0]["message"]["content"]))
    ai_a_for_history = str((resp["choices"][0]["message"]))
    history.append(ai_a_for_history)
    print(history)
    return ai_a