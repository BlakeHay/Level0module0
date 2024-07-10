from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    score = 0
    math = simpledialog.askstring(title= "Can You Do Math?" , prompt= "If in a rectangle two non-adjacent corners are 5 inches\n"
                                                                      " apart and one side length is 3 inches what's the area of the rectangle? ")


    # Make a new window variable, window = Tk()
    if math == "12":
        messagebox.showinfo(message= "Correct, score +1")
        score = score + 1
        math2 = simpledialog.askstring(title= "Can You Do Math?" , prompt= "If you had one pie with radius 9 would you trade it for two pies with radius 6?")
        if math2 == "no":
            messagebox.showinfo(message= "Correct, score +1")
            score = score + 1
            math3 = simpledialog.askstring(title= "Can You Do Math" , prompt= "3 x (9 % of 5) +3 -4 -7 2 ) x 0")
            if math3 == "0":
                messagebox.showinfo(message= "Correct, score +1")
                score = score + 1

    else:
        messagebox.showinfo(message= "Incorrect, Ur bad at math")


    messagebox.showinfo(message= "Your final score was "+ str(score)+ ". ")

    # Hide the window using the window's .withdraw() method
    
    # 1. Create a variable to hold the user's score. Set it equal to zero. 

    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    windows.mainloop()
