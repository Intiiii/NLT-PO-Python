import customtkinter as ctk

gui = ctk.CTk()

screenwidth = gui.winfo_screenwidth()
width = 800
height = 600
x = (screenwidth-width) // 2
y = 20

gui.geometry(f"{width}x{height}+{x}+{y}")
gui.title("ceasar code")

alfabet1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabet = 'abcdefghijklmnopqrstuvwxyz'

gui.rowconfigure(3, weight=1)
gui.columnconfigure(3, weight=1)

gui.input_field = ctk.CTkTextbox(gui)
gui.input_field.grid(row=1, column=1, columnspan=3, rowspan=2, padx=10, pady=10, sticky="nsew")

gui.selected_value = ctk.StringVar()
gui.option_menu = ctk.CTkOptionMenu(gui, variable=gui.selected_value, values=[str(i) for i in range(1, 27)])
gui.option_menu.grid(row=3, column=1, padx=10, pady=10)

gui.convert_button = ctk.CTkButton(gui, text="encrypt", command=encrypt)
gui.convert_button.grid(row=3, column=2, padx=10, pady=10)

def encrypt():
    input = gui.input_field.get("1.0", "end")
    verschuiving = int(gui.selected_value.get())
    output = ''
    for letter in input:
        if letter in alfabet1:
            index = alfabet1.index(letter)
            nindex = (index + verschuiving) % 26
            output += alfabet1[nindex]
        elif letter in alfabet:
            index = alfabet.index(letter)
            nindex = (index + verschuiving) % 26
            output += alfabet[nindex]
        else:
            output += letter
    gui.output_field.delete("1.0", "end")
    gui.output_field.insert("1.0", output)

gui.mainloop()