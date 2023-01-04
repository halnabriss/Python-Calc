import tkinter
from tkinter import *

number1 = 0
number2 = 0
operator1 = "+"
operator_on = False

####################
def doFun(t):
    new_text = str(t)
    input1.insert( "end" , str(new_text) )
    # print(str(t))
    # GLineEdit_520["text"] = "hello"
    # print("hiiiiiiiii" + str(t))
######################


def clear_input():
    input1.delete(0, "end")
    input1.insert(0 , "")

############################

def add_dot():
    if int(input1.get().rfind(".")) < 0:
        doFun(".")


####################################################


def define_operator(x):
    global number1, number2, operator_on, operator1
    number1 = float(input1.get())
    operator1 = x
    operator_on = True
    input1.delete(0, "end")
    input1.insert(0 , "")


################################


def start_calculation():
    global number1, number2, operator_on, operator1
    number2 = float(input1.get())


    if operator1 == "+":
        input1.delete(0, "end")
        input1.insert(0, number1 + number2)

    elif operator1 == "-":
        input1.delete(0, "end")
        input1.insert(0, number1 - number2)

    elif operator1 == "*":
        input1.delete(0, "end")
        input1.insert(0, number1 * number2)

    elif operator1 == "/":
        input1.delete(0, "end")
        try:
            input1.insert(0, number1 / number2)

        except:
            input1.insert(0, "Errrrrrrooooorrrrrrrrrr")



window = Tk()

window.geometry('360x200')
window.title("Calculator")
# label1 = tkinter.Label(window)
# label1["text"]="Welcome"
# label1.place(x=100,y=50,width=70,height=25)

input1 = tkinter.Entry(window)
input1.insert(0, "")
input1.place(x=10,y=10,width=340,height=25)


buttons =  [None] *10

buttons[0] = tkinter.Button( window, text="0", command=lambda ztemp="0": doFun(ztemp))
buttons[0].place( x=190 , y=140, width=70, height=25)
xarg = -80



for index in range(1,10):
    buttons[index] = tkinter.Button( window, text=str(index), command=lambda ztemp=index: doFun(ztemp))
    if (index-1) % 3 == 0 :
        xarg = xarg + 90
    buttons[index].place( x=xarg, y=(index-1)%3*30+50, width=70, height=25)
    # window.bind('<buttons[index]>', doFun)


buttons_sum = tkinter.Button( window, text="+", command=lambda ztemp="+": define_operator(ztemp))
buttons_sum.place( x=280 , y=50, width=70, height=25)

buttons_minus = tkinter.Button( window, text="-", command=lambda ztemp="-": define_operator(ztemp))
buttons_minus.place( x=280 , y=80, width=70, height=25)

buttons_mul = tkinter.Button( window, text="*", command=lambda ztemp="*": define_operator(ztemp))
buttons_mul.place( x=280 , y=110, width=70, height=25)

buttons_div = tkinter.Button( window, text="/", command=lambda ztemp="/": define_operator(ztemp))
buttons_div.place( x=280 , y=140, width=70, height=25)

buttons_dot = tkinter.Button( window, text=".", command=add_dot)
buttons_dot.place( x=100 , y=140, width=70, height=25)

buttons_equal = tkinter.Button( window, text="=", command=start_calculation)
buttons_equal.place( x=10 , y=140, width=70, height=25)

buttons_clear = tkinter.Button( window, text="clear", command=clear_input)
buttons_clear.place( x=10 , y=170, width=340, height=25)
#window.bind("<Return>", doFun)





window.mainloop()




