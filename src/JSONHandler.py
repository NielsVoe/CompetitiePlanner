import json
import os

class JSONHandler:
    @staticmethod
    def Export(data: list[dict], directory: str, filename: str) -> None:
        """
        Export data to a JSON file.
        
        :param data: List of dictionaries containing the data to export.
        :param directory: The directory where the file will be saved.
        :param filename: The name of the file to save the JSON data to.
        """
        if not os.path.isdir(directory):
            os.makedirs(directory)
        with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data exported to {os.path.join(directory, filename)} successfully.")

    @staticmethod
    def Import(directory: str, filename: str) -> list[dict]:
        """
        Import data from a JSON file.
        
        :param directory: The directory where the file is located.
        :param filename: The name of the file to read the JSON data from.
        :return: List of dictionaries containing the imported data.
        """
        if not os.path.isfile(os.path.join(directory, filename)):
            raise FileNotFoundError(f"The file {filename} does not exist.")
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Data imported from {filename} successfully.")
        return data
    
    @staticmethod
    def IsEmpty(filename: str) -> bool:
        """
        Check if a JSON file is empty.
        
        :param filename: The name of the file to check.
        :return: True if the file is empty, False otherwise.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read().strip() == ''
        except FileNotFoundError:
            return True