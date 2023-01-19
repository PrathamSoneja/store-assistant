import requests
import openai

with open('config.txt', 'r') as f:
    x = f.readlines()[1]

api_key = str(x)

def info_call(url):
    #url = f'https://540zfa.deta.dev/items/{id}'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    item_id = response.json()['item_id']
    item_name = response.json()['item_name']
    item_type = response.json()['item_type']
    item_desc = response.json()['item_desc']
    _ = response.json()['quantity']
    price = response.json()['price']
    return item_name, item_type, item_desc, price

def ques_call(url):
    #url = f'https://540zfa.deta.dev/items/{id}/{question}'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    return response

def gpt_call(desc, question):
    openai.api_key = api_key
    start_sequence = "\nA:"
    restart_sequence = "\n\nQ: "
    init_prompt = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\"."
    prompt = f"{init_prompt} {desc} {restart_sequence}{question} {start_sequence}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text

