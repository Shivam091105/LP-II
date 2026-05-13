import tkinter as tk
from tkinter import scrolledtext

# Function for chatbot replies
def chatbot_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to Customer Support."

    elif "order" in user_input:
        return "Please enter your Order ID."

    elif "return" in user_input:
        return "Products can be returned within 7 days."

    elif "refund" in user_input:
        return "Refund will be processed within 5 working days."

    elif "contact" in user_input:
        return "Contact us at support@gmail.com"

    elif "bye" in user_input:
        return "Thank you! Visit again."

    else:
        return "Sorry, I did not understand."

# Function to send messages
def send_message():

    user_message = entry_box.get()

    chat_area.insert(tk.END, "You : " + user_message + "\n")

    response = chatbot_response(user_message)

    chat_area.insert(tk.END, "Bot : " + response + "\n\n")

    entry_box.delete(0, tk.END)

# GUI Window
window = tk.Tk()
window.title("Customer Support Chatbot")
window.geometry("500x400")

# Chat Area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD,
                                      width=60, height=20)
chat_area.pack(pady=10)

# Entry Box
entry_box = tk.Entry(window, width=40)
entry_box.pack(side=tk.LEFT, padx=10, pady=10)

# Send Button
send_button = tk.Button(window, text="Send",
                        command=send_message)
send_button.pack(side=tk.LEFT)

# Run Application
window.mainloop()