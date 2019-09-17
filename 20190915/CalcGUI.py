import tkinter
import CalculatorV2 as calc
buttonSize = 64
window = tkinter.Tk()
window.geometry(""+str(buttonSize*4)+"x"+str(buttonSize*6+buttonSize//2))
window.resizable(False, False)
window.title("计算器")
inputLine = tkinter.Label(window, justify=tkinter.RIGHT,
                          text='', font="Helvetica 12", padx=8, anchor="e")
inputLine.place(x=0, y=buttonSize//8, width=buttonSize*4, height=buttonSize//2)

resultLine = tkinter.Label(window, justify=tkinter.RIGHT,
                           text='0', font="Helvetica 24", padx=8, anchor="e")
resultLine.place(x=0, y=buttonSize//2, width=buttonSize*4, height=buttonSize)

calced_state = 0
symbols = ['+', '-', '*', '/', '%', '^']


def appendText(text: str):
    global calced_state
    # print("Input:", text)
    if calced_state:
        if calced_state == 1:
            inputLine.config(text=resultLine["text"])
        else:
            inputLine.config(text="")
        resultLine.config(text="0")
        calced_state = 0
    if text == "AC":
        # inputLine.config(text=inputLine["text"][:-1])
        # if len(inputLine["text"]) == 0:
        #     inputLine.config(text="0")
        inputLine.config(text="")
        resultLine.config(text="0")
    elif text == "=":
        result: str
        print("Calc", inputLine["text"])
        try:
            result = str(calc.calc(inputLine["text"]))
            calced_state = 1
        except calc.CalcError as err:
            result = err.errorinfo
            calced_state = 2
        finally:
            resultLine.config(text=result)
            inputLine.config(text=inputLine["text"] + text)
            if not calced_state:
                calced_state = -1
    elif inputLine["text"] == "":
        if text in symbols:
            if not text == '-':
                inputLine.config(text="0")
        inputLine.config(text=inputLine["text"] + text)
        resultLine.config(text=str(calc.calc(inputLine["text"], portion=True)))
    else:
        inputLine.config(text=inputLine["text"] + text)
        try:
            resultLine.config(
                text=str(calc.calc(inputLine["text"], portion=True)))
        except calc.CalcError as err:
            resultLine.config(text=err.errorinfo)
            calced_state = 2
    # print("Label", inputLine["text"])


buttons = [tkinter.Button(window, text=t) for t in [
    '%', '^', 'AC', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '(', ')', '0', '=']]
for index, btn in enumerate(buttons):
    btn.place(x=index % 4 * buttonSize, y=buttonSize + index //
              4 * buttonSize + buttonSize/2, width=buttonSize, height=buttonSize)
    btn.bind("<Button-1>", lambda e: appendText(e.widget["text"]))
# inputLine
window.mainloop()
