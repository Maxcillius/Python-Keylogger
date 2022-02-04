import os

os.chdir(r"D:\Gourav\Scripts\Keylogger\\")
Data = []

def filter_kl():
    with open('key_logs.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            letter = line[24:].strip()
            if "'" in letter:
                main = letter.strip()
                Data.append(main[1])
            elif letter == "Key.space":
                Data.append(" ")
            elif letter == "Key.backspace":
                Data.pop()
            elif letter == "Key.right":
                pass
            elif letter == "Key.left":
                pass
            elif letter == "Key.shift_r" or letter == "Key.shift_l" or letter == "Key.shift":
                Data.append(" SHIFT ")
            elif letter == "Key.delete":
                Data.append(" DELETE ")
            elif letter == "Key.enter":
                Data.append(" ENTER ")
            elif letter == "Key.cmd":
                Data.append(" WIN ")
            elif letter == "Key.page_up":
                Data.append(" PG_UP ")
            elif letter == "Key.end":
                Data.append(" END ")
            elif letter == "Key.home":
                Data.append(" HOME ")
            elif letter == "Key.page_down":
                Data.append(" PG_DW ")
            elif letter == "Key.ctrl_l":
                Data.append(" CRTL_L ")
            elif letter == "Key.ctrl_r":
                Data.append(" CRTL_R ")
            else:
                Data.append(letter)

    print(''.join(Data))

filter_kl()