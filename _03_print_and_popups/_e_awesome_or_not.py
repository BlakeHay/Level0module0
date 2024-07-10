from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    number = random.randint(0, 3)
    print(number)
    is_it_awsome =  simpledialog.askstring(title= "Is It Awsome?" , prompt= "Please enter something /n "
                                                                            "you think is awsome. ")
    if number == 0:
        messagebox.showinfo(message= "Oh yes, it is")
    if number == 1:
        messagebox.showinfo(message= "it's ok.")
    if number == 2:
        messagebox.showinfo(message= "I don't like it!!!")
    if number == 3:
        messagebox.showinfo(message= "Come on dude that's NOT COOL!!!!!!!!!")
    # Make a new window variable, window = Tk()
    
    # Hide the window using the window's .withdraw() method

    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    
    # 2. Print your variable to the console
    
    # 3. Get the user to enter something that they think is awesome
    
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
        
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
    window.mainloop()
