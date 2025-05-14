#sample test test
#ui element
# calculate the sccuracy
#run the app
import tkinter as tk
from time import time
import random

#text section
text= [
    "the quick brown fox jump over the lazy dog",
    "python is the my most favorite language",
    "typing speed i am slow as a turtle",
]

#classs
class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        root.title("Typing speed test")
        self.sample_text =random.choice(text)
        self.start_time = None

        # ui element
        self.label = tk.Label(root, text="type the text below", font=("arial", 15))
        self.label.pack(pady=10)

        self.textlabel =tk.label(root ,text=self.sample_text,font=("arial", 13) wraplength=400)
        self.textlabel.pack(pady=10)

        self.entry = tk.Entry(root, width=40, font=("arial", 13))
        self.entry.pack(pady=10)
        self.entry.bind("<focusIn>",self.start_timer)
        self.entry.bind("<Return",self.check_result)

        self.result_label = tk.Label(root, text="", font=("arial", 14))
        self.result_label.pack(pady=10)

        self.reset_button =tk.Label(root,text="reset",command =self.reset)
        self.reset_button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time == None:
            self.start_time = time()
    def check_result(self, event):
            end_time = time()
            type_text = self.entry.get()
            time-taken = end_time - self.start_time
            word = len(typed_text_split())
            wpm = words/(time_taken //60)

    #calculate the accoracy
            correct_char = sum(for a,b in zip(type_text,self.sample_text) if a==b)
            accuracy = correct_char/len(self.sample_text)

            self.result_label.config(
                text = f"wpm: {wpm:2f}\nAccuracy:{accuracy: .2f}%\nTime:{time_taken:.2f}s"
            )


    def reset(self):
        self.sample_text =random.choice(text)
        self.text_label.config(text=self.sample_text)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None

        #run the app


root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()