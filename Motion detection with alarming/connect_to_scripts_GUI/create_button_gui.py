import tkinter as tk

class MyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("My GUI App")
        
        # Create a button
        self.my_button = tk.Button(root, text="Click Me!", command=self.on_button_click)
        self.my_button.pack(pady=20)
    
    def on_button_click(self):
        print("Button was clicked!")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()

