from code_compilers.base_compiler import BaseCompiler


class TypescriptCompiler(BaseCompiler):
    def compile(self, file_path: str, project_root: str):
        print(f"Compiling {file_path}")
        print(f"Scanning for imports...\n")

        imports = []

        with open(file_path, "r") as file:
            content = file.read()
            for line in content.split("\n"):
                if "import" in line:
                    print(f"Found import at: {line}")
                    import_path = line.split("from")[1].strip().strip(";").strip('\"')

                    count = import_path.count("../")
                    temp_project_root = project_root
                    import_path = import_path.replace("../", "")

                    for _ in range(count):
                        temp_project_root = "/".join(temp_project_root.split("/")[:-1])
                    
                    import_path = temp_project_root + "/" + import_path
                    imports.append(import_path)

        print("\n-------------------------------- Successfully added and formatted imports --------------------------------\n")
        return imports