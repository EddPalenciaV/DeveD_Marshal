# Program Summary - Made by Edd Palencia Vanegas
# 1. Checks if system has python and if there are errors.
# 2. Checks if the program is running in destination address
# 3. ................

import sys
import os
import re
import fitz  # PyMuPDF
import tkinter as tk
from PIL import Image, ImageTk

# # Directory when working with system
# locate_path = os.path.dirname(os.path.realpath(__file__))
# directory = os.path.join(locate_path)

def resource_path(relative_path):
    """Get the absolute path to a resource, works for dev and for PyInstaller."""
    try:
        # Creates a temp folder and stores files there
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# LOAD SCREEN
def show_splash_screen():
    # Create the root window for the splash screen
    splash_root = tk.Tk()
    splash_root.overrideredirect(True)  # Remove window decorations (title bar, etc.)
    
    # Load the image for the splash screen
    image_path = resource_path("DdevedD 460x540.png")
    splash_image = Image.open(image_path)  # Replace with your image file
    splash_photo = ImageTk.PhotoImage(splash_image)

    # Set up the canvas to display the image
    canvas = tk.Canvas(splash_root, width=splash_image.width, height=splash_image.height)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=splash_photo)

    # Center the splash screen on the screen
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()
    x_pos = (screen_width // 2) - (splash_image.width // 2)
    y_pos = (screen_height // 2) - (splash_image.height // 2)
    splash_root.geometry(f"{splash_image.width}x{splash_image.height}+{x_pos}+{y_pos}")

    # Show the splash screen for 2 seconds
    splash_root.after(2000, splash_root.destroy)  # Destroy the splash screen after 2 seconds
    splash_root.mainloop()

# VERIFY IF CORRECT DESTINATION
def is_Destination(d):
    destCompany = "M:\Synergy\Projects"    
    if destCompany in d:
        print("This program is being executed in correct company system")
    else:
        print("\nThis program has stopped because this is not a valid system. \n\nDo not promote piracy!")
        input()
        sys.exit()

def is_currentDirectory():
    # Define the directory where the PDF files are located
    path = os.path.abspath(".")
    directory = os.path.join(path)
    return directory

def list_drawings():    
    list_of_drawings = []
    
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a PDF and contains -C-, -A-, or -S- in its name
        if filename.endswith(".pdf") and bool(re.search("-C-", filename)) or bool(re.search("-A-", filename)) or bool(re.search("-S-", filename)):
            dir_drawing = os.path.join(directory, filename)            
            list_of_drawings.append(dir_drawing)
    return list_of_drawings

def remove_revision_tags():
    
    drawings = list_drawings()

    pattern_revision_tag = r'\[[A-Za-z0-9]\] '

    for i in range(len(drawings)):
        search_pattern = re.search(pattern_revision_tag, drawings[i])
        if search_pattern:
                for j in range(len(drawings[i])):
                    if j == search_pattern.start():
                        new_name = drawings[i][:j] + drawings[i][search_pattern.end():]
                        os.rename(drawings[i], new_name)
    print("Revision tags removed from all drawings.")

def revisions_from_Drawings():
    # Get list of drawings
    list_of_drawings = list_drawings()

    revisions = []
    for item in list_of_drawings:        
        drawing = fitz.open(item)
        txt_lines = []
        for page in drawing:
            for line in page.get_text("text").splitlines():
                txt_lines.append(line)
        back_to_front = reversed(txt_lines)
        reversed_txt_lines = list(back_to_front)
        #print(reversed_txt_lines)        
        
        # Iterate through the reversed lines to find the last date and corresponding revision
        for index, value in enumerate(reversed_txt_lines):        
            # Check if the line matches the date format "DD.MM.YY"
            last_date = bool(re.fullmatch(r"\d{2}\.\d{2}\.\d{2}", value))
            # If a date is found, get the revision from three lines below and append to revisions list
            if last_date:                     
                # print(f"Index {index}: {value}")                            # Last date found
                # print("The revision is: " + reversed_txt_lines[index + 3])  # Last Revision found
                rev = reversed_txt_lines[index + 3]
                revisions.append(rev)
                break  # Exit the loop after finding the revision
    
    return revisions

def tag_drawings():
    
    drawings = list_drawings()
    revisions = revisions_from_Drawings()
    pattern_original = r"[A-Za-z]-\d{2}-\d{2}"
    pattern_A = r"[A-Za-z]-[A-Za-z]{2}-\d{2}"
    pattern_B = r"[A-Za-z]-[A-Za-z0-9]{2}-\d{2}-\d{2}"

    for i in range(len(drawings)):
        search_pattern_O = re.search(pattern_original, drawings[i])
        search_pattern_A = re.search(pattern_A, drawings[i])
        search_pattern_B = re.search(pattern_B, drawings[i])
        if search_pattern_O:
            for j in range(len(drawings[i])):
                if j == search_pattern_O.end():
                    new_name = drawings[i][:j] + " [" + revisions[i] + "]" + drawings[i][j:]
                    os.rename(drawings[i], new_name)
                    # print(f"Renamed: {drawings[i]} to {new_name}\n")
        elif search_pattern_A:
            for j in range(len(drawings[i])):
                if j == search_pattern_A.end():
                    new_name = drawings[i][:j] + " [" + revisions[i] + "]" + drawings[i][j:]
                    os.rename(drawings[i], new_name)
                    # print(f"Renamed: {drawings[i]} to {new_name}\n")
        elif search_pattern_B:
            for j in range(len(drawings[i])):
                if j == search_pattern_B.end():
                    new_name = drawings[i][:j] + " [" + revisions[i] + "]" + drawings[i][j:]
                    os.rename(drawings[i], new_name)
                    # print(f"Renamed: {drawings[i]} to {new_name}\n")
    print("All drawings have been tagged with their respective revisions.")


if __name__ == "__main__":

    #---VERIFY IF EXECUTABLE IS FROZEN
    if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))    
    

    directory = is_currentDirectory()

    #is_Destination(directory)

    remove_revision_tags()
    tag_drawings()

    # Inform user
    # print("All drawings have been tagged with their respective revisions")

    # Print Author
    # print("Created by Soft. Dev. Edd Palencia-Vanegas \nDate: 26/11/2025 \nVersion: 1.0")
    #input()