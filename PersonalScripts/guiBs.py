import tkinter as tk
from tkinter import scrolledtext
import json

def create_gui(execute_code):
    # Create the main window
    root = tk.Tk()
    root.title("Python Code Executor")
    root.geometry("2000x1500")  # Increased window size to make it bigger

    # Create a frame to hold both the text input and result areas
    main_frame = tk.Frame(root)
    main_frame.pack(expand = True, fill = "both")

    # Create the left section for text input
    left_frame = tk.Frame(main_frame)
    left_frame.pack(side = "left", padx = 30, pady = 30, fill = "both", expand = True)

    # Create the right section for result display
    right_frame = tk.Frame(main_frame)
    right_frame.pack(side = "right", padx = 30, pady = 30, fill = "both", expand = True)

    # Add a title label on the left
    title_label = tk.Label(left_frame, text = "Python Code Executor", font = ("Arial", 24))
    title_label.pack(pady = 20)

    # Create the text area for multi-line input (make it larger)
    text_area = scrolledtext.ScrolledText(left_frame, width = 30, height = 15, font = ("Arial", 30), fg = "#333")
    text_area.pack(pady = 20)

    # Create the text area for multi-line input (make it larger)
    res_data = scrolledtext.ScrolledText(left_frame, width = 30, height = 15, font = ("Arial", 30), fg = "#333")
    res_data.pack(pady = 20)

    # Create the execute button
    exec_button = tk.Button(right_frame, text = "Execute", font = ("Arial", 30), command = execute_code, fg = "white", relief = "raised", padx = 30, pady = 15)
    exec_button.pack()

    # Create a label for the right section to indicate result area
    result_label = tk.Label(right_frame, text = "Execution Result", font = ("Arial", 30))
    result_label.pack(pady = 20)

    # Create the text area for displaying results (make it larger)
    result_area = scrolledtext.ScrolledText(right_frame, width = 60, height = 700, font = ("Arial", 30), fg = "#333")
    result_area.pack(pady = 20)
    return root, text_area, result_area, res_data

def divide_data(cleaned_string):
    json_index = cleaned_string.index('{"count"')
    log_part = cleaned_string[:json_index]
    json_part = cleaned_string[json_index:]
    return log_part, json.dumps(json.loads(json_part), indent=4)
   