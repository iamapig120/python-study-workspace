import tkinter
import Calculator as calc
buttonSize = 64
window = tkinter.Tk()
window.geometry(""+str(buttonSize*4)+"x"+str(buttonSize*6))
window.resizable(False, False)
window.title("计算器")
inputLine = tkinter.Label(window, justify=tkinter.RIGHT,
                          text='0', font="Helvetica 24", padx=8, anchor="e")
inputLine.place(x=0, y=0, width=buttonSize*4, height=buttonSize)


def appendText(text: str):
    print("Input:", text)
    if text == "Del":
        inputLine.config(text=inputLine["text"][:-1])
        if len(inputLine["text"]) == 0:
            inputLine.config(text="0")
    elif inputLine["text"] == "0":
        inputLine.config(text=text)
    elif text == "=":
        inputLine.config(text=calc.calc(inputLine["text"]))
    else:
        inputLine.config(text=inputLine["text"] + text)
    print("Label", inputLine["text"])


buttons = [tkinter.Button(window, text=t) for t in [
    '%', '^', 'Del', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '(', ')', '0', '=']]
for index, btn in enumerate(buttons):
    btn.place(x=index % 4 * buttonSize, y=buttonSize + index //
              4 * buttonSize, width=buttonSize, height=buttonSize)
    btn.bind("<Button-1>", lambda e: appendText(e.widget["text"]))
# inputLine
window.mainloop()
