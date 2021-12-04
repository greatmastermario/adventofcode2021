def file_contents(path):
    with open(path, "r", encoding="utf-8") as file:
        return [line.removesuffix("\n") for line in file.readlines()]
