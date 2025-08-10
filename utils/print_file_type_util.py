
from states.state import FileType


def print_file_type(file_obj: FileType):
    print(f"📄 - {file_obj.path}")
    
    if file_obj.used_by:
        print(f"   └── Koristi se u ({len(file_obj.used_by)} datoteka):")
        for used_by_path in file_obj.used_by:
            print(f"       • {used_by_path}")
    else:
        print(f"   └── Nije korišten u drugim datotekama")
    print()  
    
    print(f"{'='*50}\n")
