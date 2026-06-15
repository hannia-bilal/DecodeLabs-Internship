import tkinter as tk
from tkinter import scrolledtext

responses = {
    "hi": "Hello! 👋",
    "hello": "Hi there!",
    "hey": "Hey! Nice to meet you.",
    "how are you": "I'm doing great. Thanks for asking!",
    "good morning": "good morning to you too",
    "what is your name": "I am DecodeBot.",
    "who created you": "I was created for the DecodeLabs Internship.",
    "help": "Try asking: hello, how are you, what is your name.",
    "thank you": "You're welcome!",
    "thanks": "Happy to help!"
}


def send_message():
    user_input = message_entry.get().strip()

    if not user_input:
        return

    # Show user message
    chat_box.insert(tk.END, f"You: {user_input}\n")
    chat_box.see(tk.END)

    text = user_input.lower()

    if text == "bye":
        chat_box.insert(tk.END, "Bot: Goodbye! Have a nice day. 👋\n\n")
        message_entry.delete(0, tk.END)
        root.after(1500, root.destroy)
        return

    response = responses.get(text, "Sorry, I don't understand that.")

    chat_box.insert(tk.END, f"Bot: {response}\n\n")
    chat_box.see(tk.END)

    message_entry.delete(0, tk.END)


def clear_chat():
    chat_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("DecodeLabs AI Chatbot")
root.geometry("900x600")
root.configure(bg="#202123")


header = tk.Frame(root, bg="#202123")
header.pack(fill="x", pady=10)

title = tk.Label(
    header,
    text="🤖 DecodeLabs AI Assistant",
    font=("Arial", 20, "bold"),
    bg="#202123",
    fg="white"
)
title.pack()

welcome = tk.Label(
    header,
    text="Welcome 👋",
    font=("Arial", 14),
    bg="#202123",
    fg="#aaaaaa"
)
welcome.pack()

chat_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 11),
    bg="#343541",
    fg="white"
)

chat_box.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

chat_box.insert(
    tk.END,
    "🤖 DecodeBot: Welcome to your AI Chatbot!\n"
    "Type 'bye' to exit.\n\n"
)

bottom_frame = tk.Frame(root, bg="#202123")
bottom_frame.pack(fill="x", padx=15, pady=10)

message_entry = tk.Entry(
    bottom_frame,
    font=("Arial", 12),
    bg="white",
    fg="black"
)

message_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10),
    ipady=8
)

send_btn = tk.Button(
    bottom_frame,
    text="Send",
    command=send_message,
    bg="#19C37D",
    fg="white",
    width=10
)

send_btn.pack(side="left")

clear_btn = tk.Button(
    bottom_frame,
    text="Clear",
    command=clear_chat,
    bg="#444654",
    fg="white",
    width=10
)

clear_btn.pack(side="left", padx=(10, 0))

message_entry.focus()

root.mainloop()
