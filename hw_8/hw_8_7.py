""" Homework 8 task 7 """


class FileProcessor:
    """Class for handling files"""

    @staticmethod
    def write_to_file(file_path: str, data: str) -> None:
        """Writes data to a file"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """Reads data from a file"""
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
