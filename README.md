# CTkSlideView
A Slide View (Slideshow carousel) for customtkinter.
This includes a smooth animation between the slides too 🤩

***
## Example Video 👇

https://github.com/rigvedmaanas/CTkSlideView/assets/77579661/c10fb8f7-2057-4da2-bf10-886f7eb2a9f4

***

## How to use it?

1. Download the source code.
2. Copy and Paste the CTkSlideView python file in the directory where your python program is present.
3. import the CTkSlideView

***

## An Example for the CTkSlideView

```python
from customtkinter import *
from CTkSlideView import CTkSlideView

set_appearance_mode("dark")
set_default_color_theme("dark-blue")


root = CTk()
root.geometry("1800x900")
root.title("CTk SlideView")


slide_menu = CTkSlideView(root)
slide_menu.place(relx=0.5, rely=0.5, anchor=CENTER)


# slide_menu.create_tab() will return a frame where you can display anything.

# Some Example Slides
CTkLabel(slide_menu.create_tab(), text="Slide 1", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)

CTkLabel(slide_menu.create_tab(), text="Slide 2", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)

CTkLabel(slide_menu.create_tab(), text="Slide 3", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)

CTkLabel(slide_menu.create_tab(), text="Slide 4", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)

CTkLabel(slide_menu.create_tab(), text="Slide 5", font=("SF Display", 50)).place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
```

Feel free to customize it 😃
