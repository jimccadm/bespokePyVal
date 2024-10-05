from questionllm import chat
from validatorllm import validator
human_qstn = "In one paragraph only, why did Germany invade Europe on World War 2?"
llm_output = chat (human_qstn)
validvalue = validator(human_qstn,llm_output)
print (validvalue)
