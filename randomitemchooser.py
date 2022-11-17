import tkinter as tk
import random
import platform
import os
import sys

# Get icon for window
def chooseIcon(providedWindow):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    if platform.system() == 'Windows':
        try:
            providedWindow.iconbitmap(os.path.abspath(os.path.join(bundle_dir, 'assets\icon.ico')))
        except:
            return
    else:
        try:
            unixIcon = os.path.abspath(os.path.join(bundle_dir, 'assets/icon.xbm'))
            providedWindow.iconbitmap(f'@{unixIcon}')
        except:
            return

# Create the window
window = tk.Tk()
window.title("Random Item Chooser")
chooseIcon(window)
window.geometry("600x420")
window.resizable(False, False)

# Define vars
currentItems = []
listText = tk.StringVar()
listText = "Empty"

# Create the functions
def popup_window(text):
    error_window = tk.Toplevel()
    chooseIcon(error_window)
    error_window.resizable(False, False)

    label = tk.Label(error_window, text=text)
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(error_window, text="OK", width=7, command=error_window.destroy)
    button_close.pack(anchor='e', padx=5, pady=5)

def addItemstoList(input, listText):
    itemToAdd = input.get()
    if itemToAdd == '':
        popup_window("Input field can't be empty.")
        return
    currentItems.append(itemToAdd)
    currentListValues = listText
    if currentListValues == "Empty":
        listText = itemToAdd

    else:
        listText = listText + "\n" + itemToAdd

    label_List.config(text=listText)
    return

def clearList(currentListText):
    currentItems.clear()
    listText = "Empty"
    label_List.config(text=listText)
    label_Output.config(text='')
    input_ItemEntry.delete(0,tk.END)

def highlightSelection():
    input_ItemEntry.selection_range(0, tk.END)

def chooseRandom():
    if currentItems == []:
        popup_window("You have no items in the list!")
        return

    numberToChoose = len(currentItems)
    chosenOne = random.randint(1, int(numberToChoose))
    label_Output.config(text=currentItems[chosenOne - 1])


# Create widgets

## Left Panel-Top
frame_left = tk.Frame(width=400, height=420)
frame_left.place(x=0, y=0)

## Right Panel
frame_right = tk.Frame()
frame_right.place(x=400, y=0)

## Left Panel Widgets
label_Header = tk.Label(master=frame_left, text="Random Item Chooser", anchor="n", width=19, height=1, font=("", 20))
label_Input = tk.Label(master=frame_left, text="Input:", font=("", 13))
input_ItemEntry = tk.Entry(master=frame_left, fg = "black", bg="white", width=20)
input_ItemEntry.insert(0, "")
button_InsertItem = tk.Button(master=frame_left, text="Add to List", width=9, height=1, relief=tk.RAISED, command=lambda: addItemstoList(input_ItemEntry, label_List.cget("text")))
button_ChooseRandom = tk.Button(master=frame_left, text="Choose Random", width=20, height=2, relief=tk.RAISED, command=lambda: chooseRandom())
label_OutputHeader = tk.Label(master=frame_left, text="Output:", anchor="w", font=("", 15))
label_Output = tk.Label(master=frame_left, text="", bg="darkgray", relief=tk.SUNKEN, font=("", 15), width=32, height=4)
button_ClearList = tk.Button(master=frame_left, text="Clear List", width=9, height=1, relief=tk.RAISED, command=lambda: clearList(label_List.cget("text")))

## Right Panel Widgets
label_List = tk.Label(master=frame_right, text=listText, bg="darkgray", width=34, height=27, anchor="nw", relief=tk.SUNKEN, justify="left")

# No idea what this does but everything breaks if I remove it
window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)

# Create keybinds
window.bind('<Control-a>', lambda event: highlightSelection()) # Must do this one manually because of a weird bug
window.bind('<Return>', lambda event: addItemstoList(input_ItemEntry, label_List.cget("text")))

# Load widgets
label_Header.place(x=43, y=15)
label_List.pack()
label_Input.place(x=77, y=79)
input_ItemEntry.place(x=80, y=103)
button_InsertItem.place(x=240, y=100)
button_ChooseRandom.place(x=125, y=180)
label_OutputHeader.place(x=20, y=233)
label_Output.place(x=20, y=260)
button_ClearList.place(x=10, y=380)

# Keep window running till closed
window.mainloop()