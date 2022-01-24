import base64
import os
import random
import threading
import tkinter as tk
from tkinter import filedialog
from colored import fg


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
        if os.name == 'nt':
            os.system(f'title {self.__title}')
        self.Clear()
        methods = sorted([eval(f'Editor.{a}.__doc__') + '|' + a for a in dir(self) if not a.startswith('_') and eval(f'Editor.{a}.__doc__') is not None])
        print(f'{self.__ico}\n\n{fg("#8B0000")} > {fg("#303030")} {self.__message}\n')
        print('\n'.join([f'{self.__SecondaryColor}[{self.__PrimaryColor}{methods.index(b) + 1}{self.__SecondaryColor}] {b.split("|")[0][1:]}' for b in methods]))
        print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
        choice = input()
        root = tk.Tk()
        root.withdraw()
        try:
            eval(f'self.{methods[int(choice) - 1].split("|")[1]}()')
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
        self.Clear()
        methods = ['Mail to User', 'User to Mail', 'Back']
        print(f'{self.__ico}\n\n{fg("#8B0000")} > {fg("#303030")} {self.__message}\n')
        print('\n'.join([f'{self.__SecondaryColor}[{self.__PrimaryColor}{methods.index(b) + 1}{self.__SecondaryColor}] {b.split("|")[0]}' for b in methods]))
        print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
        choice = input()
        if choice == "1":
            path = filedialog.askopenfilename()
            open(f'Output/{path.split("/")[-1][:-4]}_MailToUser.txt', 'a').write(
                "\n".join([a[:a.index('@')] + a[a.index(':'):] for a in open(path, 'r', errors="ignore").read().split('\n') if "@" in a and ":" in a]))
            self.MailUser()
        if choice == "2":
            path = filedialog.askopenfilename()
            open(f'Output/{path.split("/")[-1][:-4]}_UserToMail.txt', 'a').write(
                "\n".join(
                    [a[:a.index(':')] + random.choice(self.__domain) + a[a.index(':'):] for a in open(path, 'r', errors="ignore").read().split('\n')
                     if
                     ":" in a]))
            self.MailUser()
        if choice == "3":
            self.menu()


    def DomainSorter(self):
        """4Email Sorter/Extractor"""
        self.Clear()
        methods = ['Email Sorter (Give you all email domain in your list)', 'Extract a specific email domain', 'Back']
        print(f'{self.__ico}\n\n{fg("#8B0000")} > {fg("#303030")} {self.__message}\n')
        print('\n'.join([f'{self.__SecondaryColor}[{self.__PrimaryColor}{methods.index(b) + 1}{self.__SecondaryColor}] {b.split("|")[0]}' for b in methods]))
        print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
        choice = input()
        if choice == "2":
            path = filedialog.askopenfilename()
            domain = input('Domain to sort (ex @gmail) ? ')
            open(f'Output/{path.split("/")[-1][:-4]}_domain' + ".txt", 'a').write("\n".join([a for a in open(path, 'r', errors="ignore").read().split('\n') if domain in a]))
            self.DomainSorter()
        if choice == "3":
            self.menu()
        if choice == "1":
            self.Clear()
            print(f'{self.__ico}\n\n{fg("00FF00")} > {fg("00FF00")}This method can take time for +10M combolist !\n')
            print(f'{self.__ico}\n\n{fg("00FF00")} > {fg("00FF00")}Improved by i6c! Added multiple files support.\n')
            path = filedialog.askopenfilenames()
            for filename in path:
                b = [b[b.index('@'):b.index(':')] for b in open(filename, 'r', errors="ignore").read().split('\n') if "@" in b and ":" in b]
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
            del tempdic, b
            print(f'\n{self.__SecondaryColor}[{self.__PrimaryColor}1{self.__SecondaryColor}] Extract All')
            print(f'{self.__SecondaryColor}[{self.__PrimaryColor}2{self.__SecondaryColor}] Back')
            print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
            choice = input()

            def CreateTexts(domain):
                open(f'{filename.split("/")[-1][:-4]}_{domain[0]}.txt', 'a').write("\n".join([a for a in open(filename, 'r', errors="ignore").read().split('\n') if domain[0] in a]))

            if choice == "1":
                try:
                    os.mkdir(filename.split('/')[-1][:-4])
                except FileExistsError:
                    pass
                for dom in domain[:49]:
                    threading.Thread(target=CreateTexts, args=[dom]).start()
                self.DomainSorter()
            if choice == "2":
                self.DomainSorter()


    def Combiner(self):
        """5Combine multiple .txt to one"""
        path = filedialog.askopenfilenames()
        open(f'Output/{path.split("/")[-1][:-4]}_CombinedCombo.txt', "a").write("".join([open(a, 'r', errors="ignore").read().replace("\n\n", "\n") for a in path]))
        self.menu()


    def UpperLowerFirst(self):
        """6Uppercase/Lowercase First Character In Password"""
        self.Clear()
        methods = ['Uppercase First Character In Password', 'Lowercase First Character In Password', 'Back']
        print(f'{self.__ico}\n\n{fg("#8B0000")} > {fg("#303030")} {self.__message}\n')
        print('\n'.join([f'{self.__SecondaryColor}[{self.__PrimaryColor}{methods.index(b) + 1}{self.__SecondaryColor}] {b.split("|")[0]}' for b in methods]))
        print(f'{self.__PrimaryColor}\nroot@extrem{self.__SecondaryColor}# ', end="")
        choice = input()
        if choice == "1":
            path = filedialog.askopenfilename()
            open(f'Output/{path.split("/")[-1][:-4]}_UpperFirst.txt', 'a').write(
                "\n".join([a[:a.index(':') + 1] + a[a.index(':') + 1].upper() + a[a.index(':') + 2:] for a in open(path, 'r', errors="ignore").read().split('\n') if ":" in a]))
            self.UpperLowerFirst()
        if choice == "2":
            path = filedialog.askopenfilename()
            open(f'Output/{path.split("/")[-1][:-4]}_LowerFirst.txt', 'a').write(
                "\n".join([a[:a.index(':') + 1] + a[a.index(':') + 1].lower() + a[a.index(':') + 2:] for a in open(path, 'r', errors="ignore").read().split('\n') if ":" in a]))
            self.UpperLowerFirst()
        if choice == "3":
            self.menu()
        else:
            self.UpperLowerFirst()


    def Clear(self):
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")


if __name__ == '__main__':
    editor = Editor()
