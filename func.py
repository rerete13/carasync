import re 




async def change_symbols(num):
    num = num.upper()
    arr_change_settings = [('А', 'A'), ('В', 'B'), ('К', 'K'), ('Т', 'T'), ('О', 'O'), ('М', 'M'), ('С', 'C'), ('Е', 'E'), ('Х', 'X'), ('Р', 'P'), ('І', 'I'), ('Н', 'H')]
    for j in arr_change_settings:
        num = num.replace(j[0], j[1])

    return num


async def cleaning(text):
    pattern = r"[0-9-.]+"
    res = ''.join(re.findall(pattern, text))
    return res

