import os

def list_subdirectories(parent_directory):
    """
    Lists and prints the names of all subdirectories within the specified parent directory.

    Args:
    parent_directory (str): The path to the parent directory.
    """
    # Check if the provided directory is actually a directory
    if not os.path.isdir(parent_directory):
        print("The specified path is not a directory.")
        return

    print("Subdirectories in " + parent_directory + ":")
    # Loop through the items in the directory
    for item in os.listdir(parent_directory):
        # Full path of the item
        item_path = os.path.join(parent_directory, item)
        # Check if the item is a directory
        if os.path.isdir(item_path):
            print(item)

# Example usage
# parent_dir = './data/python_2024_04_21_11_40_01'
# list_subdirectories(parent_dir)
