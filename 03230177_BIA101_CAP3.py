#https://github.com/03230210/03230210_BIA101_CAP3.PY
#PEMA TASHI 
#03230210
#BBIB 
#REFERENCES 
#https://www.w3schools.com/python/
#https://www.w3schools.com/python/module_os.asp
#https://www.geeksforgeeks.org/python-turtle-tutorial/
#SOLUTION :<490401>


import tkinter as tk
import os

def calculate_answer(file_name):
    if not os.path.isfile(file_name):
        return "Error: File not found"

    total_sum = 0
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            digits = [char for char in line if char.isdigit()]
            if digits:
                first_digit = digits[0]
                last_digit = digits[-1]
                two_digit_number = int(first_digit + last_digit)
                total_sum += two_digit_number
    if total_sum == 0:
        return ""
    else:
        return total_sum

def create_gui(answer, file_name):
    root = tk.Tk()
    root.title("Output Screen")
    root.geometry("300x100+10+10")

    if isinstance(answer, int):
        answer_label = tk.Label(root, text=f"The answer calculated from {file_name} is: {answer}")
    elif answer:
        answer_label = tk.Label(root, text=answer)
    else:
        answer_label = tk.Label(root, text="Error: No valid digits found in the file")

    answer_label.pack()
    root.mainloop()  # Start the event loop

def main():
    index_number = '210'
    if not isinstance(index_number, str) or len(index_number) < 3:
        print("Error: Invalid index number")
        return

    last_three_digits = index_number[-3:]
    file_name = last_three_digits + '.txt'

    answer = calculate_answer(file_name)
    create_gui(answer, file_name)

if __name__ == "__main__":
    main()