from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from workflow import graph_workflow
from langgraph.prebuilt import create_react_agent

load_dotenv()

def main():
    graph = graph_workflow()

    response = graph.invoke({"messages": [HumanMessage(
        content="/Users/filipgrabovac/Documents/Programming/documentation-tool/test-project")], 
        "project_root": "/Users/filipgrabovac/Documents/Programming/documentation-tool/test-project", 
        "extensions": [".tsx", ".html"],
        "project_structure": None})

    print(response)


if __name__ == "__main__":
    main()