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

#Sequential Chain____________________________________
from langchain.chains import SequentialChain

llm=OpenAI(temperature)

prompt1=PromptTemplate(
    input_variable=['cuisine'],
    template='I want to make a {cuisine} restaurant. Suggest some fancy name for it.'
)
cuisine_chain=LLMChain(llm=llm,prompt=prompt1,output_key='restaurant_name')

prompt2=PromptTemplate(
    input_variable=['restaurant_name'],
    template='Suggest me some menu items for {restaurant_name}'
)
menu_chain=LLMChain(llm=llm,prompt=prompt2,output_key='menu_items')

chain=SequentialChain(chain=[cuisine_chain,menu_chain],input_variables=[cuisine],
                      output_variables='restaurant_names','menu_items')























llm =OpenAI(temperature=0.7)

tem1=PromptTemplate(
    input_variable=['name'],
    template='I want to open a {name} restaurant. suggest me some good names for it.'
)

chan=LLMChain(llm=llm, prompt=tem1)

tem2=PromptTemplate(
    input_variable=['cuisine']
    template='suggest me some menu items for {cuisine}'
)
chan=LLMChain(llm=llm,prompt=tem2)

chain=