#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This work is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
 To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/4.0/.
"""

# importing liberaries 
from Tkinter import *
import ttk
import yaml

class Application(Frame):

    def __init__(self, master):
        
        # initialize the frame
        Frame.__init__(self, master)
        self.parent = master
        self.grammar = None
        self.grammar_keys = []
        self.load_data_file()
        self.create_widgets()
        self.grid()

    def load_data_file(self):
        # loading the yaml file
        with open('data.yaml', 'r') as f:
            self.grammar = yaml.load(f)['grammar']
        for i in self.grammar:
            for x in i.keys():
                self.grammar_keys.append(x)

    def button_action(self):
        key = self.box_value.get()
        for i in self.grammar:
            if key in i.keys():
                txt = ''
                for x in i[key]['description']:
                    txt += x
                self.text.delete('1.0', END)
                self.text.insert(INSERT, txt)

    def create_widgets(self):
        # creat menu
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value)
        self.box['values'] = self.grammar_keys
        self.box.current(0)
        self.box.grid(column=0 ,row=0 ,sticky=E)
        
        # the sign
        self.instruction = Label(self, text = "Choose the grammar:")
        self.instruction.grid(row =0 , column =0 ,sticky = W)
        
        # maker label
        self.maker = Label(self , text = "Made by Abdelrahman Bonna\nUnder CC license\nvisit http://creativecommons.org/licenses/by-nc/4.0/")
        self.maker.grid(row=4 , column =0 )

        
        # the button that do the job when clicked
        self.submit_button = Button(self , text = "Enter" , command = self.button_action )
        self.submit_button.grid( row = 1 , column =0 ,sticky = W)

        # the text box that shows the message
        self.text = Text(self, width = 80 , height = 20, wrap = WORD)
        self.text.grid(row = 3 , column = 0 , sticky = E )

# getting everything to work in the window
if __name__ == '__main__':
    root = Tk()
    root.title("ENGram")
    root.geometry("570x420")
    app = Application(root)
    root.mainloop()
