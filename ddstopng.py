import os
from typing import List
from PIL import Image
import argparse


def find_store_dds_files(folder_path: str) -> List[str]:
    """
    Recursively searches a folder and its subfolders for files that start with 'store' and end with '.dds'.

    Parameters:
        folder_path (str): The path to the folder to search.

    Returns:
        List[str]: A list of file paths that match the criteria.
    """
    matching_files = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().startswith('store') and file.lower().endswith('.dds'):
                matching_files.append(os.path.join(root, file))

    return matching_files


def convert_dds_to_png(file_paths: list) -> None:
    """
    Converts a list of .dds files to .png format and saves them in the same directory.
    Skips conversion if the .png file already exists.

    Parameters:
        file_paths (list): List of file paths to .dds files.
    """
    for file_path in file_paths:
        if file_path.lower().endswith('.dds'):
            try:
                # Construct the output .png path
                png_path = os.path.splitext(file_path)[0] + ".png"

                # Check if the .png file already exists
                if os.path.exists(png_path):
                    print(f"Skipping (png already exists): {png_path}")
                    continue

                # Open the .dds file
                with Image.open(file_path) as img:
                    # Save as .png
                    img.save(png_path, "PNG")
                    print(f"Converted: {file_path} -> {png_path}")
            except Exception as e:
                print(f"Error converting {file_path}: {e}")


# Example usage
if __name__ == "__main__":
    # Default folder path
    default_folder_path = r"C:\Program Files (x86)\Steam\steamapps\common\Farming Simulator 25\data"

    parser = argparse.ArgumentParser(description="Convert DDS files to PNG format.")
    parser.add_argument(
        "folder_path",
        type=str,
        nargs="?",
        default=default_folder_path,
        help="Path to the folder containing DDS files (default: Farming Simulator 25 data folder)."
    )
    args = parser.parse_args()
    folder = args.folder_path
    print(f"Searching for files in: {folder}")
    files = find_store_dds_files(folder)
    print(f"Found {len(files)} DDS files.")
    print("Converting DDS files to PNG...")
    convert_dds_to_png(files)
