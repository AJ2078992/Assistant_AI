""" A short message from the creator:
    Hi! I am Aditya jain, The creator of this project.
    This project has some lines of code that were inspired from some places, rest was all made by me.
    If you want to run this from .pyw file then run this in command prompt:
    pip install google
    """


#Importing the "Assets" module
from Assets import *
#Input_var declaration
Input_var=str()
#Tkinter setup
root=Tk()

# Setting up the output label
global Output_var
Output_var=StringVar()
Output_label=Label(root, textvariable=Output_var, font=("SegoeUI"))
Output_label.pack(fill=BOTH, expand=YES)

dark_mode_var = BooleanVar(value=True)

def toggle_dark_mode():
    """This function will take care of dark and light mode."""
    if dark_mode_var.get():
        root.configure(background="#2A2A2A")
        Output_label.configure(bg="#2A2A2A",fg="white")
        Input_frame.configure(bg="#4A4A4A")
        Input_Label.configure(fg="white", bg="#4A4A4A")
        Input_Entry.configure(fg="white", bg="#4A4A4A")
    else:
        root.configure(background="#F2F2F2")
        Output_label.configure(bg="#F2F2F2",fg="black")
        Input_frame.configure(bg="#DADADA")
        Input_Label.configure(fg="black", bg="#DADADA")
        Input_Entry.configure(fg="black", bg="#DADADA")

dark_mode_checkbox = Checkbutton(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode).pack()

# Setting up the input box
Input_frame=Frame(root)
Input_frame.pack(side=BOTTOM, fill=X)

Input_Label=Label(Input_frame, font=("Segoe UI", 20), text=">>>")
Input_Label.grid(row=0, column=0)
Input_Entry=Entry(Input_frame, font=("Segoe UI", 20))
Input_Entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
Input_frame.grid_columnconfigure(1, weight=1)

def Info():
    try:
        with open("info.txt") as file:
            name=file.read().strip()
    except FileNotFoundError as e:
        typewriter_animation()

def commands(input:str):
        """This Function will perform commands."""
        if input=="":
            pass
        elif "time" in input:
            time_var=datetime.now().strftime("It's %I:%M %p")
            typewriter_animation(time_var)
        elif "good morning" in input or "good evening" in input or "good afternoon" in input or "good night" in input:
            hour=datetime.now().hour
            if hour>=6 and hour<12:
                typewriter_animation("Good Morning!\nI wish that you have a great day!")
            elif hour>=12 and hour<16:
                typewriter_animation("Good Afternoon!\nI hope you're having a great day!")
            elif hour>=16 and hour<20:
                typewriter_animation("Good Evening!\nI hope you had a great day!")
            elif hour>=20 and hour<23:
                typewriter_animation("Good Night!\n I hope you have a good sleep!")
            else:
                typewriter_animation("I think you should sleep.")
        elif "open" in input:
            input=input.replace("open","")
            best_match = Responses.get_best_match(self=Responses,user_input=input,choices=websites.keys())
            if best_match:
                typewriter_animation(f"Opening {best_match}...")
                webbrowser.get("windows-default").open_new_tab(url=websites[best_match])
                typewriter_animation("Done!")
            else:
                typewriter_animation(f"Error: can't find {input} in my website database.")
        elif "how" in input or "what" in input or "why" in input or "where" in input or "when" in input or "search" in input:
            input=input.replace(" ","+")
            typewriter_animation("Searching...")
            webbrowser.get("windows-default").open_new_tab(url=f"https://www.google.com/search?q={input}")
            typewriter_animation("Done!")
        elif "wiki" in input:
            for results in search(query=input,stop=1,pause=0):
                pass
            typewriter_animation("Searching Wikipedia...")
            webbrowser.get("windows-default").open_new_tab(url=results)
            typewriter_animation("Done!")
        else:    
            typewriter_animation(f'''I can't understand what you mean by "{Actual_Input}"\nPlease be more specific''')


def on_enter_pressed(event):
    '''This function is called when the Enter key is pressed in the input box.'''
    output()

def scale_font(event):
    """This function scales the text according to the window size."""
    new_font_size = int(root.winfo_width()/50)
    Output_label.config(font=("Segoe UI", new_font_size))


def typewriter_animation(text:str):
    """This function will do the typewriter animation."""
    index=""
    Output_var.set("")
    for letters in text:
        index=index+letters
        Output_var.set(index)
        root.update()
        time.sleep(0.05)

#Binding functions with respective widgets.
Input_Entry.bind('<Return>', on_enter_pressed)
root.bind("<Configure>", scale_font)

def output():
    '''This function handles all the outputs.'''
    global Actual_Input
    Input_var=str(Input_Entry.get())
    Actual_Input=Input_var
    Input_Entry.delete(0,END)
    Input_var=Input_var.lower()
    try:
       Info() 
    except ValueError as e:
        commands(input=Input_var)

root.title("Assistant AI")
try:
    root.wm_iconbitmap("Icon.ico")
except Exception:
    pass
root.geometry("1000x600")
root.minsize(1000,600)

toggle_dark_mode()
typewriter_animation(text="Hello! I'm Assistant AI. An AI devloped by Aditya Jain.")
root.mainloop()