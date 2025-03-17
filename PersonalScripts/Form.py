import os
import tkinter as tk
from tkinter import scrolledtext
import subprocess
import re
from guiBs import create_gui, divide_data

# Function to handle the execution of the input in the textarea
def execute_code():
    user_input = text_area.get("1.0", tk.END).strip()  # Get input from the text area
    if user_input:
        # Write the user input to query.cypher file
        with open("./query.cypher", "w") as f:
            f.write(user_input)
        
            # Run the command and capture the output
        result = subprocess.run(
            ["/home/lroem/AeonGVT/AeonG-Pref/build/tests/mgbench/client", "--input=query.cypher", "--num-workers=1", "--queries-json=false", "--max-retries=100", "--port=7687"],
            stdout=subprocess.PIPE,  # Capture the standard output
            stderr=subprocess.PIPE   # Capture the standard error
        )
        output = result.stdout.decode('utf-8')  # Decode the output to string
        error = result.stderr.decode('utf-8')  # Decode any errors
        
        # Show the output or error in the result text area
        result_area.delete("1.0", tk.END)  # Clear previous content
        res_data.delete("1.0", tk.END)  # Clear previous content

        if output:
            cleaned_string = re.sub(r'\[.*?\] \[.*?\] \[.*?\] ', '', output)
            res_query, an_query = divide_data(cleaned_string)
            result_area.insert(tk.END, f"Output:\n{res_query}")
            res_data.insert(tk.END, f"Output:\n{an_query}")
        if error:
            result_area.insert(tk.END, f"\nError:\n{error}")
    else:
        print("No code to execute!")


root, text_area, result_area, res_data = create_gui(execute_code)
# Run the GUI application
root.mainloop()
