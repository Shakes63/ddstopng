

# DDS to PNG Converter

This script, `ddstopng.py`, recursively searches for `.dds` files in a folder and its subfolders that start with the word `store` and converts them to `.png` format. It skips conversion if the `.png` version of a file already exists.

## Requirements

- Python 3.6 or later
- [Pillow](https://pillow.readthedocs.io/) library for image processing

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt


## Usage

### Running the Script

1. Open a terminal or command prompt.
2. Run the script with the following command:

   ```bash
   python ddstopng.py [folder_path]
   ```

   - Replace `[folder_path]` with the path to the folder containing `.dds` files. If no folder path is provided, the script defaults to:
     ```
     C:\Program Files (x86)\Steam\steamapps\common\Farming Simulator 25\data
     ```

### Examples

#### Default Folder
To use the default folder path, simply run:
```bash
python ddstopng.py
```

#### Custom Folder
To specify a custom folder path:
```bash
python ddstopng.py "C:\Users\YourUser\Documents\Textures"
```

### Output
- The script will:
  1. Search for `.dds` files starting with `store` in the specified folder and subfolders.
  2. Convert each `.dds` file to `.png` format and save it in the same directory.
  3. Skip conversion for `.dds` files if the `.png` version already exists.

### Logging
The script provides detailed logs in the terminal:
- `Found X DDS files.`: Indicates how many `.dds` files were located.
- `Converted: [file_path] -> [png_path]`: Displays successful conversions.
- `Skipping (png already exists): [png_path]`: Skips files if the `.png` already exists.

## Notes

- Ensure that the folder path provided has read/write permissions.
- The `.dds` files must be valid and supported by the `Pillow` library.
- If an unsupported `.dds` file is encountered, the script will skip it and log an error.

## Troubleshooting

### Missing Dependencies
If you encounter issues with missing dependencies, ensure you have installed them using:
```bash
pip install -r requirements.txt
```

### Unsupported `.dds` Files
If a `.dds` file fails to convert, ensure it is compatible with the `Pillow` library. Some `.dds` formats may require additional plugins.

## License

This project is open-source and available under the MIT License.
