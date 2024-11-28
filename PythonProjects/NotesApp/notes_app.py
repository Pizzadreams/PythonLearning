import tkinter as tk
from tkinter import ttk
import os

class NoteApp:
    def __init__(self, master):
        self.master = master
        master.title("Note App")

        # Create the main frame
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create the text area
        self.text_area = tk.Text(self.frame, font=("Arial", 14))
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create the opacity slider
        self.opacity_label = tk.Label(self.frame, text="Opacity:")
        self.opacity_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.opacity_var = tk.DoubleVar(value=1.0)
        self.opacity_slider = ttk.Scale(self.frame, variable=self.opacity_var, from_=0.0, to=1.0, orient=tk.HORIZONTAL)
        self.opacity_slider.pack(side=tk.LEFT, padx=10, pady=10)

        self.opacity_slider.bind("<ButtonRelease-1>", self.update_opacity)

        # Add a "Save" button
        self.save_button = tk.Button(self.frame, text="Save", command=self.save_note)
        self.save_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def update_opacity(self, event):
        # Ensure the window doesn't completely disappear
        opacity = max(0.1, self.opacity_var.get())
        self.master.winfo_toplevel().attributes("-alpha", opacity)

    def save_note(self):
        # Get the text from the text area
        note_text = self.text_area.get("1.0", tk.END).strip()

        # Create the "storage" folder if it doesn't exist
        storage_folder = os.path.join(os.path.dirname(__file__), "storage")
        os.makedirs(storage_folder, exist_ok=True)

        # Save the note to a file in the "storage" folder
        note_file = os.path.join(storage_folder, "note.txt")
        with open(note_file, "w", encoding="utf-8") as f:
            f.write(note_text)

        print("Note saved to", note_file)


if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()