from enum import Enum
from typing import Annotated, List, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from pydantic import BaseModel

class FileType:
    def __str__(self):
        return f"{self.path} is used by {self.used_by}"

    def __init__(self, path: str):
        self.path = path
        self.used_by = []

    def add_used_by(self, path: str):
        self.used_by.append(path)



class GraphState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages] 
    project_root: str
    extensions: list[str]
    project_structure: list[FileType]
    file_to_review: FileType


class CodeReview(BaseModel):
    code_documentation: str


class DocumentationReviewStatus(Enum):
    FAILED = "FAILED"
    PASSED = "PASSED"

class DocumentationReview(BaseModel):
    documentation_review_status: DocumentationReviewStatus