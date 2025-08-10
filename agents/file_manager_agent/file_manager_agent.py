import os
from utils.print_file_type_util import print_file_type
from states.state import GraphState
from states.state import FileType
from code_compilers.typescript_compiler import TypescriptCompiler
from langgraph.types import Command

compilers = {
    "tsx": TypescriptCompiler()
}

class FileManagerAgent:
    def run(self, state: GraphState):
        extensions: list[str] = state["extensions"]
        project_root = state["project_root"]

        project_structure: set[FileType] = set()

        for root, dirs, files in os.walk(project_root):
            for file in files:

                if file.endswith(tuple(extensions)):
                    file_type = FileType(os.path.join(root, file))
                    project_structure.add(file_type)

        for file in project_structure:
            extension = file.path.split(".")[-1]

            if extension in compilers.keys():
                file.used_by = compilers[extension].compile(file.path, project_root)

        for file in project_structure:
            print_file_type(file)

        return Command(goto="supervisor_agent", update={"project_structure": project_structure})
        