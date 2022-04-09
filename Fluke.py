from PIL import Image
import stepic, os, re
from os import system, name
while True:
    try:
        print("""
            ███████╗██╗     ██╗   ██╗██╗  ██╗███████╗
            ██╔════╝██║     ██║   ██║██║ ██╔╝██╔════╝
            █████╗  ██║     ██║   ██║█████╔╝ █████╗  
            ██╔══╝  ██║     ██║   ██║██╔═██╗ ██╔══╝  
            ██║     ███████╗╚██████╔╝██║  ██╗███████╗
            ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                    Dev : D O R T R O 乂\n\n""")

        decenc = int(input("Press 1 for encoding\nPress 2 for decoding\n"))
        while decenc == 1:
            try:
                Files = []
                I = 0
                for filename in os.listdir('./Encodes'):
                    I += 1
                    Files.append(f"{I}. {filename}")
                print(Files)

                while True:
                    try:
                        Encode = input("Select the Image index number to encode:\n")
                        if re.search(".*[a-zA-Z].*", Encode):
                            print('Invalid input')
                        else:
                            break
                    except Exception as e:
                        print(e)

                for name in Files:
                    if Encode in name:
                        target = name[len(Encode)+2: ]
                        I = 0
                        break
                    else:
                        pass

                if I != 0:
                    print('File not found!')
                else:
                    break
            except Exception as e:
                print(e)

        while decenc == 2:
            try:
                Files = []
                I = 0
                for filename in os.listdir('./Decodes'):
                    I += 1
                    Files.append(f"{I}. {filename}")
                print(Files)

                while True:
                    try:
                        Decode = input("Select the Image index number to decode:\n")
                        if re.search(".*[a-zA-Z].*", Decode):
                            print('Invalid input')
                        else:
                            break
                    except Exception as e:
                        print(e)

                for name in Files:
                    if Decode in name:
                        target = name[len(Decode)+2: ]
                        I = 0
                        break
                    else:
                        pass

                if I != 0:
                    print('File not found!')
                else:
                    break
            except Exception as e:
                print(e)
        if decenc == 1:
            Message= input("Message to hide:\n")
            Name = input("Save as: ")
            inf = Image.open(f"./Encodes/{target}")
            imf1 = stepic.encode(inf, bytes(Message, "utf-8"))
            imf1.save(f'./Decodes/{Name}','PNG')
            print('Task completed.')
        else:
            im = Image.open(f'./Decodes/{target}')
            print(stepic.decode(im))
        while True:
            try:
                loop = input("Want to Encode/Decode next Image?\n[y/n]: ").lower()
                if loop == "n" or loop == "y":
                    break
                print("Invalid input!")
            except Exception as e:
                print(e)
        if loop == "n":
            break
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    except Exception as e:
        print(e)