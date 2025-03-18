import tkinter as tk

def first_print():
    text = "Hello World!"
    text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 16))
    text_output.grid(row=0, column=1)

window = tk.Tk()
window.geometry("600x600")
window.title("Hello TkInter!")
window.resizable(False, False)
window.configure(background="white")

# Creazione del bottone prima di mainloop
first_button = tk.Button(window, text="Saluta!", command=first_print)
first_button.grid(row=0, column=0)

if __name__ == "__main__":
    window.mainloop()