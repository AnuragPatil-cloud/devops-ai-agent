from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from tools import *

load_dotenv()

tools = [
    get_s3_buckets,
    get_ec2_instances,
    get_vpcs,
    get_cloudwatch_alarms
]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm, tools, prompt)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

result = executor.invoke({
    "input": "Audit my AWS account and give issues and summary"
})

print("\n===== FINAL OUTPUT =====\n")
print(result["output"])
