import string


letters = string.ascii_letters+"()'. "


def convert_fcklan(code) -> str:
    position = 0
    result = []
    
    for process in code:
        if process == "+":
            position += 1
        elif process == "(":
            position = 0
        elif process == ")":
            position = len(letters)-1
        elif process == ".":
            result.append(position)
            
    return "".join(letters[number] for number in result)


if __name__ == "__main__":
    code = input(">>> ")
    eval(convert_fcklan(code))
