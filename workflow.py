from langgraph.graph import StateGraph, START, END
from agents.supervisor_agent import SupervisorAgent
from agents.file_manager_agent.file_manager_agent import FileManagerAgent

from agents.code_review_agent.code_review_agent import CodeReviewAgent
from states.state import GraphState

def graph_workflow():
    supervisor_agent = SupervisorAgent()
    file_manager_agent = FileManagerAgent()
    code_review_agent = CodeReviewAgent()
    graph = StateGraph(GraphState)

    graph.add_node("supervisor_agent", supervisor_agent.run)
    graph.add_node("file_manager_agent", file_manager_agent.run)
    graph.add_node("code_review_agent", code_review_agent.run)

    graph.add_edge(START, "supervisor_agent")

    return graph.compile()

