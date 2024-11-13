import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text():
    # Get the input text from the user
    input_text = entry.get("1.0", "end-1c")

    # If the input text is empty, show an error
    if not input_text.strip():
        messagebox.showerror("Input Error", "Please enter some text to translate.")
        return

    try:
        # Translate the text from English to Tamil using GoogleTranslator
        translated = GoogleTranslator(source='en', target='ta').translate(input_text)
        output_text.delete("1.0", "end")  # Clear any previous output
        output_text.insert("1.0", translated)  # Display the translated text
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("English to Tamil Translator")

# Set the window size
root.geometry("400x400")

# Add a label for the input text
input_label = tk.Label(root, text="Enter Text in English:", font=("Helvetica", 12))
input_label.pack(pady=10)

# Add a Text widget for user to input text
entry = tk.Text(root, height=5, width=40, font=("Helvetica", 12))
entry.pack(pady=10)

# Add a button to trigger the translation
translate_button = tk.Button(root, text="Translate", font=("Helvetica", 12), command=translate_text)
translate_button.pack(pady=10)

# Add a label for the output text
output_label = tk.Label(root, text="Translated Text in Tamil:", font=("Helvetica", 12))
output_label.pack(pady=10)

# Add a Text widget to display the translated text
output_text = tk.Text(root, height=5, width=40, font=("Helvetica", 12), wrap="word")
output_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
