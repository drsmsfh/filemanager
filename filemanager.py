import os
import shutil
from send2trash import send2trash
import stat

def list_directory_contents(directory):
    try:
        # List all files and directories in the given directory
        items = os.listdir(directory)
        x = f"Contents of '{directory}':"
        dir_cont = []
        #max_length = max(len(element) for element in lim)
        for item in items:
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                size = os.path.getsize(item_path)
                fol_con =f"{item}-[{size}b]"
                dir_cont.append(fol_con)
            elif os.path.isdir(item_path):
                fol_con =f"{item}-<DIR>"
                dir_cont.append(fol_con)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except NotADirectoryError:
        print(f"The path '{directory}' is not a directory.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    itm_num = len(dir_cont)
    deg_num = str(itm_num)
    R_deg_num = len(deg_num)
    max_length = []
    val_x = len(x)+4
    max_dir_length_0 = max(len(item) for item in dir_cont)
    max_dir_length = max_dir_length_0 +5 +R_deg_num
    max_length.append(max_dir_length)
    max_length.append(val_x)
    sig_val = max(max_length)
    print('-'*sig_val)
    print("| " +x+' '*(sig_val - val_x) + " |")
    num = 1
    print('-'*sig_val)
    for item in dir_cont:
        print(f"| {num:0{R_deg_num}}."+item+" "* (sig_val - (len(item)+5 +R_deg_num))+" |")
        print('-'*sig_val)
        num += 1
    items = os.listdir(directory)
    return items

def delete_paths(paths):
    for path in paths:
        try:
            if os.path.isfile(path):
                os.remove(path)
                print(f"Successfully deleted file: {os.path.basename(path)}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Successfully deleted directory and its contents: {path}")
            else:
                print(f"Path not found: {path}")
        except PermissionError as e:
            print(f"PermissionError: {e} - {path}")
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e} - {path}")
        except OSError as e:
            print(f"OSError: {e} - {path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e} - {path}")

def dir_z(x, dr):
    items = os.listdir(x)
    zar = os.path.join(x, items[dr - 1])
    return zar

def open_file_or_folder(path):
    try:
        # Open the file or folder with the default program
        os.startfile(path)
    except FileNotFoundError:
        print("Error: File or folder not found.")
    except OSError:
        print("Error: No program associated with the file or folder.")
    except Exception as e:
        print("An unexpected error occurred:", e)

def fil_bro(x, dr):
    try:
        items = os.listdir(x)
        if dr < 1 or dr > len(items):
            raise IndexError
        dir_z_path = os.path.join(x, items[dr - 1])
        if os.path.isdir(dir_z_path):
            list_directory_contents(dir_z_path)
            return dir_z_path
        else:
            open_file_or_folder(dir_z_path)
            return x
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print(f"Invalid number. Please enter a number between 1 and {len(items)}.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return x

def get_parent_directory(path):
    # Get the parent directory of the given path
    parent_dir = os.path.dirname(path)
    return parent_dir

def move_file(source, destination):
    try:
        # Move the file from the source directory to the destination directory
        shutil.move(source, destination)
        print("File moved successfully.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except PermissionError:
        print("Error: Permission denied to access the source or destination directory.")
    except shutil.Error as e:
        print("Error:", e)

def move_to_recycle_bin(path):
    try:
        send2trash(path)
        print(f"'{os.path.basename(path)}' has been moved to the Recycle Bin.")
    except FileNotFoundError:
        print(f"Error: The file or folder '{os.path.basename(path)}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to move '{os.path.basename(path)}' to the Recycle Bin.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def copy_path(src_path, dest_path):
    try:
        # Check if the source path exists
        if not os.path.exists(src_path):
            print(f"Source path '{src_path}' does not exist.")
            return
        
        # Check if the source path is a file or a directory
        if os.path.isfile(src_path):
            # If it's a file, copy it directly
            shutil.copy2(src_path, dest_path)
            print(f"'{os.path.basename(src_path)}' copied to '{os.path.basename(dest_path)}'.")
        elif os.path.isdir(src_path):
            # If it's a directory, copy the entire directory
            shutil.copytree(src_path, dest_path)
            print(f"'{os.path.basename(src_path)}' copied to '{os.path.basename(dest_path)}'.")
        else:
            print(f"Source path '{src_path}' is neither a file nor a directory.")
    except Exception as e:
        print(f"An error occurred while copying: {e}")

def file_manager():
    corent_dir = r"C:\\"
    sel_fil = []
    list_directory_contents(corent_dir)
    while True:
        command = input("Enter 'brws' to browse folders, 'cpy' to copy, 'bck' to go back, 'sel' to select, 'mve' to move, or 'ext' to exit, or 'mtt' to move to trash, or 'dlt' to delete: ").strip().lower()
        if command == 'brws' or command == '':
            try:
                dr = int(input("Enter the number of the file: "))
                new_dir = fil_bro(corent_dir, dr)
                if new_dir:
                    corent_dir = new_dir
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif command == 'bck':
            bck = get_parent_directory(corent_dir)
            list_directory_contents(bck)
            corent_dir = bck
        elif command == 'sel':
            try:
                dr = int(input("Enter the number of the file: "))
                items = os.listdir(corent_dir)
                if dr < 1 or dr > len(items):
                    raise IndexError
                selected_path = os.path.join(corent_dir, items[dr - 1])
                sel_fil.append(selected_path)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except IndexError:
                print(f"Invalid number. Please enter a number between 1 and {len(items)}.")
        elif command == 'mve':
            for i in sel_fil:
                move_file(i, corent_dir)
            print("Files moved successfully.")
            sel_fil = []
            list_directory_contents(corent_dir)
        elif command == 'mtt':
            for i in sel_fil:
                move_to_recycle_bin(i)
            sel_fil = []
            list_directory_contents(corent_dir)
        elif command == 'cpy':
            for i in sel_fil:
                copy_path(i, corent_dir)
            sel_fil = []
            list_directory_contents(corent_dir)
            print("Files copyed successfully.")
        elif command == 'dlt':
            delete_paths(sel_fil)
            sel_fil = []
            list_directory_contents(corent_dir)
        elif command == 'ext':
            print("Exiting.")
            break
        else:
            print("Invalid command. Please enter 'brws', 'bck', 'sel', 'mve', or 'ext'.")

file_manager()
