def get_prompt(prompt_path: str):
    with open(prompt_path, "r", encoding="utf-8") as prompt_file:
        return prompt_file.read()