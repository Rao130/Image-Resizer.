@@ -0,0 +1,33 @@
import pandas as pd
from tkinter import Tk, filedialog, messagebox
def csv_to_excel():
    # Open file dialog to select the CSV file
    csv_file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
    if not csv_file_path:
        messagebox.showwarning("Warning", "No file selected.")
        return
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Set the output file path as the same name but with an .xlsx extension
        excel_file_path = csv_file_path.replace(".csv", ".xlsx")
        
        # Write to an Excel file
        df.to_excel(excel_file_path, index=False)
        
        messagebox.showinfo("Success", f"File converted and saved as {excel_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert file: {e}")
# Create the Tkinter window
root = Tk()
root.withdraw()  # Hide the main window as we only need file dialogs
# Call the CSV to Excel conversion function
csv_to_excel()
# Close the Tkinter window after running
root.destroy()
