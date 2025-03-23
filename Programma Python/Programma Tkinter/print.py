# Function: print to the default printer the passed string
# Parameters: string to print
# Returns: none

import platform
import os
import tempfile

# Detect the operating system
SYSTEM = platform.system()

# Import platform-specific modules
if SYSTEM == "Windows":
    try:
        import win32print
        import win32ui
        import win32con
        import win32gui
    except ImportError:
        print("Warning: Windows printing modules not available. Install with 'pip install pywin32'")

def print_to_whatever(text_to_print, printer_name="Microsoft Print to PDF"):
    """
    Prints text to the specified printer using proper DC context.
    
    Args:
        text_to_print (str): The text to be printed
        printer_name (str): Name of the printer to use, defaults to "Microsoft Print to PDF"
    
    Returns:
        None
    """
    if SYSTEM == "Windows":
        return _print_windows(text_to_print, printer_name)
    elif SYSTEM == "Darwin":  # macOS
        return _print_macos(text_to_print, printer_name)
    else:
        print(f"Printing not supported on {SYSTEM}. Text content:\n{text_to_print}")
        return False

def _print_windows(text_to_print, printer_name):
    """Windows-specific printing implementation."""
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
    
    print(f"Print sent to {printer_name}")
    return True

def _print_macos(text_to_print, printer_name=None):
    """macOS-specific printing implementation."""
    try:
        # Create a temporary file with the content
        fd, path = tempfile.mkstemp(suffix='.txt')
        try:
            with os.fdopen(fd, 'w') as tmp:
                tmp.write(text_to_print)
            
            # Use lp command to print
            printer_option = f"-d {printer_name}" if printer_name else ""
            os.system(f"lp {printer_option} {path}")
            print(f"Print sent to {'default printer' if not printer_name else printer_name}")
            return True
        finally:
            # Clean up the temp file
            os.unlink(path)
    except Exception as e:
        print(f"macOS printing error: {e}")
        return False

# Function to obtain list of printers
def get_printers():
    """
    Returns a list of available printers based on the current operating system.
    
    Returns:
        list: A list of available printers
    """
    if SYSTEM == "Windows":
        try:
            return [printer[2] for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)]
        except Exception as e:
            print(f"Error getting Windows printers: {e}")
            return []
    elif SYSTEM == "Darwin":  # macOS
        try:
            import subprocess
            result = subprocess.run(['lpstat', '-p'], capture_output=True, text=True)
            printers = []
            for line in result.stdout.splitlines():
                if line.startswith("printer "):
                    printers.append(line.split()[1])
            return printers
        except Exception as e:
            print(f"Error getting macOS printers: {e}")
            return ["Default"]
    else:
        print(f"Getting printers not supported on {SYSTEM}")
        return []

# Test the function
if __name__ == "__main__":
    printers = get_printers()

    print(f"Available printers on {SYSTEM}:")
    for printer in printers:
        print(printer)

    if printers:
        text_to_print = "Hello, world!\nThis is a test document.\nIt should work on both Windows and macOS."
        print_to_whatever(text_to_print, printer_name=printers[0])
    else:
        print("No printers found.")