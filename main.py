from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.tools import BraveSearch
import rich
import os

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY =os.getenv("OPENAI_API_KEY")

prompt = "What is the weather like today?"

search = BraveSearch.from_api_key(api_key="BSAv1neIuQOsxqOyy0sEe_ie2zD_n_V", search_kwargs={"count": 1})

tools = [
    Tool(
    name ="Search" ,
    func=search.run,
    description="useful when you need to answer questions about current events"
    ),
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm=ChatOpenAI(temperature=0)
agent_chain = initialize_agent(tools, llm, agent="chat-conversational-react-description",
                                verbose=True, memory=memory)

output = agent_chain.run(input=prompt)

rich.print(output)