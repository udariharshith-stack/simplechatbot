import tkinter as tk
from tkinter import scrolledtext
import datetime
import random
import webbrowser

# -----------------------------------
# AI Chatbot Response Function
# -----------------------------------
def chatbot_response(user_input):

    user_input = user_input.lower()

    # Greetings
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    if any(word in user_input for word in greetings):
        responses = [
            "Hello! How are you doing today?",
            "Hi! Nice to meet you.",
            "Hey! How can I help you today?",
            "Hello! I'm ready to chat with you."
        ]
        return random.choice(responses)

    # Name
    elif "your name" in user_input:
        return "My name is Smart AI Bot."

    # Human feelings
    elif "i am sad" in user_input:
        return "I'm sorry to hear that. Everything will become better soon."

    elif "i am happy" in user_input:
        return "That's wonderful! Keep smiling."

    elif "i am tired" in user_input:
        return "You should take some rest and relax."

    elif "i love you" in user_input:
        return "That's sweet. I enjoy talking with you too."

    # Bot feelings
    elif "how are you" in user_input:
        return "I am doing great. Thanks for asking."

    # Time
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"

    # Date
    elif "date" in user_input:
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {today}"

    # Jokes
    elif "joke" in user_input:
        jokes = [
            "Why did the computer go to school? To improve its memory.",
            "Why was the keyboard sleeping? Because it had too many shifts.",
            "Why did Python become popular? Because it is easy to understand."
        ]
        return random.choice(jokes)

    # Motivation
    elif "motivate me" in user_input:
        return "Success comes from consistency and hard work. Keep going."

    # Thanks
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome."

    # Open websites
    elif "open google" in user_input:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."

    elif "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    elif "open chatgpt" in user_input:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT..."

    # What can you do
    elif "what can you do" in user_input:
        return "I can chat with you, tell jokes, answer questions, open websites, and perform calculations."

    # Creator
    elif "who created you" in user_input:
        return "I was created using Python programming language."

    # Calculator
    elif "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
        try:
            result = eval(user_input)
            return f"The answer is {result}"
        except:
            return "Sorry, I could not calculate that."

    # Bye
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a wonderful day."

    # Default smart replies
    else:
        smart_replies = [
            "Interesting. Tell me more.",
            "I understand.",
            "Can you explain that differently?",
            "That sounds good.",
            "I'm still learning new things.",
            "Can you give more details?",
            "That's nice to hear."
        ]

        return random.choice(smart_replies)


# -----------------------------------
# Send Message Function
# -----------------------------------
def send_message():

    user_input = entry_box.get()

    if user_input.strip() == "":
        return

    # Display user message
    chat_area.insert(tk.END, "You: " + user_input + "\n")

    # Get chatbot response
    response = chatbot_response(user_input)

    # Display bot response
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    # Clear input field
    entry_box.delete(0, tk.END)

    # Auto scroll
    chat_area.yview(tk.END)


# -----------------------------------
# Clear Chat Function
# -----------------------------------
def clear_chat():
    chat_area.delete(1.0, tk.END)


# -----------------------------------
# Dark Mode Function
# -----------------------------------
dark_mode = False

def toggle_dark_mode():

    global dark_mode

    if dark_mode:

        window.configure(bg="white")

        title_label.configure(bg="white", fg="black")

        chat_area.configure(
            bg="white",
            fg="black",
            insertbackground="black"
        )

        entry_box.configure(
            bg="white",
            fg="black",
            insertbackground="black"
        )

        dark_button.configure(text="Dark Mode")

        dark_mode = False

    else:

        window.configure(bg="#1e1e1e")

        title_label.configure(bg="#1e1e1e", fg="white")

        chat_area.configure(
            bg="#2b2b2b",
            fg="white",
            insertbackground="white"
        )

        entry_box.configure(
            bg="#3b3b3b",
            fg="white",
            insertbackground="white"
        )

        dark_button.configure(text="Light Mode")

        dark_mode = True


# -----------------------------------
# Main Window
# -----------------------------------
window = tk.Tk()

window.title("Smart AI Chatbot")

window.geometry("650x750")

window.configure(bg="white")


# -----------------------------------
# Title
# -----------------------------------
title_label = tk.Label(
    window,
    text="SMART AI CHATBOT",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="black"
)

title_label.pack(pady=10)


# -----------------------------------
# Chat Area
# -----------------------------------
chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    width=70,
    height=28,
    font=("Arial", 12)
)

chat_area.pack(padx=10, pady=10)

chat_area.insert(
    tk.END,
    "Bot: Hello! I am Smart AI Bot.\n"
    "Type something to start chatting.\n\n"
)


# -----------------------------------
# Input Frame
# -----------------------------------
input_frame = tk.Frame(window, bg="white")

input_frame.pack(pady=10)


# -----------------------------------
# Entry Box
# -----------------------------------
entry_box = tk.Entry(
    input_frame,
    width=40,
    font=("Arial", 14)
)

entry_box.grid(row=0, column=0, padx=5)


# -----------------------------------
# Send Button
# -----------------------------------
send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    width=10,
    command=send_message
)

send_button.grid(row=0, column=1, padx=5)


# -----------------------------------
# Buttons Frame
# -----------------------------------
button_frame = tk.Frame(window, bg="white")

button_frame.pack(pady=10)


# -----------------------------------
# Clear Button
# -----------------------------------
clear_button = tk.Button(
    button_frame,
    text="Clear Chat",
    font=("Arial", 12),
    bg="lightcoral",
    width=15,
    command=clear_chat
)

clear_button.grid(row=0, column=0, padx=10)


# -----------------------------------
# Dark Mode Button
# -----------------------------------
dark_button = tk.Button(
    button_frame,
    text="Dark Mode",
    font=("Arial", 12),
    bg="lightgreen",
    width=15,
    command=toggle_dark_mode
)

dark_button.grid(row=0, column=1, padx=10)


# -----------------------------------
# Enter Key Support
# -----------------------------------
window.bind("<Return>", lambda event: send_message())


# -----------------------------------
# Run Application
# -----------------------------------
window.mainloop()