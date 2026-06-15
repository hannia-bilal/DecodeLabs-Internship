import tkinter as tk

responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm doing great!",
    "what is your name": "I am RuleBot.",
    "good morning": "Good morning to you too",
    "what are you doing": "replying to your questions",
    "thank you": "You're welcome!"
}

def send_message():
    user_input = entry.get().lower().strip()

    chat_box.insert(tk.END, f"You: {user_input}\n")

    if user_input == "bye":
        chat_box.insert(tk.END, "Bot: Goodbye!\n")
        root.after(1000, root.destroy)
        return

    reply = responses.get(
        user_input,
        "Sorry, I don't understand."
    )

    chat_box.insert(tk.END, f"Bot: {reply}\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Rule-Based AI Chatbot")
root.geometry("500x400")

chat_box = tk.Text(root, height=20, width=60)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=60)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

root.mainloop()