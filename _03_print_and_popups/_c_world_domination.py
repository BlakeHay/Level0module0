from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    window.withdraw()

    do_you_code = simpledialog.askstring(title= "quiz" , prompt= "Do you know how to code?")

    if do_you_code == "yes":
        messagebox.showinfo(message= "YOU WILL RULE THE WORLD TOMMORROW!!!!!!!!!!")
    # Hide the window using the window's .withdraw() method
        window.withdraw()

    else:
        messagebox.showinfo(message= "YOU WILL SIGN UP FOR CLASSES AT THE LEAGUE   OF AMAZING PROGAMMERS")
        window.withdraw()
    # 1. Ask the user if they know how to write code.
    
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.

    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    
    # Run the window's .mainloop() method
    window.mainloop()
