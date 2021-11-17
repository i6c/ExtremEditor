import base64
import msvcrt
import os
import random
import threading
import tkinter as tk
from tkinter import filedialog

from colored import fg

from legit.WindowManage import Focus


class Icon(object):
    def __init__(self):
        self.img = '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ZbC7W8ZrQjjAFTPtDeygdltzgdoStti3X6A1JbSjthHQCX/z5PfYigWAsbM/i/KSqluH3xLkV1AhI8q7UX6SCeiu9Nl791JMAPkcKDwDrDDK5P6ug9puQK8GblOlCWFs/2er9kzFRp+ijvxCayFPO2nr8x/vNb/H1i4AUNCIDSL808DR6JYbyqXdHozdFuwfxfN/fJPaDUCLwfs8FPJgMgSap1HhBYH9+9+b6/cfULQOytx7pfO9f8ORX2mNsrSnMqgqHPd/nvwe24AAyAGNQqjwKHZHri0dj5iCNdH/cd8eWmy4SWDjfg0oExFej7Cf5tkXW6C05xa8H5vbr7T3ZOztePJ7bDMCIABbegsPAC9QeS+AoUITsIdzPZqA7RXehPXd90d4K/AaUSYUb29Lkh9oFWjPupLed3nyewwDhnXW3fsmBetD3wxMfwWG/L3AArXFR/sAOxAL2L0CyAMrgC9QoF1TdovuYzz5PbZFAfCHtygp2yPvZJR2YNwWvSMlQsq4GjoEb6K8v9+DsBp4EngEu5fhMg35G4ZIBY7+hye/x/AhNZyDS9T773sRfg1M35LBQLC9AuogcL3YCHQCf8XGNh5T5TGBFwo5Xg4aiNTeBXjye4wADPsMXLqXsjFne+IBtwGvHyXvToGXgReB5cCjCI8Bjyt05oUNqVi1oCq880n43evh2H974nt4AQDAwjfZiPzh/4QH3sh5wNeBcSPwBUVqm4WswGr3h4FHEP6B3bS0G0otv00E3Wk49m+xIiEPDy8ANseC3Xubg2ZU+SxwsUCjvgI3WGWMnMI6bELQI+54VJR/oawpGHIm9gaL13n7Pz3ZPbwAqBsLd9diE4wxaht6fEbUBgWHMlNQ6U0M6v8mulHWqPQJ2D0msCKCdSiFYt4uQINAQeGwf3nCe3gBMCT40xu1SM4M8H7gIonFBAZiEVT5zkaFVdiqvb84wi8HXjTwcsHuH9J7jVwjpPLwDr9k5+EFwJbDA2+wZsBnn4SvvoGDBFqBE7Hr9QOG2oDdf4DH3fGYCI+rsqqzkfWTe/q+lcOehGWvh4N8wM7DC4BXFn9+o40JRAopZWwE7wDOAY4AXk3ttOEQ678/hw3YPQ48hvA3hNVRSLfErhAodDXCsX/1ATsPLwBGBBbtpqRz1vRGIYImA7sDhwNvxf73q7ArBiF2Df554F+4dXhV/q2wzkBOY4SXwF7zbT5g5+EFwMjGA29UImO7CBdvOFICEcaK3d0rBajYjX66TY6NhXQprUeBqAEkD4c/6Qnv4TGqBEAfYbCbEiqkTZmbF1dfr5AK7a69Bz/tCe/h4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eExlPh/ikyttTKpFSYAAAAASUVORK5CYII='


class Editor:

    def __init__(self):
        self.__name = "ExtremEditor"
        self.__version = "0.5"
        self.__author = "TomFox"
        self.__title = f'{self.__name} v{self.__version} by {self.__author}'
        self.__PrimaryColor = fg("#C71585")
        self.__SecondaryColor = fg("#F5FAFA")
        self.__message = "If you have any idea for new methods contact me"
        self.__ico = f"""
                         {self.__SecondaryColor} ______      _                     {self.__PrimaryColor} ______    _ _ _
                         {self.__SecondaryColor}|  ____|    | |                    {self.__PrimaryColor}|  ____|  | (_) |
                         {self.__SecondaryColor}| |__  __  _| |_ _ __ ___ _ __ ___ {self.__PrimaryColor}| |__   __| |_| |_ ___  _ __
                         {self.__SecondaryColor}|  __| \ \/ / __| '__/ _ \ '_ ` _ \\{self.__PrimaryColor}|  __| / _` | | __/ _ \| '__|
                         {self.__SecondaryColor}| |____ >  <| |_| | |  __/ | | | | {self.__PrimaryColor}| |___| (_| | | || (_) | |
                         {self.__SecondaryColor}|______/_/\_\\\__|_|  \___|_| |_| |_{self.__PrimaryColor}|______\__,_|_|\__\___/|_|

                                              {self.__PrimaryColor}  [Version {self.__version}]"""
        self.__domain = ['@gmail.com', '@yahoo.com', '@hotmail.com']
        self.menu()

    def menu(self):
        try:
            os.mkdir("Output")
        except FileExistsError:
            pass
        os.system(f'title {self.__title}')
        os.system('cls')
        Focus(self.__title)
        methods = sorted([eval(f'Editor.{a}.__doc__') + '|' + a for a in dir(self) if not a.startswith('_') and eval(f'Editor.{a}.__doc__') is not None])
        print(f'{self.__ico}\n\n{fg("#8B0000")} > {fg("#303030")} {self.__message}\n')
        print('\n'.join([f'{self.__SecondaryColor}[{self.__PrimaryColor}{methods.index(b) + 1}{self.__SecondaryColor}] {b.split("|")[0][1:]}' for b in methods]))
        print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
        choice = msvcrt.getch()
        root = tk.Tk()
        root.withdraw()
        with open('tmp.ico', 'wb') as tmp:
            tmp.write(base64.b64decode(Icon().img))
        root.iconbitmap('tmp.ico')
        os.remove('tmp.ico')
        try:
            eval(f'self.{methods[int(choice.decode()) - 1].split("|")[1]}()')
        except:
            self.menu()

    def Duplicate(self):
        """1Remove Duplicate"""
        path = filedialog.askopenfilename()
        open(f'Output/{path.split("/")[-1][:-4]}_Nodup.txt', 'a').write('\n'.join(list(set(open(path, 'r', errors="ignore").read().split('\n'))))[1:])
        self.menu()

    def Shuffle(self):
        """2Shuffle a Combolist"""
        path = filedialog.askopenfilename()
        lines = open(path, 'r', errors="ignore").read().split('\n')
        random.shuffle(lines)
        open(f'Output/{path.split("/")[-1][:-4]}_Shuffled.txt', 'w').write('\n'.join(list(set(lines))))
        self.menu()

    def MailUser(self):
        """3Mail to User / User to Mail"""
        os.system('cls')
        Focus(self.__title)
        methods = ['Mail to User', 'User to Mail', 'Back']
        print(f'{self.__ico}\n\n{fg("#8B0000")} > {fg("#303030")} {self.__message}\n')
        print('\n'.join([f'{self.__SecondaryColor}[{self.__PrimaryColor}{methods.index(b) + 1}{self.__SecondaryColor}] {b.split("|")[0]}' for b in methods]))
        print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
        choice = msvcrt.getch()
        if choice == b"1":
            path = filedialog.askopenfilename()
            open(f'Output/{path.split("/")[-1][:-4]}_MailToUser.txt', 'a').write(
                "\n".join([a[:a.index('@')] + a[a.index(':'):] for a in open(path, 'r', errors="ignore").read().split('\n') if "@" in a and ":" in a]))
            self.MailUser()
        if choice == b"2":
            path = filedialog.askopenfilename()
            open(f'Output/{path.split("/")[-1][:-4]}_UserToMail.txt', 'a').write(
                "\n".join(
                    [a[:a.index(':')] + random.choice(self.__domain) + a[a.index(':'):] for a in open(path, 'r', errors="ignore").read().split('\n')
                     if
                     ":" in a]))
            self.MailUser()
        if choice == b"3":
            self.menu()

    def DomainSorter(self):
        """4Email Sorter/Extractor"""
        os.system('cls')
        Focus(self.__title)
        methods = ['Email Sorter (Give you all email domain in your list)', 'Extract a specific email domain', 'Back']
        print(f'{self.__ico}\n\n{fg("#8B0000")} > {fg("#303030")} {self.__message}\n')
        print('\n'.join([f'{self.__SecondaryColor}[{self.__PrimaryColor}{methods.index(b) + 1}{self.__SecondaryColor}] {b.split("|")[0]}' for b in methods]))
        print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
        choice = msvcrt.getch()
        if choice == b"2":
            path = filedialog.askopenfilename()
            Focus(self.__title)
            domain = input('Domain to sort (ex @gmail) ? ')
            open(f'Output/{path.split("/")[-1][:-4]}_domain' + ".txt", 'a').write("\n".join([a for a in open(path, 'r', errors="ignore").read().split('\n') if domain in a]))
            self.DomainSorter()
        if choice == b"3":
            self.menu()
        if choice == b"1":
            os.system('cls')
            print(f'{self.__ico}\n\n{fg("#8B0000")} > {fg("#303030")}This method can take time for +10M combolist !\n')
            path = filedialog.askopenfilename()
            b = [b[b.index('@'):b.index(':')] for b in open(path, 'r', errors="ignore").read().split('\n') if "@" in b and ":" in b]
            tempdic = {a: 0 for a in list(set(b))}
            for domain in b:
                tempdic[domain] += 1
            domain = list(sorted(tempdic.items(), reverse=True, key=lambda item: item[1]))
            maxlen = max([len(a[0] + str(a[1])) for a in domain[:49]])
            listmail = ["{} -> {}".format(a[0], a[1]) + " " * (maxlen - len(a[0] + str(a[1]))) + " |" for a in domain[:49]]
            if len(domain) > 49:
                print(f'{self.__SecondaryColor}' + '\n'.join([f' {listmail[i]} {listmail[i + 12]} {listmail[i + 24]} {listmail[i + 36][:-1]}' for i in range(12)]))
            elif len(domain) > 37:
                print(f'{self.__SecondaryColor}' + '\n'.join([f' {listmail[i]} {listmail[i + 12]} {listmail[i + 24][:-1]}' for i in range(12)]))
            elif len(domain) > 25:
                print(f'{self.__SecondaryColor}' + '\n'.join([f' {listmail[i]} {listmail[i + 12][:-1]}' for i in range(12)]))
            elif len(domain) > 13:
                print(f'{self.__SecondaryColor}' + '\n'.join([f' {listmail[i][:-1]}' for i in range(12)]))
            else:
                print(f'{self.__SecondaryColor}' + '\n'.join([f' {a[:-1]}' for a in listmail]))
            Focus(self.__title)
            del tempdic, b
            print(f'\n{self.__SecondaryColor}[{self.__PrimaryColor}1{self.__SecondaryColor}] Extract All')
            print(f'{self.__SecondaryColor}[{self.__PrimaryColor}2{self.__SecondaryColor}] Back')
            print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
            choice = msvcrt.getch()

            def CreateTexts(domain):
                open(f"{path.split('/')[-1][:-4]}/{domain[0]}.txt", 'a').write("\n".join([a for a in open(path, 'r', errors="ignore").read().split('\n') if domain[0] in a]))

            if choice == b"1":
                try:
                    os.mkdir(path.split('/')[-1][:-4])
                except FileExistsError:
                    pass
                for dom in domain[:49]:
                    threading.Thread(target=CreateTexts, args=[dom]).start()
                self.DomainSorter()
            if choice == b"2":
                self.DomainSorter()

    def Combiner(self):
        """5Combine multiple .txt to one"""
        path = filedialog.askopenfilenames()
        open(f'Output/{path.split("/")[-1][:-4]}_CombinedCombo.txt', "a").write("".join([open(a, 'r', errors="ignore").read().replace("\n\n", "\n") for a in path]))
        self.menu()

    def UpperLowerFirst(self):
        """6Uppercase/Lowercase First Character In Password"""
        os.system('cls')
        methods = ['Uppercase First Character In Password', 'Lowercase First Character In Password', 'Back']
        print(f'{self.__ico}\n\n{fg("#8B0000")} > {fg("#303030")} {self.__message}\n')
        print('\n'.join([f'{self.__SecondaryColor}[{self.__PrimaryColor}{methods.index(b) + 1}{self.__SecondaryColor}] {b.split("|")[0]}' for b in methods]))
        print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
        choice = msvcrt.getch()
        if choice == b"1":
            path = filedialog.askopenfilename()
            open(f'Output/{path.split("/")[-1][:-4]}_UpperFirst.txt', 'a').write(
                "\n".join([a[:a.index(':') + 1] + a[a.index(':') + 1].upper() + a[a.index(':') + 2:] for a in open(path, 'r', errors="ignore").read().split('\n') if ":" in a]))
            self.UpperLowerFirst()
        if choice == b"2":
            path = filedialog.askopenfilename()
            open(f'Output/{path.split("/")[-1][:-4]}_LowerFirst.txt', 'a').write(
                "\n".join([a[:a.index(':') + 1] + a[a.index(':') + 1].lower() + a[a.index(':') + 2:] for a in open(path, 'r', errors="ignore").read().split('\n') if ":" in a]))
            self.UpperLowerFirst()
        if choice == b"3":
            self.menu()
        else:
            self.UpperLowerFirst()
