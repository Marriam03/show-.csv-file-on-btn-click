import pandas as pd
import tkinter as tk
from tkinter import messagebox
import os
file_path = 'book1.csv'
def append_to_csv(file_path, new_data):
    if os.path.exists(file_path):
        df= pd.read_csv(file_path)
    else:
        df=pd.DataFrame()
    new_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_df], ignore_index=False)
    df.to_csv(file_path, index=False)
   
 
def submit_data():

    col1_value= entry1.get()
    col2_value= entry2.get()
    col3_value = entry3.get()
    if col1_value and col2_value and col3_value:
        new_data = {'id':col1_value, 
                    'year':col2_value,
                    'price':col3_value
                    }
        append_to_csv(file_path, new_data)
        messagebox.showinfo('success','Data appned successfully')
    else:
        messagebox.showwarning('Input Error','complete all feilds')
root = tk.Tk()
root.title('csv data entry')

tk.Label(root, text='id').grid(row=0,column=0,padx=10,pady=5)
entry1= tk.Entry(root)
entry1.grid(row=0,column=1,padx=10,pady=5)

tk.Label(root,text='year').grid(row=1,column=0,padx=10,pady=5)
entry2= tk.Entry(root)
entry2.grid(row=1,column=1,padx=10,pady=5)

tk.Label(root,text='price').grid(row=2,column=0,padx=10,pady=5)
entry3=tk.Entry(root)
entry3.grid(row=2,column=1,padx=10,pady=5)

submit_button= tk.Button(root, text='Submit',command=submit_data)
submit_button.grid(row=3,column=0,columnspan=2, pady=10)

root.mainloop()

