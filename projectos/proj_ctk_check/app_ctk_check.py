import customtkinter

def game():
    my_label.configure(text="Clicaste! :O")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Noo wayuy :O")
root.geometry("700x450")
root.resizable(width=False, height=False)

check_var = customtkinter.StringVar()
my_check = customtkinter.CTkCheckBox(
    root,
    text="Queres jogar um jogo?",
    variable=check_var,
    onvalue="on",
    offvalue="off",
    command=game
)
my_check.pack(pady=40)

my_label = customtkinter.CTkLabel(
    root,
    text=""
)
my_label.pack(pady=20)

root.mainloop()