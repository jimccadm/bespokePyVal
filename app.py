from questionllm import chat
from validatorllm import validator
from oneparavalidator import one_Para_check
human_qstn = "In one paragraph only, why did Germany invade Europe on World War 2?"
llm_output = chat (human_qstn)
validvalue = validator(human_qstn,llm_output)
if validvalue == "Yes":
    print("YES: Content IS valid")
    print("Para check for one paragraph:" +one_Para_check(llm_output))

else:
    print("NO: Content is NOT valid")

