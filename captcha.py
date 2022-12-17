# Math based captcha verfication

import random
from tkinter import *
from tkinter.ttk import *
from captcha.image import ImageCaptcha
from PIL import Image,ImageTk
from tkinter import messagebox


class MathCaptcha:
    def __init__(self):
        root = Tk()
        root.title("Captcha Verification")
        self.actual = str(random.randint(1, 100)) + self.randOps() + str(random.randint(1, 100))
        print(self.actual) #For generating random string of mathmatical expression
        Label(root, text = "Math based Captcha Verification",font = "comicsansms 19 bold").pack()
        image = ImageCaptcha(fonts = ['captcha.ttf']) #Font for captcha
        data = image.generate(self.actual) 
        image.write(self.actual, "out.png") #Output image of captcha
        img = Image.open("out.png")
        w,h = img.size
        img = img.resize((w*4,h*3))
        img.save("out.png")
        photo = ImageTk.PhotoImage(img)
        Label(root, text = "Submit", image = photo).pack() #Putting image of captcha in tkinter 
        Label(root, text = "Enter the captcha:", font = "comicsansms 12 bold").pack()
        self.captchaInput = Entry(root)
        self.captchaInput.pack()
        Button(root, text = "Submit", command=self.submit).pack()
        root.mainloop()

    def randOps(self):
        ops = ('+', '-', '*', '/')
        return random.choice(ops) #For choosing random operator the list as String 

    def submit(self):
        if(int(self.captchaInput.get()) == int(eval(self.actual))): #eval() converts returns the output of mathematical expression  
            messagebox.showinfo("Alert","Captcha Verified")
        else:
            messagebox.showinfo("Alert","Incorrect Captcha")


c = MathCaptcha()
