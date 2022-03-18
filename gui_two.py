# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import LEFT, filedialog
from tkinter.filedialog import asksaveasfilename

root = tk.Tk()
frame = tk.Frame(root)
frame.grid()

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


frame_URL = tk.Frame(root, pady=10,  bg="grey", width=25) # change frame color
frame_URL.grid(row=0, column=0, sticky='w')
# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("times new roman", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="white",
    bg="grey")
url_label.grid(row=0, column=0)
url_entry= tk.Entry(frame_URL,  font=("times new roman", 12)) # change font
url_entry.grid(row=1, column=0, pady=5)   


frame = tk.Frame(root,  bg="grey") # change frame color
frame.grid(row=1, column=0, sticky='nw')


command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.grid(row=1, column=1)


ping_btn = tk.Button(frame_URL, text="Check URL Ping", width=25, command=lambda:do_command('ping'))
ping_btn.grid(row=3, column=0, sticky='n', pady=5)

tracert_btn = tk.Button(frame_URL, text="URL Tracert", width=25, command=lambda:do_command('tracert'))
tracert_btn.grid(row=4, column=0, sticky='n')

nslookup_btn = tk.Button(frame_URL, text="URL nslookup", width=25, command=lambda:do_command('nslookup'))
nslookup_btn.grid(row=5, column=0, sticky='n', pady=5)

save = tk.Button(frame_URL, text="Save", width=25, command=lambda:mSave())
save.grid(row=6, column=0, sticky='n')

root.mainloop()