from langchain_google_genai import ChatGoogleGenerativeAI
from utils.get_prompt import get_prompt
from states.state import GraphState
from langgraph.types import Command
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END
from langchain_core.messages import AIMessage

class DocumentationReviewAgent:

    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0).with_structured_output()

    def run(self, state: GraphState):
        documentation = state["messages"][-1].content

        prompt = get_prompt("agents/documentation_review_agent/prompts/system_prompt.md")

        prompt_template = ChatPromptTemplate.from_template(prompt)

        system_prompt = prompt_template.invoke({"snippet": documentation, "documentation_content": state["messages"][-1].content})

        response = self.model.invoke(system_prompt)
        
        with open(state["file_to_review"].path + ".md", "w") as file:
                file.write(response.documentation_review_status)
                    
                
        return Command(goto="supervisor_agent", update={"messages": [AIMessage(content="Documentation review complete")]})
            
