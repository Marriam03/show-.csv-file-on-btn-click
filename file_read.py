import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Read the existing CSV file
df = pd.read_csv('book1.csv')

# Define new data
new_data = {
    'teansition id': ['1020'],
    'product id': ['20'],
    'price': ['$20.09']
}

# Create a DataFrame from the new data
new_df = pd.DataFrame(new_data)

# Append the new DataFrame to the existing one
df = pd.concat([df, new_df], ignore_index=True)
# Append data to the CSV file
df.to_csv('book1.csv', mode='a', index=False, header=False)
#print(df)
print('Data appended successfully')
def display_csv_data():
  
        # Read the CSV file
        df = pd.read_csv('book1.csv')
        # Display the DataFrame in a message box
        messagebox.showinfo("CSV Data", df.to_string(index=False))
    

# Create the main window
root = tk.Tk()
root.title("Display CSV Data")

# Create a button to display CSV data
btn_display = tk.Button(root, text="Display CSV Data", command=display_csv_data)
btn_display.pack(pady=20)

# Run the application
root.mainloop()