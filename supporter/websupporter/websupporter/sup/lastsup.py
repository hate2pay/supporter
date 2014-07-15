#!/usr/lib/python3.3
import telnetlib
from tkinter import *

class Application(Frame):
    
    def __init__(self, master):
        """ Запускает рамку """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ Создает кнопки для работы с программой """
        # создает инструкцию
        self.logoimage = PhotoImage(file = "logo3.gif", width = 225, height = 118)
        Label(self,
              text = "Введите данные абонента, и выберите один из тестов для проверки!", font = "helvetica 14 bold italic underline", relief = "flat", foreground = "red"
              ).grid(row = 0, column = 0, columnspan = 10, sticky = N)

        # создает строку для ввода IP коммутатора и его порта
        Label(self,
              text = "<---  IP/порт коммутатора", font = "timesnewroman 12 bold", height = 1, relief = "flat"
              ).grid(row = 1, column = 3, sticky = "ws")
        self.person_ent = Entry(self, bg = "#FFE4C4")
        self.person_ent.grid(row = 1, column = 2, sticky = "ws")

        # создает строку для ввода IP абонента
        Label(self,
              text = "<---  IP абонента", font = "timesnewroman 12 bold", height = 1, relief = "flat"
              ).grid(row = 2, column = 3, sticky = "wn")
        self.noun_ent = Entry(self, bg = "#FFE4C4")
        self.noun_ent.grid(row = 2, column = 2, sticky = "wn")
   
        # создает галочку подробностей
        self.details = BooleanVar()
        Checkbutton(self,
                    text = "Показать вывод коммутатора ", font = "timesnewroman 10 italic", height = 1, relief = "flat",
                    variable = self.details
                    ).grid(row = 3, column = 2, columnspan = 3, sticky = "w")

        Label(self,
              text = "by hate2pay", font = "timesnewroman 8 bold", height = 1, relief = "flat", foreground = "darkcyan"
              ).grid(row = 3, column = 8, sticky = "e")


        # создает кнопку 1
        self.btn1 = Button(self,
                           text = "Проверить целостность кабеля  ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.cablediag, relief = "solid"
                           ).grid(row = 7, column = 0)

        # создает кнопку 2
        self.btn2 = Button(self,
                           text = "              Проверить Link                ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.errortest, relief = "solid"
                           ).grid(row = 6, column = 0)

        # создает кнопку 3
        self.btn3 = Button(self,
                           text = "            Проверить MAC                 ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.mactest, relief = "solid"
                           ).grid(row = 8, column = 0)

        # создает кнопку 4
        self.btn4 = Button(self,
                           text = "      Проверить получен ли IP       ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.iptest, relief = "solid"
                           ).grid(row = 9, column = 0)

        # создает кнопку 5
        self.btn5 = Button(self,
                           text = "   Проверить состояние порта     ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.looptest, relief = "solid"
                           ).grid(row = 10, column = 0)

        # создает кнопку 6
        self.btn6 = Button(self,
                           text = "               Включить порт               ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.portactivate, relief = "solid"
                           ).grid(row = 11, column = 0)

        # создает кнопку 7
        self.btn7 = Button(self,
                           text = "Узнать сведения о коммутаторе ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.sysinfo, relief = "solid"
                           ).grid(row = 12, column = 0)

        # создает кнопку 8
        self.btn8 = Button(self,
                           text = "Посмотреть логи коммутатора  ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.showlog, relief = "solid"
                           ).grid(row = 13, column = 0)

        # создает кнопку 9
        self.btn9 = Button(self,
                           text = "Посмотреть количество каналов  ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.showprofile, relief = "solid"
                           ).grid(row = 14, column = 0)

        # создает кнопку-заглушку
        self.btn10 = Button(self,
                           text = "Посмотреть количество каналов  ", width = 25, height = 2, bg = "#33B5E5", fg = "black", font = "timesnewroman 12",
                           command = self.showprofile, relief = "solid"
                           )#.grid(row = 5, column = 0)
    
        # создаёт основное текстовое поле
        self.main_text = Text(self, width = 100, height = 35, wrap = WORD, relief = "solid", bg = "#FFE4C4")
        self.main_text.grid(column = 1, row = 4, columnspan = 8, rowspan = 14, sticky = "N")

        # создаёт полосу прокрутки
        scr = Scrollbar(self, command = self.main_text.yview, relief = "solid")
        self.main_text.configure(yscrollcommand=scr.set)
        scr.grid(column = 9, row = 4, rowspan = 14, sticky = N)

        #Вставка логотипа
        Label(self, image = self.logoimage, relief = "flat").grid(column = 0, row = 1, columnspan = 2, rowspan = 3, sticky = "NW")
        #cv = Canvas(self, width = 100, height = 35).grid(column = 1, row = 3, columnspan = 6, rowspan = 14, sticky = S)
        #cv.create_image(image = logoimage, anchor = top)
        
        #Переключатель производителей оборудования
        self.switcher = StringVar()
        self.switcher.set("1")
        Radiobutton(self, text = "ZyXEL", variable = self.switcher, value = "1").grid(row = 3, column = 3, columnspan = 3, sticky = "e")
        Radiobutton(self, text = "Edge-Core", variable = self.switcher, value = "2").grid(row = 3, column = 6, columnspan = 3, sticky = "w")

    def printtext(self, text):

        self.main_text.delete(0.0, END)
        self.main_text.insert(0.0, text)
        return None

    def cablediag(self):
        """ Формирует информацию для вывода"""
        # получает данные из пользовательского ввода
        person = self.person_ent.get()


        host = None
        err = False
        try:
            b = []
            b = person.split("/")
            host = b[0]
            iface = b[1]
            i = int(iface)
            if i > 28:
                err = True
                story = "Нет такого порта!"
        except:
            story = "Ввод неверен, повторите ввод!"
            err = True
        if err:
            story = story + " Введите корректный номер порта!"

        else:
            if host:    
                user = "admin"
                password = "MsgPvvF03"
                password1 = "TFRjhx6224"
                password2 = "omgMs69F"
                password3 = "omgMs69F"
                global tn
                try:
                    tn = telnetlib.Telnet(host, 23, 2)
                except:
                    story = "Заданный IP недоступен, проверьте правильность ввода!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None


                if self.switcher.get() == "1":
                    model_check = tn.read_until(b"User name: ", 1)
                    if "Username" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора!, Выберите Edge-core!")
                        return None
                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"cable-diagnostics " + iface.encode('ascii') + b"\r\n")
                    info = tn.read_until(b"# ").decode('ascii')
                    if "Port" in info:
                        start = info.find("Port")
                    else:
                        start = info.find("port")
                    info = info[start:]
                    lines = info.splitlines()
                    del lines[len(lines) - 1]
                    info = "\n".join(lines)
                    a = info.count("Ok")
                    b = info.count("Open")
                    c = info.count("Short")
                    if a == 2:
                        story = "Кабель, исправен и вставлен в устройство!"
                    elif b == 2:
                        story = "Кабель не вставлен либо компьютер выключен!"
                    elif c != 0:
                        story = "Кабель поврежден!"
                    elif b == 1 or a == 1:
                        story = "Кабель поврежден либо сломана грозозащита"
                    else:
                        story = "Невозможно проверить, возможно порт выключен либо поврежден, обратитесь за помощью к администратору! "

                    if self.details.get():
                        story = story + "\n" + info
                    tn.write(b"exit\r\n")
                else:
                    story = "Тест кабеля Edge-Core: \n\n"
                    model_check = tn.read_until(b"Username: ", 1)
                    if "User name" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора! Выберите ZyXEL!")
                        return None

                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password2.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(user.encode('ascii') + b"\r\n")
                        tn.read_until(b"Password: ")
                        tn.write(password3.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1).decode('ascii')
                    tn.write(b"test cable-diagnostics interface ethernet 1/" + iface.encode('ascii') + b"\r\n")
                    tn.read_until(b"#  ", 8).decode('ascii')
                    tn.write(b"show cable-diagnostics interface ethernet 1/" + iface.encode('ascii') + b"\r\n")
                    info = tn.read_until(b"#").decode('ascii')
                    lines = info.splitlines()
                    info = "\n".join(lines)
                    if "Port" in info:
                        start = info.find("Port")
                    else:
                        start = info.find("port")
                    info = info[start:]
                    lines = info.splitlines()
                    del lines[len(lines) - 1]
                    info = "\n".join(lines)
                    a = info.count("OK")
                    b = info.count("Open")
                    c = info.count("No cable")
                    if a == 2:
                        story = story + "Кабель, исправен и вставлен в устройство!"
                    elif b == 2:
                        story = story + "Кабель не вставлен либо компьютер выключен! Смотрите подробный вывод коммутатора! "
                    elif c != 0:
                        story = story + "В этот порт не вставлен кабель!"
                    elif b == 1 or a == 1:
                        story = story + "Кабель поврежден либо режим работы устройств не 'Full-Duplex'"
                    else:
                        story = story + "Невозможно проверить, возможно порт выключен либо поврежден, смотрите подробный вывод коммутатора! "

                    if info == "":
                        story = "Неудалось проверить, скорее всего данный коммутатор не поддерживает функцию диагностики кабеля =("

                    if self.details.get():
                        story = story + "\n\n\n" + info
                    tn.write(b"exit\r\n")
        
        # выводит результат на экран                                
        self.printtext(story) #self.main_text.delete(0.0, END)
        #self.main_text.insert(0.0, story)
        
    def mactest(self):
        
        """ Формирует информацию для вывода"""
        # получает данные из пользовательского ввода
        person = self.person_ent.get()

        host = None
        err = False
        try:
            b = []
            b = person.split("/")
            host = b[0]
            iface = b[1]
            i = int(iface)
            if i > 28:
                err = True
                story = "Нет такого порта!"
        except:
            story = "Ввод неверен, повторите ввод!"
            err = True
        if err:
            story = story + " Введите корректный номер порта!"

        else:
            if host:    
                user = "admin"
                password = "MsgPvvF03"
                password1 = "TFRjhx6224"
                password2 = "omgMs69F"

                global tn
                try:
                    tn = telnetlib.Telnet(host, 23, 2)
                except:
                    story = "Заданный IP недоступен, проверьте правильность ввода!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None
                if self.switcher.get() == "1":
                    model_check = tn.read_until(b"User name: ", 1)
                    if "Username" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора!, Выберите Edge-core!")
                        return None
                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show mac address-table port " + iface.encode('ascii') + b"\r\n")
                    file2 = tn.read_until(b"# ").decode('ascii')
                    start = file2.find("Port")
                    file2 = file2[start:]
                    l = file2.splitlines()
                    del l[len(l) - 1]
                    file2 = "\n".join(l)
                    if "Dynamic" in file2:
                        story = "На порту есть cледуюцие MAC адреса: \n"
                        lines = file2.splitlines()
                        for line in lines:
                            word = line.split()
                            if word[0] == iface:
                                story = story + word[2] + "\n"
                    else:
                        story = "MAC адресов на порту нет! "
                        
                    if self.details.get():
                        story = "Детальная информация:" + "\n" + file2
                    tn.write(b"exit\r\n")
	            
                else:
                    story = "Тест кабеля Edge-Core: \n\n"
                    model_check = tn.read_until(b"Username: ", 1)
                    if "User name" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора! Выберите ZyXEL!")
                        return None

                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password2.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show mac-address-table interface ethernet 1/" + iface.encode('ascii') + b"\r\n")
                    file2 = tn.read_until(b"#", 1).decode('ascii')
                    #start = file2.find("Port")
                    #file2 = file2[start:]
                    l = file2.splitlines()
                    del l[0]
                    del l[len(l) - 1]
                    file2 = "\n".join(l)
                    #if "Eth" in file2:
                        #story = "На порту есть cледуюцие MAC адреса: \n"
                        #lines = file2.splitlines()
                        #for line in lines:
                            #word = line.split()
                            #if True: #word[2] == iface:
                                #story = story + word[1] + "\n"
                    #else:
                        #story = "MAC адресов на порту нет! "
                    story = "Список MAC на этом порту: \n" + file2 + "\n\n\n\t\tЕсли MAC нет, проведите другой тест и повторите попытку еще раз!"

                    if self.details.get():
                        story = "Детальная информация:" + "\n" + file2 + "\n\n\n\t\tЕсли MAC нет, проведите другой тест и повторите попытку еще раз!"
                    tn.write(b"exit\r\n")                          



        
        # выводит результат на экран                                
        self.main_text.delete(0.0, END)
        self.main_text.insert(0.0, story)

    def errortest(self):

        person = self.person_ent.get()
        host = None
        err = False
        try:
            b = []
            b = person.split("/")
            host = b[0]
            iface = b[1]
            i = int(iface)
            if i > 28:
                err = True
                story = "Нет такого порта!"
        except:
            story = "Ввод неверен, повторите ввод!"
            err = True
        if err:
            story = story + " Введите корректный номер порта!"

        else:
            if host:    
                user = "admin"
                password = "MsgPvvF03"
                password1 = "TFRjhx6224"
                password2 = "omgMs69F"
                global tn
                try:
                    tn = telnetlib.Telnet(host, 23, 2)
                except:
                    story = "Заданный IP недоступен, проверьте правильность ввода!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None
                if self.switcher.get() == "1":
                    model_check = tn.read_until(b"User name: ", 1)
                    if "Username" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора!, Выберите Edge-core!")
                        return None
                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show interfaces " + iface.encode('ascii') + b"\r\n")
                    file = tn.read_until(b"ESC").decode('ascii')
                    tn.write(b"\r\n")
                    tn.write(b"\r\n")
                    start = file.find("Port")
                    file = file[start:]
                    l = file.splitlines()
                    del l[len(l) - 1]
                    file = "\n".join(l)
                    if "STOP" in file:
                        story = "Link отсутствует! \n"
                    elif "FORWARDING" in file:
                        story = "Link есть! \n"
                    lines = file.splitlines()
                    errorsline = lines[6].split(":")
                    if int(errorsline[1]) > 0:
                        story = story + "На порту есть ошибки! Количество: " + errorsline[1]
                    else:
                        story = story + "На порту ошибок нет!"
                    uptimeline = lines[9].split(":")
                    story = story + "\nВремя работы интерфейса: " + uptimeline[1] + " часов " + uptimeline[2] + " минут " + uptimeline[3] + " секунд"
                    if self.details.get():
                        story = "Детальная информация об интерфейсе: " + "\n" + file
                    tn.write(b"exit\r\n")

                else:
                    story = "Тест кабеля Edge-Core: \n\n"
                    model_check = tn.read_until(b"Username: ", 1)
                    if "User name" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора! Выберите ZyXEL!")
                        return None

                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password2.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show interfaces counters ethernet 1/" + iface.encode('ascii') + b"\r\n")
                    if "Zeleniy" not in model_check.decode('ascii'):
                        file = tn.read_until(b"More", 1).decode('ascii')
                        tn.write(b" ")
                        #tn.write(b" ")
                        tn.write(b"\r\n")
                        file2 = tn.read_until(b"#").decode('ascii')
                        start = file.find("Ethernet")
                        end = file.find("---")
                        file = file[start:end]
                        start2 = file2.find("CRC")
                        file2 = file2[start2:]
                        file = file + file2
                        l = file.splitlines()
                        del l[len(l) - 1]
                        file = "\n".join(l)
                    else:
                        file = tn.read_until(b"Others to", 1).decode('ascii')
                        tn.write(b" ")
                        #tn.write(b" ")
                        tn.write(b"A")
                        file2 = tn.read_until(b"#").decode('ascii')
                        start = file.find("Ethernet")
                        end = file.find("---")
                        file = file[start:end]
                        start2 = file2.find("Deferred") - 15
                        end2 = file2.find("64 Octets")
                        file2 = file2[start2:end2]
                        file = file + file2
                        l = file.splitlines()
                        del l[len(l) - 1]
                        file = "\n".join(l)
                    """if "STOP" in file:
                        story = "Link отсутствует! \n"
                    elif "FORWARDING" in file:
                        story = "Link есть! \n"
                    lines = file.splitlines()
                    errorsline = lines[6].split(":")
                    if int(errorsline[1]) > 0:
                        story = story + "На порту есть ошибки! Количество: " + errorsline[1]
                    else:
                        story = story + "На порту ошибок нет!"
                    uptimeline = lines[9].split(":")
                    story = story + "\nВремя работы интерфейса: " + uptimeline[1] + " часов " + uptimeline[2] + " минут " + uptimeline[3] + " секунд"""
                    story = "Счётчики пакетов на интерфейсе: " + "\n" + file
                    if self.details.get():
                        story = "Счётчики пакетов на интерфейсе: " + "\n" + file 
                    tn.write(b"exit\r\n")

            

        self.main_text.delete(0.0, END)
        self.main_text.insert(0.0, story)

    def iptest(self):
        
        """ Формирует информацию для вывода"""
        # получает данные из пользовательского ввода
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        
        host = None
        err = False
        try:
            b = []
            b = person.split("/")
            host = b[0]
            iface = b[1]
            i = int(iface)
            if i > 28:
                err = True
                story = "Нет такого порта!"
        except:
            story = "Ввод неверен, повторите ввод!"
            err = True
        if err:
            story = story + " Введите корректный номер порта!"

        else:
            if host:    
                user = "admin"
                password = "MsgPvvF03"
                password1 = "TFRjhx6224"
                password2 = "omgMs69F"
                global tn
                try:
                    oct = noun.split(".")
                    int(oct[0]) + int(oct[1]) + int(oct[2]) + int(oct[3])
                except:
                    story = "Введите правильный IP для проверки!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None
                try:
                    tn = telnetlib.Telnet(host, 23, 2)
                except:
                    story = "Заданный IP недоступен, проверьте правильность ввода!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None
                if self.switcher.get() == "1":
                    model_check = tn.read_until(b"User name: ", 1)
                    if "Username" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора!, Выберите Edge-core!")
                        return None
                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show dhcp snooping binding " + b"\r\n")
                    file3 = tn.read_until(b"Total", 2).decode('ascii')
                    tn.write(b"\r\n")
                    file2 = tn.read_until(b"Total", 2).decode('ascii')
                    lines = file3.splitlines()
                    lines = lines[2:]
                    lines[0] = "Список полученных адресов: \n"
                    del lines[len(lines) - 1]
                    file3 = "\n".join(lines)
                    #file3 = file3 + lines[0].strip()
                    #del lines[0]
                    #for line in lines[:len(lines) - 1]:
                        #line.strip()
                        #file3 = file3 + line
                    if "172." in file2:
                        cut2 = file2.find(":")
                        file2 = file2[cut2 - 4:]
                        lines = file2.splitlines()
                        file2 = ""
                        for line in lines:
                            file2 = file2 + "\n" + line
                        file3 = file3 + file2
                    if noun in file3:
                        story = "IP получен\n"
                    else:
                        story = "Введенный вами IP не получен!\n"
                        
                    if self.details.get():
                        story = story + file3
                    tn.write(b"exit\r\n")

                else:
                    #story = "Провер Edge-Core: \n\n"
                    model_check = tn.read_until(b"Username: ", 1)
                    if "User name" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора! Выберите ZyXEL!")
                        return None

                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password2.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show ip dhcp snooping binding " + b"\r\n")
                    file3 = tn.read_until(b"#", 2).decode('ascii')
                    #tn.write(b"\r\n")
                    #file2 = tn.read_until(b"Total", 2).decode('ascii')
                    lines = file3.splitlines()
                    #lines = lines[1:]
                    lines[0] = "Список полученных адресов: \n"
                    del lines[len(lines) - 1]
                    file3 = "\n".join(lines)
                    #file3 = file3 + lines[0].strip()
                    #del lines[0]
                    #for line in lines[:len(lines) - 1]:
                        #line.strip()
                        #file3 = file3 + line
                    """if "172." in file2:
                        cut2 = file2.find(":")
                        file2 = file2[cut2 - 4:]
                        lines = file2.splitlines()
                        file2 = ""
                        for line in lines:
                            file2 = file2 + "\n" + line
                        file3 = file3 + file2"""
                    if noun in file3:
                        story = "IP получен\n"
                    else:
                        story = "Введенный вами IP не получен!\n"
                        
                    if self.details.get():
                        story = story + file3
                    tn.write(b"exit\r\n")




        
        # выводит результат на экран                                
        self.main_text.delete(0.0, END)
        self.main_text.insert(0.0, story)

    def looptest(self):

        person = self.person_ent.get()
        host = None
        err = False
        try:
            b = []
            b = person.split("/")
            host = b[0]
            iface = b[1]
            i = int(iface)
            if i > 28:
                err = True
                story = "Нет такого порта!"
        except:
            story = "Ввод неверен, повторите ввод!"
            err = True
        if err:
            story = story + " Введите корректный номер порта!"

        else:
            if host:    
                user = "admin"
                password = "MsgPvvF03"
                password1 = "TFRjhx6224"
                password2 = "omgMs69F"
                global tn
                try:
                    tn = telnetlib.Telnet(host, 23, 2)
                except:
                    story = "Заданный IP недоступен, проверьте правильность ввода!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None

                if self.switcher.get() == "1":
                    model_check = tn.read_until(b"User name: ", 1)
                    if "Username" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора!, Выберите Edge-core!")
                        return None
                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show loopguard " + b"\r\n")
                    file1 = tn.read_until(b"ESC", 1).decode('ascii')
                    tn.write(b"\r\n")
                    file2 = tn.read_until(b"ESC", 1).decode('ascii')
                    tn.write(b"\r\n")
                    file3 = tn.read_until(b"ESC", 1).decode('ascii')
                    tn.write(b"\r\n")
                    #обработка полученных строк
                    c1 = file2.find("    10")
                    c2 = file2.find("--")
                    file2 = file2[c1:c2]
                    c3 = file1.find("-- more")
                    file1 = file1[:c3]
                    c4 = file3.find("    22")
                    file3 = file3[c4:]
                    file = file1 + file2 + file3
                    start = file.find("Port")
                    file = file[start:]
                    lines = file.splitlines()
                    del lines[len(lines) - 1]
                    file = "\n".join(lines)
                    story = ""
                    for line in lines:
                        words = line.split()
                        if words[0] == iface:
                            if words[1] == "Active":
                                st = "АКТИВЕН"
                            else:
                                st = "НЕАКТИВЕН"
                            if words[2] == "Enable":
                                l = "ВКЛЮЧЕНО"
                            elif words[2] == "Disable":
                                l = "OТКЛЮЧЕНО"
                            else:
                                l = "НЕИЗВЕСТНО"
                            story = "Информация об интерфейсе:\n" + "Порт: " + words[0] + "\nCостояние порта: " + st + "\nСостояние LoopGuard: " + l + "\nКоличество переданных пакетов: " + words[3]
                    if self.details.get():
                        story = "Детальная информация о портах коммутатора: " + "\n" + file
                    tn.write(b"exit\r\n")
            
                else:
                    story = "Тест кабеля Edge-Core: \n\n"
                    model_check = tn.read_until(b"Username: ", 1)
                    if "User name" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора! Выберите ZyXEL!")
                        return None

                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password2.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show interfaces status ethernet 1/" + iface.encode('ascii') + b"\r\n")
                    file1 = tn.read_until(b"[A]", 1).decode('ascii')
                    tn.write(b"A" + b"\r\n")
                    file2 = tn.read_until(b"ESC", 1).decode('ascii')
                    #tn.write(b"\r\n")
                    #file3 = tn.read_until(b"ESC", 1).decode('ascii')
                    #tn.write(b"\r\n")
                    #обработка полученных строк
                    c1 = file1.splitlines()
                    #del c1[len(c1) - 1]
                    del c1[len(c1) - 1]
                    del c1[0]
                    c2 = file2.splitlines()
                    del c2[len(c2) - 1]
                    del c2[len(c2) - 1]
                    #del c2[0]
                    #c3 = file1.find("-- more")
                    #file1 = file1[:c3]
                    #c4 = file3.find("    22")
                    #file3 = file3[c4:]
                    file1 = "\n".join(c1)
                    file2 = "\n".join(c2)
                    if "Operation" in file2:
                        start = file2.find("Operation")
                        file2 = file2[start:]
                    else:
                        start = file2.find("Flow")
                        file2 = file2[start:]
                    file = file1 + "\n" + file2
                    story = file
                    """start = file.find("Port")
                    file = file[start:]
                    lines = file.splitlines()
                    del lines[len(lines) - 1]
                    file = "\n".join(lines)
                    story = ""
                    for line in lines:
                        words = line.split()
                        if words[0] == iface:
                            if words[1] == "Active":
                                st = "АКТИВЕН"
                            else:
                                st = "НЕАКТИВЕН"
                            if words[2] == "Enable":
                                l = "ВКЛЮЧЕНО"
                            elif words[2] == "Disable":
                                l = "OТКЛЮЧЕНО"
                            else:
                                l = "НЕИЗВЕСТНО"
                            story = "Информация об интерфейсе:\n" + "Порт: " + words[0] + "\nCостояние порта: " + st + "\nСостояние LoopGuard: " + l + "\nКоличество переданных пакетов: " + words[3]"""
                    story = "Детальная информация о состоянии порта: " + "\n  " + file
                    if self.details.get():
                        story = "Детальная информация о состоянии порта: " + "\n  " + file
                    tn.write(b"exit\r\n")                           

        self.main_text.delete(0.0, END)
        self.main_text.insert(0.0, story)

    def portactivate(self):

        person = self.person_ent.get()
        host = None
        err = False
        try:
            b = []
            b = person.split("/")
            host = b[0]
            iface = b[1]
            i = int(iface)
            if i > 28:
                err = True
                story = "Нет такого порта!"
        except:
            story = "Ввод неверен, повторите ввод!"
            err = True
        if err:
            story = story + " Введите корректный номер порта!"

        else:
            if host:    
                user = "admin"
                password = "MsgPvvF03"
                password1 = "TFRjhx6224"
                password2 = "omgMs69F"
                global tn
                try:
                    tn = telnetlib.Telnet(host, 23, 2)
                except:
                    story = "Заданный IP недоступен, проверьте правильность ввода!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None
                if self.switcher.get() == "1":
                    model_check = tn.read_until(b"User name: ", 1)
                    if "Username" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора!, Выберите Edge-core!")
                        return None
                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"configure terminal " + b"\r\n")
                    tn.read_until(b"(config)# ", 1).decode('ascii')
                    tn.write(b"interface port-channel "+ iface.encode('ascii') + b"\r\n")
                    tn.read_until(b"interface)#", 1).decode('ascii')
                    tn.write(b"no inactive "+ b"\r\n")
                    tn.read_until(b"interface)#", 1).decode('ascii')
                    tn.write(b"exit " + b"\r\n")
                    tn.read_until(b"(config)# ", 1).decode('ascii')
                    tn.write(b"exit " + b"\r\n")
                    tn.read_until(b"# ", 1).decode('ascii')
                    tn.write(b"write memory " + b"\r\n")
                    tn.read_until(b"# ", 10).decode('ascii')
                    story = "Введенный порт АКТИВЕН! "
                    if self.details.get():
                        story = story + "\nПодробную информацию о портах можно узнать, если нажать кнопку -Проверить состояние порта-"
                    tn.write(b"exit\r\n")
            
                else:
                    story = "Тест кабеля Edge-Core: \n\n"
                    model_check = tn.read_until(b"Username: ", 1)
                    if "User name" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора! Выберите ZyXEL!")
                        return None

                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password2.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"configure " + b"\r\n")
                    tn.read_until(b"(config)# ", 1).decode('ascii')
                    tn.write(b"interface ethernet 1/"+ iface.encode('ascii') + b"\r\n")
                    story = tn.read_until(b"config-if)#", 1).decode('ascii')
                    tn.write(b"no shutdown "+ b"\r\n")
                    story = story + tn.read_until(b"config-if)#", 1).decode('ascii')
                    tn.write(b"exit " + b"\r\n")
                    story = story + tn.read_until(b"(config)# ", 1).decode('ascii')
                    tn.write(b"exit " + b"\r\n")
                    story = story + tn.read_until(b"# ", 1).decode('ascii')
                    tn.write(b"copy running-config startup-config " + b"\r")
                    story = story + tn.read_until(b"Startup ", 10).decode('ascii')
                    tn.write(b"\r\n")
                    f = tn.read_until(b"#", 10).decode('ascii')
                    tn.write(b"exit " + b"\r\n")
                    story = "Введенный порт АКТИВЕН! "
                    if self.details.get():
                        story = story + "\nПодробную информацию о портах можно узнать, если нажать кнопку -Проверить состояние порта-" + "\n" + f
                    tn.write(b"exit\r\n")                              

        self.main_text.delete(0.0, END)
        self.main_text.insert(0.0, story)

    def sysinfo(self):

        person = self.person_ent.get()
        host = None
        err = False
        try:
            b = []
            b = person.split("/")
            host = b[0]
            iface = b[1]
            i = int(iface)
            if i > 28:
                err = True
                story = "Нет такого порта!"
        except:
            story = "Ввод неверен, повторите ввод!"
            err = True
        if err:
            story = story + " Введите корректный номер порта!"

        else:
            if host:    
                user = "admin"
                password = "MsgPvvF03"
                password1 = "TFRjhx6224"
                password2 = "omgMs69F"
                global tn
                try:
                    tn = telnetlib.Telnet(host, 23, 2)
                except:
                    story = "Заданный IP недоступен, проверьте правильность ввода!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None
                
                if self.switcher.get() == "1":
                    model_check = tn.read_until(b"User name: ", 1)
                    if "Username" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора!, Выберите Edge-core!")
                        return None
                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show system-information " + b"\r\n")
                    file = tn.read_until(b"# ", 1).decode('ascii')
                    start = file.find("Product")
                    file = file[start:]
                    lines = file.splitlines()
                    del lines[len(lines) - 1]
                    file = "\n".join(lines)
                    info = ""
                    for line in lines:
                        if "Product Model" in line:
                            word1 = line.split(":")
                            info = info + "Модель коммутатора: " + word1[1]
                        if "System Name" in line:
                            word2 = line.split(":")
                            info = info + "\nХостнейм коммутатора: " + word2[1]
                        if "Time" in line:
                            word3 = line.split(":", 1)
                            time = word3[1].split()
                            time1 = time[0].split(":")
                            info = info + "\nВремя работы коммутатора: " + time1[0] + " часов " + time1[1] + " минут " + time1[2] + " секунд"
                        if "Address" in line:
                            word4 = line.split(":", 1)
                            info = info + "\nМАС адрес коммутатора: " + word4[1]
                    story = "Информация о коммутаторе: " + "\n\n\n" + info
                    if self.details.get():
                        story = "Подробный вывод данных о коммутаторе\n\n" + file
                    tn.write(b"exit\r\n")

                else:
                    story = "Тест кабеля Edge-Core: \n\n"
                    model_check = tn.read_until(b"Username: ", 1)
                    if "User name" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора! Выберите ZyXEL!")
                        return None

                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password2.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show system " + b"\r\n")
                    file = tn.read_until(b"#", 1).decode('ascii')
                    lines = file.splitlines()
                    del lines[0]
                    del lines[len(lines) - 1]
                    file = "\n".join(lines)
                    #start = file.find("Product")
                    #file = file[start:]
                    #lines = file.splitlines()
                    #del lines[len(lines) - 1]
                    #file = "\n".join(lines)
                    #info = ""
                    #for line in lines:
                        #if "Product Model" in line:
                            #word1 = line.split(":")
                            #info = info + "Модель коммутатора: " + word1[1]
                        #if "System Name" in line:
                            #word2 = line.split(":")
                            #info = info + "\nХостнейм коммутатора: " + word2[1]
                        #if "Time" in line:
                            #word3 = line.split(":", 1)
                            #time = word3[1].split()
                            #time1 = time[0].split(":")
                            #info = info + "\nВремя работы коммутатора: " + time1[0] + " часов " + time1[1] + " минут " + time1[2] + " секунд"
                        #if "Address" in line:
                            #word4 = line.split(":", 1)
                            #info = info + "\nМАС адрес коммутатора: " + word4[1]
                    story = "Информация о коммутаторе: " + "\n\n\n" + file
                    if self.details.get():
                        story = "Подробный вывод данных о коммутаторе\n\n" + file
                    tn.write(b"exit\r\n")                            

        self.main_text.delete(0.0, END)
        self.main_text.insert(0.0, story)

    def showlog(self):

        person = self.person_ent.get()
        host = None
        err = False
        try:
            b = []
            b = person.split("/")
            host = b[0]
            iface = b[1]
            i = int(iface)
            if i > 28:
                err = True
                story = "Нет такого порта!"
        except:
            story = "Ввод неверен, повторите ввод!"
            err = True
        if err:
            story = story + " Введите корректный номер порта!"

        else:
            if host:    
                user = "admin"
                password = "MsgPvvF03"
                password1 = "TFRjhx6224"
                password2 = "omgMs69F"
                global tn
                try:
                    tn = telnetlib.Telnet(host, 23, 2)
                except:
                    story = "Заданный IP недоступен, проверьте правильность ввода!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None


                if self.switcher.get() == "1":
                    model_check = tn.read_until(b"User name: ", 1)
                    if "Username" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора!, Выберите Edge-core!")
                        return None
                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show logging " + b"\r\n")
                    file = tn.read_until(b"# ", 0.5).decode('ascii')
                    tn.write(b"\r\n")
                    file2 = tn.read_until(b"# ", 4).decode('ascii')
                    cut1 = file.find("   1")
                    cut2 = file.find("--")
                    file = file[cut1:cut2]
                    start2 = file2.find("  20")
                    file2 = file2[start2:]
                    file = file + file2
                    lines = file.splitlines()
                    del lines[len(lines) - 1]
                    file = "\n".join(lines)
                    info = "Лог порта №" + iface + ":\n\n"
                    lines = file.splitlines()
                    for line in lines:
                        if "Port " + iface in line:
                            info = info + "\n" + line
                    story = info
                    if self.details.get():
                        story = "Подробный лог коммутатора\n\n" + file
                    tn.write(b"exit\r\n")

                else:
                    story = "Тест кабеля Edge-Core: \n\n"
                    model_check = tn.read_until(b"Username: ", 1)
                    if "User name" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора! Выберите ZyXEL!")
                        return None

                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password2.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show log ram " + b"\r\n")
                    file = tn.read_until(b"[A]", 0.5).decode('ascii')
                    tn.write(b"A" + b"\r\n")
                    file2 = tn.read_until(b"# ", 4).decode('ascii')
                    cut1 = file.find("---")
                    cut2 = file2.find("level")
                    file = file[:cut1]
                    #start2 = file2.find("  20")
                    file2 = file2[cut2:]
                    file = file + file2
                    lines = file.splitlines()
                    del lines[len(lines) - 1]
                    file = "\n".join(lines)
                    info = "Лог порта №" + iface + ":\n\n"
                    lines = file.splitlines()
                    counter = 0
                    for line in lines:
                        counter += 1
                        if "Port  " + iface in line:
                            info = info + "\n" + lines[counter - 2] + "\n" + line
                    story = info
                    if self.details.get():
                        story = "Подробный лог коммутатора\n\n" + file
                    tn.write(b"exit\r\n")                              

        self.main_text.delete(0.0, END)
        self.main_text.insert(0.0, story)

    def showprofile(self):

        URLS = {'239.192.2.33': 'CBS Drama', '239.192.2.31': 'КХЛ', '239.192.2.30': 'Киносоюз (НТВ+)', '239.192.4.84': 'History HD', '239.192.2.37': 'TiJi', '239.192.2.36': 'Карусель', '239.192.2.35': 'Disney Channel', '239.192.2.34': 'Euronews', '239.192.2.39': 'Jim Jam', '239.192.2.38': 'Nickelodeon', '239.192.4.99': 'HD Кино 2', '239.192.4.98': 'Спорт 1 HD (Россия)', '239.192.4.97': 'MGM HD', '239.192.4.96': 'Viasat Nature/History HD', '239.192.4.95': 'TV1000 Megahit HD', '239.192.4.94': 'TV1000 Premium HD', '239.192.4.93': 'TV1000 Comedy HD', '239.192.4.92': 'Россия HD', '239.192.4.91': 'Первый канал HD (Россия)', '239.192.4.90': 'Охотник и рыболов HD', '239.192.0.48': 'Ukrainian Fashion', '239.192.1.29': 'Телекафе', '239.192.0.40': 'Radio Ukraine     UR2', '239.192.1.24': 'CNN International', '239.192.0.42': 'НТВ Мир', '239.192.0.43': 'Viasat Explorer CEE', '239.192.0.44': 'Viasat History', '239.192.0.45': 'Детский мир', '239.192.1.23': 'CCTV9 (English)', '239.192.1.22': 'Diva Universal', '239.192.3.250': 'Blue Hustler', '239.192.1.3': 'AzTV', '239.192.1.1': 'Парк развлечений', '239.192.1.6': 'RTД (English)', '239.192.1.7': 'STV', '239.192.1.5': 'Amazing Life', '239.192.1.8': 'Комсомольская правда', '239.192.1.9': 'ТДК', '239.192.2.19': 'CBS Reality', '239.192.2.18': 'MGM international', '239.192.0.9': 'ТВi', '239.192.0.8': '2+2', '239.192.0.7': 'UBR', '239.192.2.10': 'Eurosport 2', '239.192.0.5': 'O-TV', '239.192.0.4': '5 канал', '239.192.0.3': 'ICTV', '239.192.0.2': 'НТН', '239.192.0.1': 'Рада', '239.192.0.66': 'Спас', '239.192.0.67': 'News One', '239.192.0.64': 'Здоровое ТВ', '239.192.0.65': 'Ретро', '239.192.0.62': 'Шансон', '239.192.0.63': 'Мир ТВ', '239.192.0.61': 'ТВ Центр Международный', '239.192.0.69': 'Ru.Music', '239.192.1.49': 'English Club TV', '239.192.1.48': 'InterAz', '239.192.1.43': 'Охота и рыбалка', '239.192.1.42': 'Fox Life', '239.192.1.41': 'Fox Crime', '239.192.1.40': 'RT (Espanol)', '239.192.1.47': 'Россия 24', '239.192.1.46': 'Россия К', '239.192.1.45': 'RT (English)', '239.192.1.44': 'Comedy TV', '239.192.1.54': 'TV5 Monde Europe (Francais)', '239.192.1.55': 'RAI News (Italiano)', '239.192.4.20': 'Тонис HD', '239.192.4.21': 'Discovery HD Showcase', '239.192.2.5': 'Интересное ТВ', '239.192.2.7': 'Авто Плюс', '239.192.2.6': 'Боец ТВ', '239.192.2.1': 'Совершенно секретно', '239.192.2.2': 'Дом кино', '239.192.3.138': 'РБК', '239.192.1.53': 'Deutsche Welle', '239.192.1.20': 'BBC World News', '239.192.3.129': 'RU.TV', '239.192.1.60': 'НТА', '239.192.1.63': 'Черное море', '239.192.1.62': 'Право TV', '239.192.1.65': 'Maxxi-TV', '239.192.1.64': 'Культура', '239.192.1.67': 'Союз', '239.192.1.66': 'ATR', '239.192.3.121': 'Наука 2.0', '239.192.1.68': 'Беларусь 24', '239.192.0.47': 'RTVi', '239.192.3.125': 'Кино плюс (НТВ+)', '239.192.3.124': '24 Техно', '239.192.3.126': 'Русский Extreme', '239.192.2.68': 'TV Rus', '239.192.2.69': 'R1', '239.192.2.60': 'Русский иллюзион', '239.192.2.61': 'Еврокино', '239.192.2.62': 'Успех', '239.192.2.63': 'Мужской', '239.192.2.64': 'Загородная жизнь', '239.192.2.65': 'Music Box UA', '239.192.2.66': 'Ностальгия', '239.192.2.67': 'Pro Все', '239.192.3.106': 'Наше новое кино (НТВ+)', '239.192.3.105': 'Киноклуб (НТВ+)', '239.192.3.104': 'Кинохит (НТВ+)', '239.192.3.103': 'Премьера (НТВ+)', '239.192.3.102': 'Universal Channel', '239.192.3.109': 'TV1000 Action East', '239.192.3.108': 'SET (Sony Entertainment)', '239.192.0.28': 'Юнион', '239.192.0.29': 'Интер', '239.192.0.22': 'Новый канал', '239.192.0.23': 'ТРК "Украина"', '239.192.0.20': 'ZOOM', '239.192.0.21': 'Глас', '239.192.0.26': '27 канал (Донецк)', '239.192.0.27': '12 канал (Донецк)', '239.192.0.24': 'УТ-1', '239.192.0.25': 'ТЕТ', '239.192.2.46': 'Усадьба', '239.192.2.44': 'Футбол+', '239.192.2.45': 'Discovery Investigation', '239.192.2.42': 'Спорт 1', '239.192.2.43': 'Спорт 2', '239.192.2.40': 'Gulli', '239.192.2.41': 'Cartoon Network/TCM', '239.192.2.48': 'Домашние животные', '239.192.2.49': 'Наше кино (НТВ+)', '239.192.0.46': 'Наше любимое кино', '239.192.1.10': 'Ля-минор ТВ', '239.192.1.14': 'Домашний', '239.192.0.59': 'Футбол', '239.192.0.58': 'Пiксель TV', '239.192.0.57': 'Enter-фильм', '239.192.0.56': 'Время:далёкое и близкое', '239.192.0.55': 'Первый канал. Всемирная сеть', '239.192.0.54': 'РТР-Планета', '239.192.0.53': 'Discovery Channel', '239.192.0.52': 'Eurosport', '239.192.0.51': 'Animal Planet', '239.192.0.50': 'National Geographic', '239.192.0.15': 'Первый деловой', '239.192.3.139': 'Спорт 1 (Россия)', '239.192.3.248': 'Playboy TV', '239.192.3.249': 'Русская ночь', '239.192.4.85': 'Футбол+ HD', '239.192.4.17': 'HD Кино', '239.192.4.16': 'Animal Planet HD', '239.192.4.15': 'Travel + Adventure HD', '239.192.4.14': 'MTV Live HD', '239.192.4.13': 'Футбол 2 HD (НТВ+)', '239.192.4.12': 'Nat Geo Wild HD', '239.192.4.10': 'Nickelodeon HD', '239.192.4.19': 'Футбол HD (НТВ+)', '239.192.4.18': 'HD Спорт', '239.192.3.18': 'Музыка Первого', '239.192.3.19': 'Travel Channel', '239.192.3.12': 'MTV Hits', '239.192.2.28': 'Иллюзион+', '239.192.2.29': '24 Док', '239.192.2.24': 'Viasat Sport', '239.192.2.27': 'Драйв', '239.192.2.20': 'Extreme Sports', '239.192.0.75': 'НЛО-ТВ', '239.192.0.77': 'Малятко TV', '239.192.0.76': 'Донбасс', '239.192.0.71': 'Погода ТВ', '239.192.0.70': 'Star TV', '239.192.0.73': 'Business', '239.192.0.72': 'Добро ТВ', '239.192.0.79': 'Эко-ТВ', '239.192.0.78': 'Гумор ТБ', '239.192.4.86': 'Outdoor Channel HD', '239.192.4.87': 'Fashion One HD', '239.192.1.61': 'Солнце', '239.192.1.38': 'ZooПарк', '239.192.0.19': 'Мега', '239.192.1.37': 'Shant TV', '239.192.1.32': 'ТНВ планета', '239.192.1.31': 'ТРО', '239.192.3.142': 'История', '239.192.3.141': 'ТВ Центр', '239.192.3.140': '5 канал (Москва)', '239.192.3.120': 'Моя планета', '239.192.0.13': 'M2', '239.192.0.12': 'M1', '239.192.0.11': 'Тонис', '239.192.0.10': 'СТБ', '239.192.0.17': 'К1', '239.192.0.16': 'Киевская Русь (КРТ)', '239.192.1.52': 'Bloomberg (English)', '239.192.0.14': 'News 24', '239.192.3.136': 'Дождь. Optimistic channel', '239.192.3.137': 'Москва 24', '239.192.3.134': 'Звезда', '239.192.0.18': 'К2', '239.192.3.132': 'НТВ', '239.192.1.59': 'Моя дитина', '239.192.3.130': 'Спорт (НТВ+)', '239.192.2.74': 'НСТ (страшное кино)', '239.192.2.73': 'Наш Футбол (НТВ+)', '239.192.2.72': 'Вопросы и ответы', '239.192.2.71': 'Психология 21', '239.192.2.70': '2x2', '239.192.0.84': 'Голдберри', '239.192.0.85': 'Shopping TV', '239.192.0.86': 'Банк ТБ', '239.192.0.87': 'ЦК (КДРТРК)', '239.192.0.80': 'ЧП Инфо', '239.192.0.81': 'Real Estate TV', '239.192.0.82': 'Меню-ТВ', '239.192.0.83': 'Новый город (Донецк)', '239.192.0.6': '1+1', '239.192.3.114': 'TLC', '239.192.3.115': 'Discovery Science', '239.192.3.116': 'Ocean-TV', '239.192.3.117': 'Viasat Nature CEE', '239.192.3.110': 'TV1000 Русское кино', '239.192.3.111': '365 дней ТВ', '239.192.3.112': 'Nat Geo Wild (Россия)', '239.192.3.113': 'Discovery World', '239.192.3.118': 'Russian Travel Guide', '239.192.3.119': 'Outdoor Channel', '239.192.2.14': 'Кто есть кто', '239.192.0.39': 'Radio Ukraine     RUI', '239.192.0.38': 'Love Radio', '239.192.1.51': 'Перец ТВ', '239.192.0.31': 'QTV', '239.192.0.30': 'Интер+', '239.192.0.33': 'Плюс Плюс', '239.192.0.32': 'Гамма', '239.192.0.35': 'Radio Era', '239.192.0.34': 'Unian-TV', '239.192.0.37': 'Radio Ukraine     UR3', '239.192.0.36': 'Radio Ukraine     UR1', '239.192.5.6': 'Кинорейс 4 (тест)', '239.192.5.4': 'Кинорейс 3 (тест)', '239.192.5.5': 'Кинорейс 5 (тест)', '239.192.5.2': 'Кинорейс 1 (тест)', '239.192.5.3': 'Кинорейс 2 (тест)', '239.192.1.19': 'TV1000 East', '239.192.2.55': 'Мультимания', '239.192.2.54': 'ТВ XXI', '239.192.2.57': 'Da Vinci Learning', '239.192.2.56': 'Оружие', '239.192.2.51': 'Кинолюкс (НТВ+)', '239.192.2.50': 'Многосерийное ТВ', '239.192.2.53': 'Комедия ТВ', '239.192.2.52': 'Индия ТВ', '239.192.2.59': 'Радость моя', '239.192.2.58': 'Xsport', '239.192.5.14': 'СТС Москва', '239.192.5.15': 'РЕН ТВ', '239.192.5.16': 'Первый канал (Россия)', '239.192.5.17': 'Россия 1', '239.192.5.13': 'ТНТ', '239.192.5.18': 'Футбол (НТВ+)', '239.192.4.3': 'Кинопоказ HD2', '239.192.4.2': 'Телепутешествия HD', '239.192.4.1': 'Кинопоказ HD1', '239.192.4.7': 'Eurosport HD', '239.192.4.6': 'Mezzo Live HD', '239.192.4.5': 'HD Life', '239.192.4.4': 'Еда ТВ HD', '239.192.4.9': 'National Geographic HD', '239.192.4.8': 'M6.FR HD'}

        person = self.person_ent.get()
        host = None
        err = False
        try:
            b = []
            b = person.split("/")
            host = b[0]
            iface = b[1]
            i = int(iface)
            if i > 28:
                err = True
                story = "Нет такого порта!"
        except:
            story = "Ввод неверен, повторите ввод!"
            err = True
        if err:
            story = story + " Введите корректный номер порта!"

        else:
            if host:    
                user = "admin"
                password = "MsgPvvF03"
                password1 = "TFRjhx6224"
                password2 = "omgMs69F"
                global tn
                try:
                    tn = telnetlib.Telnet(host, 23, 2)
                except:
                    story = "Заданный IP недоступен, проверьте правильность ввода!"
                    self.main_text.delete(0.0, END)
                    self.main_text.insert(0.0, story)
                    return None

                if self.switcher.get() == "1":
                    model_check = tn.read_until(b"User name: ", 1)
                    if "Username" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора!, Выберите Edge-core!")
                        return None
                    tn.write(user.encode('ascii') + b"\r\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\r\n")
                    f = tn.read_until(b"#", 1).decode('ascii')
                    if "#" not in f:
                        tn.write(password1.encode('ascii') + b"\r\n")
                        tn.read_until(b"#", 1)
                    tn.write(b"show running-config interface port-channel "+ iface.encode('ascii') + b"\r\n")
                    file = tn.read_until(b"# ", 0.5).decode('ascii')
                    tn.write(b"show multicast " + b"\r\n")
                    file2 = tn.read_until(b"# ", 0.5).decode('ascii')
                    start = file2.find("Index")
                    file2 = file2[start:]
                    lines = file2.splitlines()
                    story2 = "Этот абонент сейчас не смотрит никаких каналов"
                    groups = []
                    for line in lines:
                        if "898" in line:
                            words = line.split()
                            words = words[1:]
                            for word in words:
                                if str(iface) == str(word):
                                    try:
                                        channel = URLS[words[2]]
                                    except:
                                        channel = "Неизвестный канал =("
                                    story2 = "Запрос идёт на канал: " + channel + "  Время запроса: " + words[4] + "  Таймаут: " + words[3] + " секунд."
                                    groups.append(story2)

                    file2 = "\n".join(lines)
                    if "IPTV_L" in file:
                        story = "У абонента открыто 170 каналов"
                    elif "IPTVM" in file:
                        story = "У абонента открыто 110 каналов"
                    elif "IPTV_S" in file:
                        story = "У абонента открыто 70 каналов"
                    elif "IPTV_XL" in file:
                        story = "У абонента открыто 250 каналов"
                    elif "IPTV0" in file:
                        story = "У абонента открыто 70 каналов"
                    elif "IPTV0X" in file:
                        story = "У абонента открыто 50 каналов"
                    elif "IPTV1" in file:
                        story = "У абонента открыто 96 каналов"
                    elif "IPTV2" in file:
                        story = "У абонента открыто 146 каналов"
                    elif "ALL" in file:
                        story = "У абонента открыто 196 каналов"
                    else:
                        story = "Произошла какая-то ОШИБКА, не могу проверить профиль абонента!"

                    if groups:
                        story2 = "\n".join(groups)

                    story = "\t\tКоличество каналов доступных абоненту: " + "\n\n" + story + "\n\n\n\n\t\t" + "Запросы от абонента в данный момент: " + "\n\n"+ story2

                    if self.details.get():
                        pass

                    tn.write(b"exit\r\n")
            
                else:
                    story = "\t\t\t\nТЕСТ IPTV Edge-core! \n\n"
                    model_check = tn.read_until(b"Username: ", 1)
                    if "User name" in model_check.decode('ascii'):
                        tn.close()
                        self.main_text.delete(0.0, END)
                        self.main_text.insert(30.30, "Выбрана неверная модель коммутатора! Выберите ZyXEL!")
                        return None
                    if "Zeleniy" not in model_check.decode('ascii'):
                        tn.write(user.encode('ascii') + b"\r\n")
                        tn.read_until(b"Password: ")
                        tn.write(password2.encode('ascii') + b"\r\n")
                        f = tn.read_until(b"#", 1).decode('ascii')
                        if "#" not in f:
                            tn.write(password1.encode('ascii') + b"\r\n")
                            tn.read_until(b"#", 1)
                        tn.write(b"show mvr members" + b"\r\n")
                        file = tn.read_until(b"More", 0.5).decode('ascii')
                        file[file.find("MVR"):]
                        while "SPNT" not in file:
                            tn.write(b" ")
                            file = file + tn.read_until(b"More", 0.5).decode('ascii')
                        lines = file.splitlines()
                        line_to_find = "eth1/" + iface
                        score = []
                        new_lines = []
                        for line in lines:
                            if "239.192" in line:
                                start = line.find("239.192")
                                new_lines.append(line[start:])
                                if line_to_find in line:
                                    score.append(line[start:])
                        file = "\n".join(new_lines)
                        if score:
                            new_score = []
                            new_score.append("\n\n Абонент сейчас смотрит следующие каналы: \n")
                            for line in score:
                                words = line.split()
                                try:
                                    channel = URLS[words[0]]
                                except:
                                    channel = "Неизвестный =("
                                new_score.append("---\t" + channel)
                            info = "\n".join(new_score)
                        else:
                            info = "Абонент не смотрит никаких каналов в данный момент"
                        if self.details.get():
                            story = story + file
                        else:
                            story = story + info
                    else:
                        tn.write(user.encode('ascii') + b"\r\n")
                        tn.read_until(b"Password: ")
                        tn.write(password2.encode('ascii') + b"\r\n")
                        f = tn.read_until(b"#", 1).decode('ascii')
                        if "#" not in f:
                            tn.write(password1.encode('ascii') + b"\r\n")
                            tn.read_until(b"#", 1)
                        tn.write(b"show running-config interface ethernet 1/" + iface.encode('ascii') + b"\r\n")
                        file = tn.read_until(b"#", 1).decode('ascii')
                        if "ip igmp filter " in file:
                            if "ip igmp filter 1" in file:
                                channels = "У абонента открыто 70 каналов \n\n\n"
                            elif "ip igmp filter 2" in file:
                                channels = "У абонента открыто 110 каналов \n\n\n"
                            elif "ip igmp filter 3" in file:
                                channels = "У абонента открыто 170 каналов \n\n\n"
                            elif "ip igmp filter 4" in file:
                                channels = "У абонента открыто 250 каналов \n\n\n"
                            else:
                                channels = "Неизвестное количество каналов \n\n\n"
                        else:
                            channels = "Произошла ОШИБКА! Неудалось определить количество каналов! "

                        #result = []

                        result = "\n\n\n" + channels
                        tn.write(b"show mvr members sort-by-port ethernet 1/" + iface.encode('ascii') + b"\r\n")
                        file = tn.read_until(b"#", 1).decode('ascii')
                        file[file.find("MVR"):]
                        lines = file.splitlines()
                        file = "\n".join(lines[1:])
                        info = []
                        score = []
                        for line in file.splitlines():
                            if "Eth" in line:
                                info.append(line)
                        if info:
                            for line in info:
                                word = line.split()
                                try:
                                    channel = URLS[word[4]]
                                except:
                                    channel = "Неизвестный =( "
                                score.append("Абонент смотрит канал: " + channel + " \n")
                        else:
                            score.append("Абонент не смотрит никаких каналов в данный момент")
                        result = result + "\n\n\n" + "\n".join(score)

                        if self.details.get():
                            story = story + file
                        else:
                            story = story + result
                            



        self.main_text.delete(0.0, END)
        self.main_text.insert(0.0, story)
# main
tn = None
root = Tk()
root.geometry("950x700")
root.title("Supporter 2.1")
app = Application(root)
app.bg = "blue"
root.mainloop()
