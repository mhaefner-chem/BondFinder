# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:13:20 2024

@author: bt308570
"""


def multisplit(original_string, splitters):
    
    splitted_string = [original_string]
    for splitter in splitters:
        tmp = []
        for string in splitted_string:
            for item in string.split(splitter):
                tmp.append(item)
        splitted_string = tmp
    
    return splitted_string  

def range_extender(original_string):
    
    expanded_string = []
    
    if "-" in original_string:
        splitted_string = original_string.split("-")
        for i in range(int(splitted_string[0]),int(splitted_string[1])+1):
            expanded_string.append(str(i))
    else:
        expanded_string = [original_string]
    
    return expanded_string
        
# creates the search and request window
class main_window:
    
    # initializes the base window
    def __init__(self):
        
        self.version = "0.5.0"
        self.icon = "" # obsolete, for compatibility
        
        self.d_init = 2.5
        self.d = 0
        self.delta_d_init = 0.1
        self.delta_d = 0.0
        
        self.pairings = []
        self.data = []
        
        
        
        self.root = create_window("450x350+120+120","BondFinder")
        self.frame_entry_fields()
        self.frame_upper_buttons()
        self.frame_output()
        self.frame_buttons()
        self.root.mainloop()        
        
     
    # frame holding the buttons for file management and plotting
    def frame_entry_fields(self):
        
        
        
        def entry_fields_d():
            self._frame_distance = tk.Frame(self.root)
            self._frame_distance.pack(side=tk.TOP,fill=tk.Y,expand=False)
            # label, entry for Jagodszinski notation
            self._label_distance = ttk.Label(self._frame_distance,width=24)
            self._label_distance["text"] = "Distance in Å, blank for all:"
            self._label_distance.pack(side=tk.LEFT)
            
            self.distance = tk.StringVar()
            self._entry_distance = ttk.Entry(
                self._frame_distance,
                textvariable=self.distance,
                width=8
            )
            self._entry_distance.insert(tk.END, self.d_init)
            self._entry_distance.pack(side=tk.LEFT)
            
        def entry_fields_delta():
            self._frame_delta = tk.Frame(self.root)
            self._frame_delta.pack(side=tk.TOP,fill=tk.Y,expand=False)
            # label, entry for Jagodszinski notation
            self._label_delta = ttk.Label(self._frame_delta,width=24)
            self._label_delta["text"] = "Allowed deviation in Å:"
            self._label_delta.pack(side=tk.LEFT)
            
            self.delta = tk.StringVar()
            self._entry_delta = ttk.Entry(
                self._frame_delta,
                textvariable=self.delta,
                width=8
            )
            self._entry_delta.insert(tk.END, self.delta_d_init)
            self._entry_delta.pack(side=tk.LEFT)    
        
        def entry_fields_ions():
            self._frame_ions = tk.Frame(self.root)
            self._frame_ions.pack(side=tk.TOP,fill=tk.Y,expand=False)
            # label, entry for cation and anion
            self._label_cation = ttk.Label(self._frame_ions,width=30)
            self._label_cation["text"] = "Cation (e.g., Cu, blank for all):"
            self._label_cation.pack(side=tk.LEFT)
            
            self.cation = tk.StringVar()
            self._entry_cation = ttk.Entry(
                self._frame_ions,
                textvariable=self.cation,
                width=12
            )
            self._entry_cation.pack(side=tk.LEFT)   
            
            self._label_anion = ttk.Label(self._frame_ions,width=14)
            self._label_anion["text"] = "Anion:"
            self._label_anion.pack(side=tk.LEFT)
            
            self.anion = tk.StringVar()
            self._entry_anion = ttk.Entry(
                self._frame_ions,
                textvariable=self.anion,
                width=12
            )
            self._entry_anion.pack(side=tk.LEFT) 
            
        def entry_fields_charges():
            self._frame_charges = tk.Frame(self.root)
            self._frame_charges.pack(side=tk.TOP,fill=tk.Y,expand=False)
            
            self._label_chg_cation = ttk.Label(self._frame_charges,width=30)
            self._label_chg_cation["text"] = "Charge of cation (blank for all):"
            self._label_chg_cation.pack(side=tk.LEFT)
            
            self.chg_cation = tk.StringVar()
            self._entry_chg_cation = ttk.Entry(
                self._frame_charges,
                textvariable=self.chg_cation,
                width=12
            )
            self._entry_chg_cation.pack(side=tk.LEFT)   
            
            self._label_chg_anion = ttk.Label(self._frame_charges,width=14)
            self._label_chg_anion["text"] = "Charge anion:"
            self._label_chg_anion.pack(side=tk.LEFT)
            
            self.chg_anion = tk.StringVar()
            self._entry_chg_anion = ttk.Entry(
                self._frame_charges,
                textvariable=self.chg_anion,
                width=12
            )
            self._entry_chg_anion.pack(side=tk.LEFT) 
            
        def entry_fields_CN():
            self._frame_CN = tk.Frame(self.root)
            self._frame_CN.pack(side=tk.TOP,fill=tk.Y,expand=False)
            # label, entry for cation and anion
            self._label_CN_cation = ttk.Label(self._frame_CN,width=30)
            self._label_CN_cation["text"] = "CN Cation (blank for all):"
            self._label_CN_cation.pack(side=tk.LEFT)
            
            self.CN_cation = tk.StringVar()
            self._entry_CN_cation = ttk.Entry(
                self._frame_CN,
                textvariable=self.CN_cation,
                width=12
            )
            self._entry_CN_cation.pack(side=tk.LEFT)   
            
            self._label_CN_anion = ttk.Label(self._frame_CN,width=14)
            self._label_CN_anion["text"] = "CN Anion:"
            self._label_CN_anion.pack(side=tk.LEFT)
            
            self.CN_anion = tk.StringVar()
            self._entry_CN_anion = ttk.Entry(
                self._frame_CN,
                textvariable=self.CN_anion,
                width=12
            )
            self._entry_CN_anion.pack(side=tk.LEFT)   
            
            
        entry_fields_d()
        entry_fields_delta()
        entry_fields_ions()
        entry_fields_charges()
        entry_fields_CN()
    
    def frame_upper_buttons(self):
        
        self._frame_upper_buttons = tk.Frame(self.root)
        self._frame_upper_buttons.pack(side=tk.TOP,fill=tk.X)
        
        self._button_reset = ttk.Button(self._frame_upper_buttons, text = 'Reset', command = lambda : reset())
        self._button_reset.pack(side=tk.LEFT,expand=True)
        
        def reset():
            self._entry_distance.delete(0, 'end')
            self._entry_distance.insert(tk.END, self.d_init)
            
            self._entry_delta.delete(0, 'end')
            self._entry_delta.insert(tk.END, self.delta_d_init)
            
            self._entry_cation.delete(0, 'end')
            self._entry_anion.delete(0, 'end')
            self._entry_chg_cation.delete(0, 'end')
            self._entry_chg_anion.delete(0, 'end')
            self._entry_CN_cation.delete(0, 'end')
            self._entry_CN_anion.delete(0, 'end')
        

        
    def frame_output(self):
        
        # message to be displayed in the text box
        message = "Program ready.\n"
        if len(self.pairings) > 0:
            
            
            message += "{:6} {:3} {:3} {:6} {:3} {:3} {:>6} {:6}\n".format("Cation","Ox.","CN","Anion","Ox.","CN","d","Δ d_orig")
            for pairing in self.pairings:
                
                if abs(self.d-pairing[2]) < float(self.delta.get()) or self.d < 0.001:
                    oxstate_cat = self.data[pairing[0]]["oxstate"]
                    oxstate_an = self.data[pairing[1]]["oxstate"]
                    CN_cat = self.data[pairing[0]]["CN"]
                    CN_an = self.data[pairing[1]]["CN"]
                    label_cat = self.data[pairing[0]]["label"]
                    label_an = self.data[pairing[1]]["label"]
                    
                    message += "{:6} {:3} {:3} {:6} {:3} {:3} {:6.3f} {:6.3f}".format(label_cat,oxstate_cat,CN_cat,label_an,oxstate_an,CN_an,pairing[2],self.d-pairing[2])
                    message += "\n"
        
        self.text_frame = tk.Frame(self.root, bg="white")
        self.text_frame.pack(expand=True, fill=tk.BOTH)
        
        self.text_box = tk.Text(self.text_frame, wrap = "word",height=10,width=32)
        self.text_box.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        
        scrbar = ttk.Scrollbar(
            self.text_frame,
            command=self.text_box.yview)
        
        self.text_box["yscrollcommand"] = scrbar.set
        self.text_box.insert('1.0', message)
        self.text_box.config(state='disabled')
        scrbar.pack(side=tk.LEFT, fill=tk.Y)
        

        
    # frame holding the About button
    def frame_buttons(self):
        self._frame_buttons = tk.Frame(self.root)
        self._frame_buttons.pack(side=tk.BOTTOM,fill=tk.X)
        
        sep = ttk.Separator(self._frame_buttons,orient='horizontal')
        sep.pack(side=tk.TOP,fill=tk.X)
        
        # button for pair info
        self._button_info_structure = ttk.Button(self._frame_buttons, text = 'Generate Pairs', command = lambda : get_pairings())
        self._button_info_structure.pack(side=tk.LEFT,expand=True)
    
    
        def get_pairings():
            try:
                d = float(self.distance.get())
            except:
                d = 0
            self.d = d
            
            data = []
            data_filename = "BondLengths.csv"
            
            with open(data_filename,mode="r") as f:
                lines = f.readlines()
                for line in lines:
                    
                    if not "#" in line:
                        tmp = line.split(",")
                        if not tmp[8] == "":
                            data.append({"label":tmp[1],"oxstate":int(tmp[2]),"CN":tmp[4],"spin":tmp[5],"r":float(tmp[8])})
                        
                
            self.data = data
            pairings = []
            for i in range(len(data)):
                for j in range(len(data)):
                    if np.sign(data[i]["oxstate"]) > -1 and np.sign(data[j]["oxstate"]) < 1:
                        
                        # separators for entries
                        separators = [" ",","]
                        
                        cations = multisplit(self.cation.get(),separators)
                        anions = multisplit(self.anion.get(),separators)
                        
                        if data[i]["label"] in cations or cations == [""]:
                            if data[j]["label"] in anions or anions == [""]:
                                
                                chg_cations = []
                                for item in multisplit(self.chg_cation.get(),separators):
                                    try:
                                        chg_cations.append(int(item))
                                    except:
                                        chg_cations.append(item)
                                chg_anions = []
                                for item in multisplit(self.chg_anion.get(),separators):
                                    try:
                                        chg_anions.append(int(item))
                                    except:
                                        chg_anions.append(item)
                                
                                
                                if data[i]["oxstate"] in chg_cations or chg_cations == [""]:
                                    if data[j]["oxstate"] in chg_anions or chg_anions == [""]:
                                        
                                        CN_cations = multisplit(self.CN_cation.get(),separators)
                                        CN_anions = multisplit(self.CN_anion.get(),separators)
                                        
                                        if not CN_cations == [""]:
                                            tmp = []
                                            for CN_cation in CN_cations:
                                                for item in range_extender(CN_cation):
                                                    tmp.append(item)
                                            CN_cations = []
                                            for item in tmp:
                                                CN_cations.append(item)
                                            
                                        if not CN_anions == [""]:
                                            tmp = []
                                            for CN_cation in CN_anions:
                                                for item in range_extender(CN_cation):
                                                    tmp.append(item)
                                            CN_anions = []
                                            for item in tmp:
                                                CN_anions.append(item)
                                        
                                        
                                        if str(data[i]["CN"]) in CN_cations or CN_cations == [""]:
                                            if str(data[j]["CN"]) in CN_anions or CN_anions == [""]:
                                                pairings.append((i,j,data[i]["r"]+data[j]["r"]))
                                
                        
            self.pairings = pairings
            # while True:
            # for pairing in pairings:
            #     if abs(d-pairing[2]) < 0.02:
            #         print(data[pairing[0]]["label"],data[pairing[1]]["label"],pairing[2],d-pairing[2])
            self.text_frame.destroy()
            self.frame_output()

        # button for showing the help window
        self._button_help = ttk.Button(self._frame_buttons, text = 'Help', command = lambda : helpbox())
        self._button_help.pack(side=tk.LEFT,expand=True)
        
        def helpbox():
            helpbox = create_window("650x400+120+120", "Help",self.icon)
            helpbox.config(bg='#AAAAAA')
            
            message ='''BondFinder does things.
Version {}
   
'''.format(self.version)
            text_box = tk.Text(helpbox, wrap = "word")
            text_box.pack(expand=True,fill=tk.X)
            text_box.insert('end', message)
            text_box.config(state='disabled')
        
        # button that displays a window with the program version, license, and brief description
        about_button = ttk.Button(
            self._frame_buttons,
            text='About',
            command = lambda: about()
            )
        about_button.pack(side=tk.LEFT,expand=True)
        
        def about():
            about = create_window("650x400+120+120", "About BondFinder",self.icon)
            about.config(bg='#AAAAAA')
            message ='''BondFinder does things.
Version {}
'''.format(self.version)
# LICENSE:
# MIT License
# Copyright (c) 2024 mhaefner-chem
# Contact: michael.haefner@uni-bayreuth.de

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# FURTHER LICENSE INFORMATION:


            text_box = tk.Text(about, wrap = "word")
            text_box.pack(expand=True,fill=tk.X)
            text_box.insert('end', message)
            text_box.config(state='disabled')

# function that ensures that the created windows do not become bigger than the screen
def window_size_limiter(avail_wxh,req_wxh,req_offset_xy):

    actual_wxh = [0,0]
    actual_offsets = [0,0]
    
    # check whether window fits on the current screen with and without offsets
    for i in range(len(avail_wxh)):
        if req_wxh[i] > avail_wxh[i]:
            actual_wxh[i] = avail_wxh[i]
            print("Caution, requested window doesn't fit the screen!")
        elif req_wxh[i] + req_offset_xy[i] > avail_wxh[i]:
            actual_wxh[i] = req_wxh[i]
            actual_offsets[i] = avail_wxh[i] - req_wxh[i]
            print("Caution, requested offset would move window off the screen!")
        else:
            actual_wxh[i] = req_wxh[i]
            actual_offsets[i] = req_offset_xy[i]
    
    return actual_wxh,actual_offsets

# function that creates a new window
def create_window(dimensions="500x350+100+100", title = "Tkinter Hello World", icon = ""):
   
    w = int(dimensions.split("x")[0])
    h = dimensions.split("x")[1]
    h = int(h.split("+")[0])
    
    offset_x = int(dimensions.split("+")[1])
    offset_y = int(dimensions.split("+")[2])
    
    # initializes the Tk root window
    window = tk.Tk()
    
    # gets screen properties and centers in upper third
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    offset_x = int(screen_width/3 - w / 3)
    offset_y = int(screen_height/3 - h / 3)
    
    # makes sure the window stays within bounds
    actual_wxh, actual_offsets = window_size_limiter([screen_width,screen_height],[w,h], [offset_x,offset_y])
    
    # set a title
    window.title(title)
    
    # specify geometry and max and min measurements
    window.geometry(f"{actual_wxh[0]}x{actual_wxh[1]}+{actual_offsets[0]}+{actual_offsets[1]}")
    window.minsize(10,10)
    window.maxsize(screen_width,screen_height)
    if icon != "":
        window.iconbitmap(icon)
    
    return window

# beginning of main program
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
if __name__ == "__main__":
    
    # make window
    main = main_window()