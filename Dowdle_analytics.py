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
#packages (those not in the Python Standard Library) into your active project virtual environment first.

# Standard library imports
import csv
import pathlib 
import json

# External library imports (requires virtual environment)
import requests
import pandas as pd
import xlrd

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

    except Exception as ee:
        print(f"Error fetching and writing csv data: {ee}")

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

    except Exception as eee:
        print(f"Error fetching and writing excel data: {eee}")

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

    except Exception as eeee:
        print(f"Error fetching and writing JSON data: {eeee}")

#6. Process Data and Generate Output - Write functions to read, process, and write results using 
#appropriate Python collections (lists, sets, dictionaries, etc.). Demonstrate understanding of each 
#collection data type's characteristics and usage.
#7. Implement Exception Handling - Use try/except/finally and implement exception handling to catch known 
#possible errors and handle them gracefully in at least one of your functions.

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

    except Exception as ep:
        print(f"Error processing text data: {ep}")

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

    except Exception as eep:
        print(f"Error processing CSV data: {eep}")

## Function 3. Process Excel Data: Extract and analyze data from Excel files to produce meaningful 
## statistics, summaries, or insights, and save the insights as text files.
def process_excel_data(excel_folder_name, excel_filename, output_filename):
    try:
        # Read the Excel data from the file
        excel_folder_path = pathlib.Path(excel_folder_name)
        excel_file_path = excel_folder_path / excel_filename
        excel_data = pd.read_excel(excel_file_path)

        # Example: Summarize data (assuming it has a numeric column named 'Value')
        summary = excel_data.describe()

        # Format the results
        result = summary.to_string()

        # Write the results to the output file
        output_file_path = excel_folder_path / output_filename
        output_file_path.write_text(result, encoding='utf-8')
        print(f"Excel data processed and results saved to {output_file_path}")

    except Exception as eeep:
        print(f"Error processing Excel data: {eeep}")

## Function 4. Process JSON Data: Process JSON data with dictionaries to demonstrate proficiency in 
## working with labeled data.
def process_json_data(json_folder_name, json_filename, output_filename):
    try:
        # Read the JSON data from the file
        json_folder_path = pathlib.Path(json_folder_name)
        json_file_path = json_folder_path / json_filename

        # Ensure the file is not empty and contains valid JSON
        try:
            json_data = json_file_path.read_text(encoding='utf-8')
            if not json_data.strip():
                raise ValueError("JSON data is empty")
            data = json.loads(json_data)
        except json.JSONDecodeError as eeeep:
            print(f"Error decoding JSON: {eeeep}")
            return
        except ValueError as eeeev:
            print(eeeev)
            return

        # Check if "people" key exists in the JSON data
        if "people" not in data:
            raise KeyError("'people' key not found in JSON data")

        # Extracting specific information
        number_of_astronauts = data.get('number', 0)
        astronaut_names = [person['name'] for person in data['people']]

        # Format the results
        result = f"Number of astronauts: {number_of_astronauts}\nAstronauts:\n"
        result += "\n".join(astronaut_names)

        # Write the results to the output file
        output_file_path = json_folder_path / output_filename
        output_file_path.write_text(result, encoding='utf-8')
        print(f"JSON data processed and results saved to {output_file_path}")

    except KeyError as eeeek:
        print(eeeek)
    except Exception as eeeex:
        print(f"Error processing JSON data: {eeeex}")

#8. Main Function - Implement a main() function to test the folder creation functions and demonstrate 
#the use of imported modules.
def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print my name
    name = "Brittany Dowdle"
    print(f"Name: {name}")

    # URL's where data was pulled
    txt_url = 'https://www.thecompleteworksofshakespeare.com/tragedy/romeo-and-juliet'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    json_url = 'http://api.open-notify.org/astros.json'
    
    # Folder names
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 
    
    # File names
    txt_filename = 'romeoJuliet.txt'
    csv_filename = 'countryLadderScore.csv'
    excel_filename = 'cattle.xls' 
    json_filename = 'astronauts.json' 
    
    # Functios to take web data and convert it to a specified file format
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)
    
    # Functons for text processing in different file formats
    process_text_data('data-txt', 'romeoJuliet.txt', 'romeoJuliet_analysis.txt')
    process_csv_data('data-csv', 'countryLadderScore.csv', 'countryLadderScore_analysis.txt')
    process_excel_data('data-excel', 'cattle.xls', 'cattle_analysis.txt')
    process_json_data('data-json', 'astronauts.json', 'astronauts_analysis.txt')

#9. Conditional Script Execution (At the end of the file) - Ensure the main function only executes when 
#the script is run directly, not when imported as a module by using standard boilerplate code.
if __name__ == '__main__':
    main()        