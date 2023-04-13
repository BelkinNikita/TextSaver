import tkinter as tk
import os.path


def Error():
    ErrorWindow = tk.Tk()
    ErrorWindow.title('Saving the file')
    ErrorWindow.geometry('600x100')
    Error_Message = tk.Label(ErrorWindow, text='Saving file path has not been found', fg='red', font=('Arial', 15))
    Error_Message.pack(pady=25)


def SettingsButton():
    global sett_cond
    global settings_window
    global path
    if sett_cond == 0:
        SettingshavebeenOpened()
        sett_cond = 1
    else:
        path = settings_window.get('1.0', 'end')
        settings_window.delete('1.0', 'end')
        settings_window.place_forget()
        btn_return.place_forget()
        sett_cond = 0


def SettingshavebeenOpened():
    settings_window.insert(tk.END, path)
    settings_window.place(x=35, y=8)
    btn_return.place(x=440, y=5)


def FileIsSaved_btn():
    try:
        text_input = textbox.get('1.0', 'end')
        if sett_cond == 0:
            path_and_file = path + 'textfile.txt'
        else:
            path_and_file = os.path.join(settings_window.get('1.0', 'end'), 'textfile.txt')
        path_and_file = path_and_file.replace('\n', '')
        file = open(path_and_file, 'a')
        file.write(text_input)
        Save_Window()
    except:
        Error()


def FileIsSaved_key(event):
    try:
        text_input = textbox.get('1.0', 'end')
        if sett_cond == 0:
            path_and_file = path + 'textfile.txt'
        else:
            path_and_file = os.path.join(settings_window.get('1.0', 'end'), 'textfile.txt')
        path_and_file = path_and_file.replace('\n', '')
        file = open(path_and_file, 'a')
        file.write(text_input)
        Save_Window()
    except:
        Error()


def Save_Window():
    WinSave = tk.Tk()
    WinSave.title('Saving the file')
    WinSave.geometry('600x100')
    text_input = textbox.get('1.0', 'end')
    if len(text_input) > 1:
        if len(text_input) > 13:
            text_input = (text_input[:8])
            text_input = text_input + '...'
        Save_Complete_Message = tk.Label(WinSave, text='The text "%s" has been saved successfully' % text_input,
                                         font=('Arial', 15))
    else:
        Save_Complete_Message = tk.Label(WinSave, text='text is empty', font=('Arial', 15))
    Save_Complete_Message.pack(pady=25)


def Return_Settings():
    settings_window.delete('1.0', 'end')
    path = 'C:\\Users\\%s\\Desktop\\' % os.getlogin()
    settings_window.insert(tk.END, path)


def Exit_btn():
    Window.destroy()

def Exit_key(event):
    Window.destroy()

Window = tk.Tk()
Window.title('TextSaver by @BelkinNikita')
Window.geometry('500x500')
Window.minsize(500, 500)
Window.maxsize(500, 500)
Window.bind('<Escape>', Exit_key)
Window.bind('<F5>', FileIsSaved_key)
path = 'C:\\Users\\%s\\Desktop\\' % os.getlogin()


textbox = tk.Text(Window, height=22)
textbox.pack(pady=50)

btn_exit = tk.Button(text='EXIT(f12)', font=('Arial, 18'), activebackground='grey', command=Exit_btn)
btn_exit.place(x=340,y=430)
btn_save = tk.Button(text='SAVE(f5)', font=('Arial, 18'), activebackground='grey', command=FileIsSaved_btn)
btn_save.place(x=220,y=430)

btn_return = tk.Button(text='@', font=('Arial, 8'), activebackground='grey', command=Return_Settings)
sett_cond = 0
settings_window = tk.Text(Window, height=1, width=40)
btn_setting = tk.Button(text='…', font=('Arial, 8'), activebackground='grey', command=SettingsButton)
btn_setting.place(x=5,y=5)


Window.mainloop()