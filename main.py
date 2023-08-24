from customtkinter import *
from CTkSlideView import CTkSlideView

set_appearance_mode("dark")
set_default_color_theme("dark-blue")


root = CTk()
root.geometry("1800x900")
root.title("CTk SlideMenu")


#An Example For Slide Menu

slide_menu = CTkSlideView(root)
slide_menu.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl = CTkLabel(slide_menu.create_tab(), text="Slide 1", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)
lbl2 = CTkLabel(slide_menu.create_tab(), text="Slide 2", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)
lbl3 = CTkLabel(slide_menu.create_tab(), text="Slide 3", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)
lbl4 = CTkLabel(slide_menu.create_tab(), text="Slide 4", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)
lbl5 = CTkLabel(slide_menu.create_tab(), text="Slide 5", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)





root.mainloop()