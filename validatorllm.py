import ollama

def validator(question,llm_response):
    

    q_Validator = f"Has {llm_response} as a response to the human question {question} provided a sufficent response?"
    combi_qanda = "Human Question:" + question + "LLM Answer was:" + llm_response
    print ("****\n" + combi_qanda)

    response = ollama.chat(model='bespoke-minicheck:latest', messages=[
    {
        'role': 'user',
        'content': q_Validator,
    },
    ])
    return(response['message']['content'])