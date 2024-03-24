import tkinter as tk
# Create the main application window
root = tk.Tk()

# Set window title and dimensions, and disable resizing
root.title('Simple Calculator')
root.geometry("570x600+100+200")
root.resizable(False,False)

# Set background color
root.configure(bg="#17161b")

# Variable to store the equation entered by the user
equation = ""

# Function to update the equation label when a button is clicked
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

# Function to clear the equation
def clear():
    global equation
    equation = ""
    label_result.config(text = equation)

# Function to evaluate the equation and display the result
def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result= "error"
            equation = ""
    label_result.config(text = result)

# Create a label to dsiplay the equation and result
label_result= tk.Label(root, width=25, height=2, text="", font=("arial",30))
label_result.pack()

# Create buttons for basic arithmetic operations and numbers
button_result=tk.Button(root,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10,y=100)
button_result=tk.Button(root,text="/", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=150,y=100)
button_result=tk.Button(root,text="%", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=290,y=100)
button_result=tk.Button(root,text="*", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=430,y=100)

button_result=tk.Button(root,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10,y=200)
button_result=tk.Button(root,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150,y=200)
button_result=tk.Button(root,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290,y=200)
button_result=tk.Button(root,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430,y=200)

button_result=tk.Button(root,text="4", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10,y=300)
button_result=tk.Button(root,text="5", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150,y=300)
button_result=tk.Button(root,text="6", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290,y=300)
button_result=tk.Button(root,text="+", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430,y=300)

button_result=tk.Button(root,text="1", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10,y=400)
button_result=tk.Button(root,text="2", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150,y=400)
button_result=tk.Button(root,text="3", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290,y=400)
button_result=tk.Button(root,text="0", width=11, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10,y=500)

button_result=tk.Button(root,text=".", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290,y=500)
button_result=tk.Button(root,text="=", width=5, height=3, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=430,y=400)

# Positioning of buttons and assigning click actions
# Buttons are placed in a grid-like manner using .place()method

# Start the GUI application
root.mainloop()