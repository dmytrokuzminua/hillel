"""Homework 7 task 6 Convert"""


import csv
import json
import xml.etree.ElementTree as ET


class CSVtoJSONConverter:
    """Class (csv to json) & (json to csv)"""
    @staticmethod
    def csv_to_json(csv_file, json_file):
        """Converts a csv file to json"""
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"CSV '{csv_file}' конвертовано в JSON '{json_file}'")

    @staticmethod
    def json_to_csv(json_file, csv_file):
        """Converts a json file to csv"""
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)
        if data:
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"JSON '{json_file}' конвертовано в CSV '{csv_file}'")


class XMLtoJSONConverter:
    """Class xml to json"""
    @staticmethod
    def xml_to_json(xml_file, json_file):
        """Converts a xml file to json"""
        tree = ET.parse(xml_file)
        root = tree.getroot()
        data = []
        for elem in root:
            item = {child.tag: child.text for child in elem}
            data.append(item)
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"XML '{xml_file}' конвертовано в JSON '{json_file}'")


if __name__ == "__main__":
    CSVtoJSONConverter.csv_to_json("students.csv", "students.json")
    CSVtoJSONConverter.json_to_csv("students.json", "students_from_json.csv")
    XMLtoJSONConverter.xml_to_json("products.xml", "products.json")
