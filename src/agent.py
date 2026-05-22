import os
from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from tavily import TavilyClient

_tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def web_search(query: str) -> str:
    """Search the web for up-to-date information on a given query."""
    response = _tavily.search(query=query, max_results=5)
    results = response.get("results", [])
    if not results:
        return "No results found."
    return "\n\n".join(
        f"<search_result>\n{r['title']}\n{r['url']}\n{r['content'][:500]}\n</search_result>"
        for r in results
    )

root_agent = Agent(
    name="google_adk_web_search_agent",
    description="An agent that can search the web to answer questions.",
    model="gemini-2.5-flash",
    instruction="""You are a helpful and friendly AI assistant.
Use the web_search tool to find up-to-date information when answering questions, only if it is necessary.""",
    tools=[web_search],
)

# Convert to A2A server (this enables the agent card)
app = to_a2a(root_agent)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
