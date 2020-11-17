lines = ""
while True:
    cur_inp = input()
    lines += cur_inp + "\n"
    if cur_inp == '0':
        break
result = tuple(lines.split())
