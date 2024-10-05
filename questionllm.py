import ollama

def chat(question):
    print(question)
    response = ollama.chat(model='llama3.2:3b', messages=[
    {
        'role': 'user',
        'content': question,
    },
    ])
    return(response['message']['content'])