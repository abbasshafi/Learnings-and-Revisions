from langchain.opneai import OpenAI
from langchain import PromptTemplate

llm=OpenAI(temperature=0.6)
prompt_template_name= PromptTemplate(
    input_variable=['cuisine'],
    template='i want to open a {cuisine} restaurant, suggest some fancy names'
)
name_chain=LLMChain(llm=llm,prompt=prompt_template_name)

prompt_template_name2=PromptTemplate(
    input_variable=['restaurant_name'],
    template='suggest a {restaurant_name} for it.'
)
name_chain2=LLMChain(llm=llm,prompt=prompt_template_name2)

from langchain.chains import SimpleSequentialChain

chain=SimpleSequentialChain(chains=[name_chain,name_chain2])
response=chain.run("pakistani")
print(response)























llm=OpenAI(temperature=0.6)

prompt_template_name=PromptTemplate(
    input_variable=["name"]
    template='suggest me some fancy {name} for a restaurant.'
)
chan1=LLMChain(llm=llm, prompt=prompt_template_name)

prompt_template_name2=PromptTemplate(
    input_variable=['cuisines'],
    template='i want to open {cuisine} restaurant suggest some well known dishes'
)
chan2=LLMChain(llm=llm,prompt=prompt_template_name2)

chain=SimpleSequentialChain(chain=['chan1','chan2'])
response=chain.run('pakistani')
print(response)