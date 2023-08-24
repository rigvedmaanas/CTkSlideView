from customtkinter import CTkLabel, CTkFrame, CTkButton, CENTER, DISABLED, NORMAL
from CTkAnimator import CTkAnimator

class CTkSlideView(CTkFrame):
    def __init__(self, *args,
                 width: int = 900,
                 height: int = 500,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.w = width
        self.h = height
        self.tabs = []
        self.main_smoother = self.w/2
        self.guide = self.w/2
        self.right_btn = CTkButton(self, text=">", width=40, height=40, bg_color="transparent", font=("SF Display", 20), command=self.move_left)
        self.right_btn.place(x=self.w-50, rely=0.5, anchor=CENTER)

        self.left_btn = CTkButton(self, text="<", width=40, height=40, bg_color="transparent", font=("SF Display", 20), command=self.move_right, state=DISABLED)
        self.left_btn.place(x=50, rely=0.5, anchor=CENTER)
        self.left_anim = CTkAnimator(from_=0, to=self.w, acceleration=0.01)
        self.right_anim = CTkAnimator(from_=0, to=-self.w, acceleration=0.01)
        self.indicator_frame = CTkFrame(self, height=25, corner_radius=0, fg_color="transparent")
        self.indicator_frame.place(relx=0.5, y=self.h-15, anchor=CENTER)



    def move_left(self):
        if int(self.tabs[-1][0].place_info()["x"]) == self.w/2:
            self.right_btn.configure(state=DISABLED)
        else:
            self.right_btn.configure(state=NORMAL)
        if int(self.tabs[0][0].place_info()["x"]) != self.w / 2:
            self.left_btn.configure(state=NORMAL)
        val = self.left_anim.get()

        for i, x in enumerate(self.tabs):

            x[0].place(x=x[1]-val, y=((self.h-20)/2))

        if self.left_anim.completed != True:
            self.winfo_toplevel().after(10, self.move_left)

        else:
            self.left_anim.change_val(from_=self.left_anim.from_, to=self.left_anim.from_+self.w)
            for i, x in enumerate(self.tabs):
                #x[0].place(x=x[1] - val, rely=0.5)
                self.tabs[i][1] = int(self.tabs[i][0].place_info()["x"])
                if self.tabs[i][1] == self.w/2:
                    self.tabs[i][2].configure(fg_color="white")
                else:
                    self.tabs[i][2].configure(fg_color="grey")


    def move_right(self):
        if int(self.tabs[0][0].place_info()["x"]) == self.w / 2:
            self.left_btn.configure(state=DISABLED)
        else:
            self.left_btn.configure(state=NORMAL)
        if int(self.tabs[-1][0].place_info()["x"]) != self.w/2:
            self.right_btn.configure(state=NORMAL)
        val = self.right_anim.get()
        for i, x in enumerate(self.tabs):
            x[0].place(x=x[1] - val,  y=((self.h-20)/2))


        if self.right_anim.completed != True:
            self.winfo_toplevel().after(10, self.move_right)

        else:
            self.right_anim.change_val(from_=self.right_anim.from_, to=self.right_anim.from_ - self.w)
            for i, x in enumerate(self.tabs):
                # x[0].place(x=x[1] - val, rely=0.5)
                self.tabs[i][1] = int(self.tabs[i][0].place_info()["x"])
                if self.tabs[i][1] == self.w/2:
                    self.tabs[i][2].configure(fg_color="white")
                else:
                    self.tabs[i][2].configure(fg_color="grey")




    def create_tab(self):
        frame = CTkFrame(self, width=self.w-100, height=self.h-50)
        frame.place(x=self.guide, y=((self.h-20)/2), anchor=CENTER)
        lbl = CTkLabel(self.indicator_frame, width=5, height=5, fg_color="grey", corner_radius=8, text="", font=("SF Display", 1))
        lbl.pack(side="left", padx=5)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        self.tabs.append([frame, self.guide, lbl])
        self.tabs[0][2].configure(fg_color="white")
        self.left_btn.lift()
        self.right_btn.lift()
        self.guide += self.w
        return frame
