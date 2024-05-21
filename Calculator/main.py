#Caclulator GUI
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
from tkinter import simpledialog

class HelpDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Calculator Help")
        self.resizable(False,False)
        self.ico = Image.open('help.png')
        self.photo = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.photo)

        help_text = """
        Calculator Help:

        1. Basic Operations:
           - Addition (+): Enter the first number, press the '+' button, enter the second number, and click '=' to see the result.
           - Subtraction (-): Enter the first number, press the '-' button, enter the second number, and click '=' to see the result.
           - Multiplication (*): Enter the first number, press the *' button, enter the second number, and click '=' to see the result.
           - Division (/): Enter the first number, press the '/' button, enter the second number, and click '=' to see the result.

        2. Clearing the Display:
           - C (All Clear): Click the 'C' button to clear the entire display.

        3. Decimal Numbers:
           - Use the decimal point (.) button to input decimal numbers. For example, enter '3.14' for Pi.

        4. Other Functions:
           - Percentage (%): To calculate percentages, enter the number, press the '%' button, and click '=' to see the result.

        Note: The calculator follows the order of operations (BODMAS) for complex calculations.
        """

        help_label = tk.Label(self, text=help_text, justify=tk.LEFT)
        help_label.pack(padx=10, pady=10)
class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")
        self.resizable(False,False)
        self.ico = Image.open('about.png')
        self.photo = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.photo)

        about_text = """
Welcome to the Calculator GUI!

Created with passion and dedication by Rajan Poudel, a budding computer coding and programming enthusiast, 
this calculator represents my first step into the world of software development. With a deep love for 
computers and a desire to bring functionality to life, I embarked on this journey to create a user-friendly 
and efficient calculator application.

As a beginner in the world of coding, I embraced the challenge of building this GUI-based calculator from 
scratch. With every line of code written, I discovered the power and creativity that programming offers. This 
project has not only honed my technical skills but has also ignited a fire within me to explore the limitless 
possibilities of software development.

The Calculator GUI aims to provide you with a reliable and intuitive tool for all your mathematical needs. 
Whether you're a student, professional, or simply someone who enjoys crunching numbers, this calculator is 
designed to make your calculations swift and accurate. This application has covered some basic arithmetic 
operations only.

My vision for this calculator is to create a user-friendly experience that allows anyone, regardless of their 
coding expertise, to easily perform calculations with confidence. I hope that this tool will not only assist 
you in your daily mathematical tasks but also inspire you to delve further into the fascinating world of 
computer programming.

Thank you for joining me on this exciting journey as I take my first steps into the realm of coding. Your 
support and feedback are invaluable to me as I continue to learn and grow. Feel free to explore the various 
features of this calculator GUI, and may it bring simplicity and efficiency to your mathematical endeavors.

Happy calculating!
Rajan Poudel
        """

        help_label = tk.Label(self, text=about_text, justify=tk.LEFT)
        help_label.pack(padx=10, pady=10)

class RatingDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Rate Me")
        self.resizable(False,False)
        self.stars = 0
        self.ico = Image.open('rate.png')
        self.photo = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.photo)

        self.star_labels = []
        for i in range(5):
            star_label = tk.Label(self, text="★", font=("Arial", 20))
            star_label.pack(side=tk.LEFT, padx=5)
            star_label.bind("<Enter>", lambda event, index=i: self.on_star_enter(event, index))
            star_label.bind("<Leave>", self.on_star_leave)
            star_label.bind("<Button-1>", lambda event, index=i: self.on_star_click(event, index))
            self.star_labels.append(star_label)

    def on_star_enter(self, event, index):
        for i in range(index + 1):
            self.star_labels[i].config(fg="gold")

    def on_star_leave(self, event):
        self.update_stars()

    def on_star_click(self, event, index):
        self.stars = index + 1
        self.update_stars()
        tmsg.showinfo("Thank You", "Thank you for rating the application with {} stars!".format(self.stars))
        f = open("ratings.txt","a")
        f.write(f"Rating : {self.stars} \n")
        f.close()
        self.destroy()

    def update_stars(self):
        for i in range(5):
            if i < self.stars:
                self.star_labels[i].config(fg="gold")
            else:
                self.star_labels[i].config(fg="black")

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"366x619")
        self.title("Calculator - By Rajan Poudel")
        # self.resizable(False,False)
        self.configure(background="Black")
        self.ico = Image.open('app.png')
        self.photo = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.photo)

   
    def review(self):
       self.statusvar.set ("Status : Reviewing...")
       self.sbar. update ( )
       review = simpledialog.askstring("Review Me", "Please provide your feedback , review or complains . I will get to you soon")
       if review=='':
          pass
       elif review is not None:
            f = open("review.txt","a")
            f.write(f"Review : {review} \n")
            f.close()
            tmsg.showinfo("Thank You", "Thank you for the review and feedback!")
       self.statusvar.set ("Status : OK")
       self.sbar. update ( )
    def menu(self):
        
        self.menubar=Menu(self,tearoff=0,relief="flat")
        self.historymenu = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="History",menu=self.historymenu)
        self.menubar.add_command(label="About",command=lambda: About(self))
        self.menubar.add_command(label="Help",command=lambda: HelpDialog(self))
        self.menubar.add_command(label="Exit",command=self.exit)
        self.menubar.add_command(label="Rate Me",command=self.rate_me)
        self.menubar.add_command(label="Review",command=self.review)
        self.menubar.configure(bg="Grey")
        self.config(menu=self.menubar)

    def exit(self):
        self.statusvar.set ("Status : Quiting...")
        self.sbar. update ( )
        tmsg_value=tmsg.askquestion("Exit","Wanna Exit The Application ?")
        if tmsg_value == "yes":
            self.destroy()
        else:
          self.statusvar.set ("Status : OK")
          self.sbar. update ( )

    def calc_screen(self):
        self.scvalue = StringVar()
        self.scvalue.set ("")
        self.screen = Entry(self, textvar=self.scvalue,font="lucida 40 bold",relief=FLAT,fg="White",insertbackground="White")
        self.screen.configure(bg="#0C2340")
        self.screen.pack (fill=X, ipadx=8, pady=10, padx=10)  
       
    def buttons_frame(self):
        a = 0
        buttons = [7,8,9,"+",4,5,6,"-",1,2,3,"*",0,".","%","/","00","C","="]
        for i in range(1,6):
          self.frame = Frame (self, bg="Black")
          for i in range(0,4):
            if (i+a ==19):
               continue
            self.button=Button(self.frame, text=buttons[i+a], font="lucida 35 bold",bg="Cyan",fg="White",relief=FLAT,activebackground="Red")
            self.button.pack(side=LEFT,ipadx=10,ipady=5,padx=10,pady=10)
            self.button.bind("<Button-1>",self.click)
          self.frame.pack ()
          a = a + 4
        
    def submenu_clicked(self,text):
       self.scvalue.set(text)
       self.screen.update()
    
    def click(self,event):
        clicked_button = str(event.widget.cget("text"))
        if clicked_button == "=":
         self.statusvar.set ("Status : Calculating...")
         self.sbar.update ( )
         try:
          if self.scvalue.get().isdigit():
             value = int(self.scvalue.get())
          else:
             value = eval(self.scvalue.get())
          a = self.scvalue.get()
          self.historymenu.add_command(0,label=self.scvalue.get(),command=lambda:self.submenu_clicked(f"{a}"))

          self.scvalue.set(value)
          self.screen.update()
          self.statusvar.set("Status : OK")
          self.sbar.update ( )
         except Exception as e :
            self.statusvar.set("Status : Oops , Error :(")
            self.sbar.update ( )
            tmsg.showerror("Error","Sorry ! Couldn't evaluate")

            self.scvalue.set("")
            self.statusvar.set("Status : OK")
            self.sbar.update ( )
        elif clicked_button == "C":
          self.scvalue.set ("")
          self.screen.update()
        else:
         self.scvalue.set(self.scvalue.get()+clicked_button)
         self.screen.update()

    def status(self):
        self.statusvar = StringVar()
        self.statusvar.set("Status : OK")
        self.sbar = Label(self,textvariable=self.statusvar,anchor="e",bg= "gray51")
        self.sbar.pack(side=BOTTOM,fill=X)

    def rate_me(self):
      self.statusvar.set ("Status : Rating...")
      self.sbar. update ( )
      rating_dialog = RatingDialog(self)
      self.stat()

    def stat(self):
        self.statusvar.set ("Status : OK")
        self.sbar. update ( )

if __name__ == "__main__":
    window = GUI()
    window.menu()
    window.calc_screen()
    window.buttons_frame()
    window.status()
    window.mainloop()
