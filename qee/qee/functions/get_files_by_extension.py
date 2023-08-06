import os
import glob


def get_files_by_extension(folder_path: str, extension: str = None) -> list[str]:
    """
    The function is intended to read files from a folder by extension

    - folder_path: folder path in the files to be read
    - extension: file extension to be read
    """

    # Verify if folder path exists
    if not os.path.exists(folder_path):
        print(f"Caminho inválido: {folder_path}")
        return

    # Read files all if extension is None
    if extension is None:
        extension = "*"

    # Build pattern using file extension
    pattern_fetch = os.path.join(folder_path, f"*.{extension}")

    # Create a list of files with the pattern that matches the extension
    files = glob.glob(pattern_fetch)

    return files
