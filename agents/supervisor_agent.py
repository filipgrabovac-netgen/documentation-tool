from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.types import Command
from states.state import GraphState
from langchain_core.messages import  AIMessage


class SupervisorAgent:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

    def run(self, state: GraphState):
        if state["project_structure"] is None:
            return Command(goto="file_manager_agent", update={"messages": [AIMessage(content="I need to create a project structure")]})
        
        if len(state["project_structure"]) == 0:
            return Command(goto="END", update={"messages": [AIMessage(content="No more files to review")]})

        return Command(goto="code_review_agent", update={"messages": [AIMessage(content="I need to review the code")], "file_to_review": state["project_structure"].pop()})
