from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from datetime import datetime

def get_current_time():
    now =  datetime.now()
    return f"The current time is: {now.strftime('%Y-%m-%d %H:%M:%S')} "

root_agent = Agent(name = "google_adk_time_agent",
                   description = "An agent that greets the user and provides the current time.",
                   model="gemini-2.5-flash",
                   instruction= """You are a helpful and friendly AI assistant.
                   Greet the user warmly and use the tools when needed.""",
                    tools=[get_current_time]
                   )

# Convert to A2A server (this enables the agent card)
app = to_a2a(root_agent)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)