from tkinter import *
root = Tk()
root.title("Number pad")
root.geometry("400x500")
nums = [[9,8,7] , [6,5,4] , [3,2,1] ,["#" , 0 , "*"]]
for i in range (4):
    root.columnconfigure(i , weight = 1 , min_size = 80)
    root.columnconfigure(i , weight = 1 , min_size = 80)
    for j in range (0,3):
        frame  = Frame(master = root , relief = SUNKEN , borderwidth = 1)
        frame.grid(row = i , column = j)
        label = Label(master = frame , text = nums[i][j] , bg ="#00FFFF")
        label.pack(padx = 3 , pady = 3)
root.mainloop()