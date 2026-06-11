from morse import encode, decode
from audio import play_morse

def main():
    print("remorsehorse")
    while True:
        mode=input("1=Text->Morse 2=Morse->Text 3=Play Morse q=Quit: ").strip().lower()
        if mode=="q":
            break
        if mode=="1":
            print(encode(input("Text: ")))
        elif mode=="2":
            print(decode(input("Morse: ")))
        elif mode=="3":
            text=input("Text: ")
            morse=encode(text)
            print(morse)
            play_morse(morse)

if __name__=="__main__":
    main()