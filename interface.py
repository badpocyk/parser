from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from google_archive_cits_parser import *
import docx
root = Tk()
# Название и разрешение можно поменять при желании, по мне так норм.
root.title(u'Parser')
# Числа которые прибавляются - это смещение на экране чтобы вылазило окно удобно.
root.geometry('1060x608+200+8')
root.resizable(False, False)

# Клик кнопки Получить. Внутрь функции вставляй че надо там относительно этого блока
# def click_poluchit():
#     search_request = get_name()
#     bi = browser_index()
#     cap = captcha_()
#     pages = int(amount_pages())
#     print(pages)
#     book_list = get_list(search_request, bi, cap, pages)
#     for book in book_list:
#         listbox_ssylki.insert(END, book.name)


# путь файла
def click_path():
    try:
        print(select_ssylka())
        file_dialog = filedialog.askopenfilename()
        path = file_dialog
        label_path_file['text'] = path
        document = docx.Document(path)
        document.add_paragraph(select_ssylka())
        document.save(path)
        label_path['text'] = 'Готово'
        return path
    except TclError:
        string = "Не выбрана ссылка!"
        messagebox.showerror("Ошибка", string)
    except Exception as e:
        string = "Произошла критическая ошибка! Код ошибки: '" + str(e) + "'. Попробуйте снова."
        messagebox.showerror("Ошибка", string)


# Клик кнопки Вставить. Аналогично
def click_insert():
    print()

# Получить название книги
def get_name():
    name = text_name.get('1.0', END+'-1c')
    return name

# Индекс выбранного браузера в списке
def browser_index():
    browser = variable.get()
    return browser

# Индекс выбранного формата в списке
def format_index():
    format = variable2.get()
    return format

# Наличие PDF
def pdf():
    pdf_ = var1.get()
    return pdf_

# Количество страниц
def amount_pages():
    amount = entry_pages.get()
    return amount

# Выбор нужной ссылки
def select_ssylka():
    ssylka = listbox_ssylki.curselection()
    ssy = listbox_ssylki.get(ssylka)
    return ssy

def click_poluchit():
    try:
        search_request = get_name()
        bi = browser_index()
        cap = captcha_()
        pdf_file = pdf()
        if (search_request == "") | (amount_pages() == ""):
            messagebox.showerror("Ошибка", "Введите название книги и количество страниц!")
            pass
        else:
            pass
            #listbox_ssylki.delete(0, END)
        pages = int(amount_pages())
        book_list = get_list(search_request, bi, cap, pages)
        for book in book_list:
            if format_index() == "ГОСТ":
                if int(pdf_file) == 1:
                    if book.pdf:
                        listbox_ssylki.insert(END, book.gost)
                else:
                    listbox_ssylki.insert(END, book.gost)
            elif format_index() == "MLA":
                if int(pdf_file) == 1:
                    if book.pdf:
                        listbox_ssylki.insert(END, book.mla)
                else:
                    listbox_ssylki.insert(END, book.mla)
            elif format_index() == "APA":
                if int(pdf_file) == 1:
                    if book.pdf:
                        listbox_ssylki.insert(END, book.apa)
                else:
                    listbox_ssylki.insert(END, book.apa)
    except Exception as e:
        string = "Произошла критическая ошибка! Код ошибки: '" + str(e) + "'. Попробуйте снова."
        messagebox.showerror("Ошибка", string)
# Чекбокс капчи 
def captcha_():
    cap = captcha.get()
    return cap

root.rowconfigure(0, pad=10)
root.rowconfigure(1, pad=20)
root.rowconfigure(2, pad=20)
root.rowconfigure(3, pad=10)
root.rowconfigure(4, pad=90)
root.rowconfigure(5, pad=30)
root.rowconfigure(6, pad=30)

root.columnconfigure(0, pad=50)
root.columnconfigure(1, pad=10)
root.columnconfigure(2, pad=10)

# Все виджеты ниже

frame_name = Frame(root)
frame_browser = Frame(root)
frame_format = Frame(root)
frame_pdf = Frame(root)
frame_pages = Frame(root)
frame_ssylki = Frame(root)
frame_path = Frame(root)
frame_get = Frame(root)

label_name = Label(frame_name, text='Введите название книги:',font='Verdana 13')
text_name = Text(frame_name, font='Verdana 11',width=30,height=4)
label_browser = Label(frame_browser,text='Выберите браузер:\t',font='Verdana 13')

# listbox_browser = Listbox(frame_browser, height=3,width=27, selectmode=BROWSE, font='Verdana 13')
# listbox_browser.insert(END, 'Google Chrome')
# listbox_browser.insert(END, 'Firefox')
# listbox_browser.insert(END, 'Яндекс.Браузер')

variable = StringVar(root)
variable.set("Google Chrome")
w = OptionMenu(frame_browser,  variable,"Google Chrome", "Firefox")

label_format = Label(frame_format,text='Выберите формат :', font='Verdana 13')

# listbox_format = Listbox(frame_format, height=3, width=27, selectmode=BROWSE, font='Verdana 13')

# listbox_format.insert(END, 'MLA')
# listbox_format.insert(END, 'APA')

variable2 = StringVar(root)
variable2.set("ГОСТ")
w2 = OptionMenu(frame_format,  variable2,"MLA", "APA", "ГОСТ")

label_pdf = Label(frame_pdf, text='Наличие PDF файла:', font='Verdana 13')

var1 = IntVar()

check_pdf1 = Checkbutton(frame_pdf, text='Выбирать при наличии PDF\t', variable=var1, font='Verdana 13')

label_pages = Label(frame_pages, text='Выберите количество страниц:',font='Verdana 13')
entry_pages = Entry(frame_pages, width=30, font='Verdana 11')

# Кнопка Получить
button_poluchit = Button(frame_get, text='Получить', width=20, font='Verdana 13',background='#ccc', command=click_poluchit)
captcha = IntVar()
check_captcha = Checkbutton(frame_get, text='Обойти капчу', variable=captcha, font='Verdana 13')

label_ssylki = Label(frame_ssylki, text='Выберите нужную ссылку:', font='Verdana 13')

scrollbar = Scrollbar(frame_ssylki)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbarx = Scrollbar(frame_ssylki, orient=HORIZONTAL)
scrollbarx.pack(side=BOTTOM, fill=X)

listbox_ssylki = Listbox(frame_ssylki,yscrollcommand=scrollbar.set,xscrollcommand=scrollbarx.set, selectmode=BROWSE, font='Verdana 11', height=20, width=60)

scrollbar.config(command=listbox_ssylki.yview)
scrollbarx.config(command=listbox_ssylki.xview)

label_path = Label(frame_path, text='Введите путь к файлу Microsoft Word:', font='Verdana 13')
#entry_path = Entry(frame_path, width=35, font='Verdana 11')
button_path = Button(frame_path,width=20, font='Verdana 13', command=click_path, text='Открыть и вставить', background='#ccc')
label_path_file = Label(frame_path, text='', font='Verdana 11')

frame_name.grid(row=0,column=0)
frame_browser.grid(row=1,column=0)
frame_format.grid(row=2,column=0)
frame_pdf.grid(row=3,column=0)
frame_pages.grid(row=4, column=0)
frame_get.grid(row=5, column=0)
frame_ssylki.grid(row=0,column=1, rowspan=5, columnspan=6)
frame_path.grid(row=5, column=4)

label_name.pack()
text_name.pack()
label_browser.pack()
#listbox_browser.pack()
w.pack()
label_format.pack()
#listbox_format.pack()
w2.pack()
label_pdf.pack()
check_pdf1.pack()
label_pages.pack()
entry_pages.pack()
label_ssylki.pack()
listbox_ssylki.pack()
label_path.pack()
#entry_path.pack()
button_path.pack()
label_path_file.pack()
button_poluchit.pack()
check_captcha.pack()
root.mainloop()