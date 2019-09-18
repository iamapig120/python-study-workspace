import tkinter
import tkinter.ttk
import tkinter.font
import CalculatorV2 as calc
buttonSize = 64
window = tkinter.Tk()
window.style = tkinter.ttk.Style()
window.style.theme_use("classic")
window.geometry(""+str(buttonSize*4)+"x"+str(buttonSize*6+buttonSize//2))
window.resizable(False, False)
window.title("计算器")

input_line_fnt = tkinter.font.Font(
    family=('微软雅黑'), size=12, weight=tkinter.font.NORMAL)
result_line_fnt = tkinter.font.Font(
    family=('微软雅黑'), size=24, weight=tkinter.font.NORMAL)
input_btn_fnt = tkinter.font.Font(
    family=('微软雅黑'), size=12, weight=tkinter.font.NORMAL)

input_line = tkinter.Label(window, justify=tkinter.RIGHT,
                           text='', font=input_line_fnt, padx=8, anchor="e")
input_line.place(x=0, y=buttonSize//8, width=buttonSize *
                 4, height=buttonSize//2)

result_line = tkinter.Label(window, justify=tkinter.RIGHT,
                            text='0', font=result_line_fnt, padx=8, anchor="e")
result_line.place(x=0, y=buttonSize//2, width=buttonSize*4, height=buttonSize)

calced_state = 0
symbols = ['+', '-', '*', '/', '%', '^']


def appendText(text: str):
    global calced_state
    # print("Input:", text)
    if calced_state:
        if calced_state == 1:
            input_line.config(text=result_line["text"])
        else:
            input_line.config(text="")
        result_line.config(text="0")
        calced_state = 0
    if text == "AC":
        # inputLine.config(text=inputLine["text"][:-1])
        # if len(inputLine["text"]) == 0:
        #     inputLine.config(text="0")
        input_line.config(text="")
        result_line.config(text="0")
    elif text == "=":
        result: str
        print("Calc", input_line["text"])
        try:
            result = str(calc.calc(input_line["text"]))
            calced_state = 1
        except calc.CalcError as err:
            result = err.errorinfo
            calced_state = 2
        finally:
            result_line.config(text=result)
            input_line.config(text=input_line["text"] + text)
            if not calced_state:
                calced_state = -1
    elif input_line["text"] == "":
        if text in symbols:
            if not text == '-':
                input_line.config(text="0")
        input_line.config(text=input_line["text"] + text)
        try:
            result_line.config(
                text=str(calc.calc(input_line["text"], portion=True)))
        except calc.CalcError as err:
            result_line.config(text=err.errorinfo)
            calced_state = 2
    else:
        input_line.config(text=input_line["text"] + text)
        try:
            result_line.config(
                text=str(calc.calc(input_line["text"], portion=True)))
        except calc.CalcError as err:
            result_line.config(text=err.errorinfo)
            calced_state = 2
    # print("Label", inputLine["text"])


btn_chars = ['%', '^', 'AC', '/', '7', '8', '9', '*', '4',
             '5', '6', '-', '1', '2', '3', '+', '(', ')', '0', '=']
buttons = [tkinter.Button(window, text=text, font=input_btn_fnt)
           for text in btn_chars]


def key_press_event(e):
    if e.char in btn_chars:
        return appendText(e.char)
    if e.keycode == 13 or e.keycode == 108:
        return appendText('=')
    if e.keycode == 8:
        return appendText('AC')


window.bind("<Key>", key_press_event)
for index, btn in enumerate(buttons):
    btn.place(x=index % 4 * buttonSize, y=buttonSize + index //
              4 * buttonSize + buttonSize/2, width=buttonSize, height=buttonSize)
    btn.config(background="#F3F3F3")
    btn.bind("<Button-1>", lambda e: appendText(e.widget["text"]))
    btn.bind("<Enter>", lambda e: e.widget.config(background="#DDDDDD"))
    btn.bind("<Leave>", lambda e: e.widget.config(background="#F3F3F3"))
# inputLine
window.mainloop()
