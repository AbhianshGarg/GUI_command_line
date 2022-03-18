# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

#runs command
def do_command(command):
    global command_textbox, url_entry
    #deletes past terminal output and shows message while running command
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    # use url_val to print output in textbox
    p = subprocess.Popen(command + " " + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)


def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()


frame_URL = tk.Frame(root, pady=10,  bg="grey") # change frame color
frame_URL.pack()
# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("times new roman", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="white",
    bg="grey")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("times new roman", 12)) # change font
url_entry.pack(side=tk.LEFT)


frame = tk.Frame(root,  bg="grey") # change frame color
frame.pack()


command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()


ping_btn = tk.Button(frame, text="Check URL Ping", command=lambda:do_command('ping'))
ping_btn.pack()

tracert_btn = tk.Button(frame, text="URL Tracert", command=lambda:do_command('tracert'))
tracert_btn.pack()

nslookup_btn = tk.Button(frame, text="URL nslookup", command=lambda:do_command('nslookup'))
nslookup_btn.pack()

save = tk.Button(frame, text="Save", command=lambda:mSave())
save.pack()

root.mainloop()
