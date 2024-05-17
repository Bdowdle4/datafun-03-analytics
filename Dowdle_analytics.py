#1. Environment Setup
    #py -m venv .venv
    #.\.venv\Scripts\Activate.ps1
    #py -m pip install requests
    #py -m pip freeze > requirements.txt

#2. Project Start - In your Python file, create a docstring with a brief introduction to your project.
'''Project 3 emphasizes skills in using Git for version control, creating and managing Python 
virtual environments, and handling different types of data. The project involves fetching data 
from the web, processing it using appropriate Python collections, and writing the processed data 
to files.'''

#3. Import Dependencies (At the Top, After the Introduction) - Be sure you have INSTALLED any external 
# packages (those not in the Python Standard Library) into your active project virtual environment first.

# Standard library imports
import csv
import pathlib 
import json

# External library imports (requires virtual environment)
import requests

#4. Data Acquisition - Use the requests library to fetch data from specified web APIs or online data sources.
#5. Write Data - Write functions to save content to different file types (e.g., text, CSV, JSON).

## Fetches text data from the specified URL and writes it to a new file
def fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url):
    try:
        # Fetch data from URL
        response = requests.get(txt_url)
        response.raise_for_status()  # Error message for bad status codes

        # Full file path using pathlib
        text_folder_path = pathlib.Path(txt_folder_name)
        text_file_path = text_folder_path / txt_filename

        # Ensure the parent directory exists
        text_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the fetched text data to the file
        text_file_path.write_text(response.text, encoding='utf-8')
        print(f"Text data successfully saved to {text_file_path}")

    except Exception as e:
        print(f"Error fetching and writing text data: {e}")

## Fetches CSV data from the specified URL and writes it to a new file
def fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url):
    try:
        # Fetches data from URL
        response = requests.get(csv_url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Construct the full file path using pathlib
        csv_folder_path = pathlib.Path(csv_folder_name)
        csv_file_path = csv_folder_path / csv_filename

        # Ensure the parent directory exists
        csv_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the fetched text data to the file
        csv_file_path.write_text(response.text, encoding='utf-8')
        print(f"CSV data successfully saved to {csv_file_path}")

    except Exception as e:
        print(f"Error fetching and writing csv data: {e}")

## Fetches Excel data from the specified URL and writes it to a new file
def fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url):
    try:
        # Fetches data from URL
        response = requests.get(excel_url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Construct the full file path using pathlib
        excel_folder_path = pathlib.Path(excel_folder_name)
        excel_file_path = excel_folder_path / excel_filename

        # Ensure the parent directory exists
        excel_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the fetched text data to the file
        excel_file_path.write_bytes(response.content)
        print(f"Excel data successfully saved to {excel_file_path}")

    except Exception as e:
        print(f"Error fetching and writing excel data: {e}")

## Fetches JSON data from the specified URL and writes it to a new file
def fetch_and_write_json_data(json_folder_name, json_filename, json_url):
    try:
        # Fetches data from URL
        response = requests.get(json_url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Validate that the response contains JSON data
        try:
            data = response.json()
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return

        # Construct the full file path using pathlib
        json_folder_path = pathlib.Path(json_folder_name)
        json_file_path = json_folder_path / json_filename

        # Ensure the parent directory exists
        json_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the fetched JSON data to the file
        json_file_path.write_text(json.dumps(data, indent=4), encoding='utf-8')
        print(f"JSON data successfully saved to {json_file_path}")

    except Exception as e:
        print(f"Error fetching and writing JSON data: {e}")

#6. Process Data and Generate Output - Write functions to read, process, and write results using 
# appropriate Python collections (lists, sets, dictionaries, etc.). Demonstrate understanding of each 
# collection data type's characteristics and usage.

## Function 1. Process Text Data: Process text with lists and sets to demonstrate proficiency in working 
## with text files.
def process_text_data(txt_folder_name, txt_filename, output_filename):
    try:
        # Read the text data from the file
        text_folder_path = pathlib.Path(txt_folder_name)
        text_file_path = text_folder_path / txt_filename
        text_data = text_file_path.read_text(encoding='utf-8')

        # Split text into words and calculate word count
        words = text_data.split()
        word_count = len(words)
      
        # Format the results
        result = f"Word Count: {word_count}\n{text_data}"

        # Write the results to the output file
        output_file_path = text_folder_path / output_filename
        output_file_path.write_text(result, encoding='utf-8')
        print(f"Text data processed and results saved to {output_file_path}")

    except Exception as e:
        print(f"Error processing text data: {e}")

## Function 1. Process Text Data: Process text with lists and sets to demonstrate proficiency in working 
## with text files.
def process_csv_data(csv_folder_name, csv_filename, output_filename):
    try:
        # Read the CSV data from the file
        csv_folder_path = pathlib.Path(csv_folder_name)
        csv_file_path = csv_folder_path / csv_filename
        csv_data = csv_file_path.read_text(encoding='utf-8').splitlines()

        # Parse the CSV data
        reader = csv.reader(csv_data)
        header = next(reader)
        rows = list(reader)

        # Example: Calculate average of a numeric column (assuming the last column is numeric)
        numeric_column = [float(row[-1]) for row in rows]
        average_value = sum(numeric_column) / len(numeric_column)

        # Format the results
        result = f"Average of last column: {average_value:.2f}\n"

        # Write the results to the output file
        output_file_path = csv_folder_path / output_filename
        output_file_path.write_text(result, encoding='utf-8')
        print(f"CSV data processed and results saved to {output_file_path}")

    except Exception as e:
        print(f"Error processing CSV data: {e}")
