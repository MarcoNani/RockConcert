# Function: print to the default printer the passed string
# Parameters: string to print
# Returns: none

import win32print
import win32ui
import win32con
import win32gui

def print_to_whatever(text_to_print, printer_name="Microsoft Print to PDF"):
    """
    Prints text to the specified printer using proper DC context.
    
    Args:
        text_to_print (str): The text to be printed
        printer_name (str): Name of the printer to use, defaults to "Microsoft Print to PDF"
    
    Returns:
        None
    """
    document_name = "Print whatever"
    
    # Create a device context for the PDF printer
    hdc = win32gui.CreateDC("WINSPOOL", printer_name, None)
    dc = win32ui.CreateDCFromHandle(hdc)
    
    dc.StartDoc(document_name)
    dc.StartPage()
    
    # Set text properties
    dc.SetMapMode(win32con.MM_TWIPS)  # 1440 per inch
    dc.SetTextColor(0)  # Black text
    
    # Select a font
    font = win32ui.CreateFont({
        "name": "Consolas",
        "height": 220,  # Size in logical units
        "weight": 400,  # Normal weight
    })
    dc.SelectObject(font)
    
    # Calculate positions (72 points per inch, 20 twips per point)
    y_pos = -500  # Start position (top margin)
    left_margin = 500  # Left margin
    
    # Print each line of text
    for line in text_to_print.split('\n'):
        y_pos -= 200  # Line spacing
        dc.TextOut(left_margin, y_pos, line)
    
    dc.EndPage()
    dc.EndDoc()
    dc.DeleteDC()
    
    print(f"Print send to {printer_name}")


# Function to obtain list of printers
def get_printers():
    """
    Returns a list of available printers.
    
    Returns:
        list: A list of available printers
    """
    printers = [printer[2] for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)]
    return printers

# Test the function
if __name__ == "__main__":

    printers = get_printers()

    print("Available printers:")
    for printer in printers:
        print(printer)

    

    text_to_print = "Hello, world!\nThis is a test document.\nIt should work with PDF."
    print_to_whatever(text_to_print, printer_name=printers[3])