import webbrowser
import tkinter as tk
from tkinter import messagebox

# Function to open search results in web browser
def search():
    item = entry.get().strip()
    print(item)
    if not item:
        messagebox.showerror("Error", "Please enter an item to search.")
        return
    
    # Encode the search query for URLs
    item_query = item.replace(" ", "%20")

    # Construct search URLs (Make sure these match the real search URLs)
    urls = {
        "Blinkit": f"https://www.blinkit.com/s/?q={item_query}",
        "Zepto": f"https://www.zeptonow.com/search?q={item_query}",  # Check Zepto's URL format
        "Instamart": f"https://www.swiggy.com/instamart?query={item_query}"  # Updated Instamart URL
    }

    
    # Open each URL in the default web browser
    for platform, url in urls.items():
        webbrowser.open(url)

# Create the main window
root = tk.Tk()
root.title("Grocery Price Checker")
root.geometry("400x200")
root.resizable(False, False)

# UI Elements
label = tk.Label(root, text="Enter an item name:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search, font=("Arial", 12), bg="green", fg="white")
search_button.pack(pady=10)

# Run the application
root.mainloop()
