import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- DATASET ---------------- #

tech_data = {
    "Track": [
        "Artificial Intelligence",
        "Web Development",
        "Data Science",
        "Cyber Security",
        "Cloud Computing"
    ],

    "Skills": [
        "Python Machine Learning Deep Learning TensorFlow PyTorch AI",
        "HTML CSS JavaScript React Node Web Frontend Backend",
        "Python Pandas NumPy Data Analysis Visualization Statistics",
        "Ethical Hacking Network Security Linux Penetration Testing",
        "AWS Azure Docker Kubernetes DevOps Cloud"
    ]
}

df = pd.DataFrame(tech_data)

# ---------------- TF-IDF MODEL ---------------- #

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Skills"])

# ---------------- FUNCTIONS ---------------- #

def recommend():

    user_interest = entry_box.get().strip()

    if not user_interest:
        return

    user_vector = vectorizer.transform([user_interest])

    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    )

    scores = similarity_scores.flatten()

    top_indices = scores.argsort()[-3:][::-1]

    result_box.delete("1.0", tk.END)

    result_box.insert(
        tk.END,
        f"🔍 Interest: {user_interest}\n\n"
    )

    result_box.insert(
        tk.END,
        "🚀 Top Recommendations\n\n"
    )

    rank = 1

    for i in top_indices:

        percentage = scores[i] * 100

        result_box.insert(
            tk.END,
            f"{rank}. {df.iloc[i]['Track']}\n"
            f"   Match Score: {percentage:.2f}%\n\n"
        )

        rank += 1


def clear_all():
    entry_box.delete(0, tk.END)
    result_box.delete("1.0", tk.END)


# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Tech Stack Recommender")
root.geometry("950x650")
root.configure(bg="#202123")

# ---------------- HEADER ---------------- #

title = tk.Label(
    root,
    text="🚀 Tech Stack Recommender",
    font=("Arial", 22, "bold"),
    bg="#202123",
    fg="white"
)

title.pack(pady=15)

welcome = tk.Label(
    root,
    text="Welcome, Hannia! 👋",
    font=("Arial", 14),
    bg="#202123",
    fg="#aaaaaa"
)

welcome.pack()

subtitle = tk.Label(
    root,
    text="Discover the best technology track based on your interests.",
    font=("Arial", 11),
    bg="#202123",
    fg="#cccccc"
)

subtitle.pack(pady=(0, 20))

# ---------------- INPUT ---------------- #

input_frame = tk.Frame(root, bg="#202123")
input_frame.pack(fill="x", padx=20)

label = tk.Label(
    input_frame,
    text="Enter your interests:",
    font=("Arial", 12),
    bg="#202123",
    fg="white"
)

label.pack(anchor="w")

entry_box = tk.Entry(
    input_frame,
    font=("Arial", 13),
    bg="white",
    fg="black"
)

entry_box.pack(fill="x", pady=10, ipady=8)

# ---------------- BUTTONS ---------------- #

button_frame = tk.Frame(root, bg="#202123")
button_frame.pack(pady=10)

recommend_btn = tk.Button(
    button_frame,
    text="Recommend",
    command=recommend,
    bg="#19C37D",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)

recommend_btn.pack(side="left", padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_all,
    bg="#444654",
    fg="white",
    font=("Arial", 11),
    width=15
)

clear_btn.pack(side="left", padx=10)

# ---------------- RESULTS ---------------- #

result_box = scrolledtext.ScrolledText(
    root,
    font=("Arial", 11),
    bg="#343541",
    fg="white",
    wrap=tk.WORD
)

result_box.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

result_box.insert(
    tk.END,
    "🎯 Enter your interests and click Recommend.\n\n"
    "Examples:\n"
    "- AI Machine Learning\n"
    "- Web Development\n"
    "- Data Analysis\n"
    "- Ethical Hacking\n"
    "- Cloud AWS\n"
)

# Press Enter to Recommend
entry_box.bind("<Return>", lambda event: recommend())

entry_box.focus()

root.mainloop()
