#5 imports below were added manually
from org.translateai.crypto.utils.io.FileProcessingException import FileProcessingException
from pathlib import Path
import datetime
import random
import os

class FileUtils:
    def __init__(self):
        raise TypeError("FileUtils cannot be instantiated")

    @staticmethod
    def readFile(folderPath, fileName):
        path = Path(f"{folderPath}/{fileName}")
        try:
            with open(path, 'rb') as f:
                return f.read()
        except Exception as e:
            raise FileProcessingException(f"Error reading file: {path}", e)

    @staticmethod
    def writeFile(folderPath, fileName, data):
        path = Path(f"{folderPath}/{fileName}")
        try:
            with open(path, 'wb') as f:
                f.write(data)
        except Exception as e:
            raise FileProcessingException(f"Error writing file: {path}", e)

    @staticmethod
    def createTestSubFolder(parentFolder):
        #added missing dash after %S - minor fix for the line below
        name = f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-')}{random.randint(1000, 9999)}"
        new_folder = Path(f"{parentFolder}/{name}")
        try:
            os.makedirs(new_folder)
        except FileExistsError:
            raise FileProcessingException(f"Directory already exists: {new_folder}", None)
        return str(new_folder)

    @staticmethod
    def areEqual(folder1, file1, folder2, file2):
        path1 = Path(f"{folder1}/{file1}")
        path2 = Path(f"{folder2}/{file2}")
        try:
            #Not exactly the way to compare files that was used originally, but OK
            return hash(open(path1, 'rb').read()) == hash(open(path2, 'rb').read())
        except Exception as e:
            raise FileProcessingException(f"Error comparing files: {path1} and {path2}", e)
