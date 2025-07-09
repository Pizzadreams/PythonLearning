import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style
from settings import UNSPLASH_API_KEY

# create the main window
root = tk.Tk()
root.title("Image Generator")
root.geometry("800x600")
root.config(bg="white")
root.resizable(False, False)
style = Style(theme="sandstone")

# define a function to retrieve and display an image based on the selected category
def display_image(category):
    # make a request to the Unsplash API to get a random image
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id={UNSPLASH_API_KEY}"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content

    # Extract image data
    img_data = requests.get(data["urls"]["regular"]).content
    artist_name = data["user"]["name"]  # Get the artist's name
    image_title = data["description"] if data["description"] else "Untitled"  
    
    photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))
    label.config(image=photo)
    label.image = photo

    # Update the attribution label
    attribution_label.config(text=f"Photo by {artist_name} on Unsplash\nTitle: {image_title}")

# function to enable/disable the "Generate Image" button
def enable_button(*args):
    generate_button.config(state="normal" if category_var.get() != "Choose Category" else "disabled")

# create the GUI elements
def create_gui():
    global category_var, generate_button, label, attribution_label

    # Dropdown for Category selection
    category_var = tk.StringVar(value="Choose Category")
    category_options = ["Choose Category", "Food", "Animals", "People", "Music", "Art", "Vehicles", "Random"]
    category_dropdown = ttk.OptionMenu(root, category_var, *category_options, command=enable_button)
    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_dropdown.config(width=14)

    # Generate Image Button
    generate_button = ttk.Button(text="Generate Image", state="disabled", command=lambda: display_image(category_var.get()))
    generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root, background="white")
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Create attribution label
    attribution_label = tk.Label(root, background="white", font=("Arial", 10))
    attribution_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    # Expandable rows/cols
    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()

if __name__ == '__main__':
    create_gui()