import tkinter as tk
from tkinter import scrolledtext

# Expert System Rules
def expert_system(user_input):

    user_input = user_input.lower()
    if 'hi' in user_input or 'hello' in user_input:
        return "Hello! How may I help you?"

    if "password" in user_input:
        return "Please reset your password using the 'Forgot Password' option."

    elif "internet" in user_input or "network" in user_input:
        return "Check your Wi-Fi connection and restart the router."

    elif "printer" in user_input:
        return "Ensure the printer is connected properly and has paper."

    elif "software" in user_input:
        return "Please reinstall the software or contact technical support."

    elif "virus" in user_input:
        return "Run a full antivirus scan on your system."

    elif "contact" in user_input:
        return "Contact Help Desk at: helpdesk@gmail.com"

    elif "bye" in user_input:
        return "Thank you for using Help Desk Expert System."

    else:
        return "Sorry! No solution available for this problem."

# Send Message Function
def send_message():

    user_message = entry_box.get()

    chat_area.insert(tk.END, "User : " + user_message + "\n")

    response = expert_system(user_message)

    chat_area.insert(tk.END, "Expert System : " + response + "\n\n")

    entry_box.delete(0, tk.END)

# GUI Window
window = tk.Tk()

window.title("Help Desk Expert System")

window.geometry("550x450")

# Chat Area
chat_area = scrolledtext.ScrolledText(window,
                                      wrap=tk.WORD,
                                      width=65,
                                      height=20)

chat_area.pack(pady=10)

# Entry Box
entry_box = tk.Entry(window, width=40)

entry_box.pack(side=tk.LEFT, padx=10, pady=10)

# Send Button
send_button = tk.Button(window,
                        text="Send",
                        command=send_message)

send_button.pack(side=tk.LEFT)

# Run Application
window.mainloop()