from langchain_google_genai import ChatGoogleGenerativeAI
from utils.get_prompt import get_prompt
from states.state import CodeReview, GraphState
from langgraph.types import Command
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
import os

class CodeReviewAgent:

    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0).with_structured_output(CodeReview)

    def run(self, state: GraphState):
        content = ""
        with open(state["file_to_review"].path, "r") as file:
            content = file.read()

        code_review_prompt = get_prompt("agents/code_review_agent/prompts/system_prompt.md")
        code_review_prompt_template = ChatPromptTemplate.from_template(code_review_prompt)
        system_prompt = code_review_prompt_template.invoke({"snippet": content, "context": state["file_to_review"].used_by})

        response = self.model.invoke(system_prompt)


        with open(state["file_to_review"].path + ".md", "w") as file:
            file.write(response.code_documentation)

        return Command(goto="supervisor_agent", update={"messages": [AIMessage(content=response.code_documentation)]})
    
