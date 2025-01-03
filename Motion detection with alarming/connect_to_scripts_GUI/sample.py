import tkinter as tk
import subprocess

def run_script():
    # Replace 'script_to_run.py' with the path to your Python script
    try:
        subprocess.run(['python', 'script_to_run.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")

# Create the main application window
root = tk.Tk()
root.title("Run Script Example")

# Create a button
run_button = tk.Button(root, text="Run Script", command=run_script)
run_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
