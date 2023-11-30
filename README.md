
# Python-File-Converter

The Python File Converter is a simple utility that converts CSV files from a list of directories into JSON objects. This project is designed to be used with Python 3.9 and utilizes a Python virtual environment to manage dependencies.
Table of Contents

Installation
Usage
How it Works
License
## Installation
To set up the Python virtual environment and install the required dependencies, follow these steps:

Clone the repository to your local machine:
````bash
Copy code
git clone https://github.com/yourusername/python-file-converter.git
cd python-file-converter
Create a virtual environment:
bash
Copy code
python3 -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS and Linux:
bash
Copy code
source venv/bin/activate
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Usage
After setting up the virtual environment and installing the dependencies, you can use the Python File Converter to process a list of directories containing CSV files and convert them into JSON objects.

Run the script with the following command:

bash
Copy code
python converter.py /path/to/directory1 /path/to/directory2 ...
Replace /path/to/directory1, /path/to/directory2, etc. with the actual paths to the directories containing the CSV files you want to convert.
````
## How it Works
The Python File Converter works as follows:

It takes a list of directories as input.
For each directory provided, it processes all the CSV files found within that directory.
For each CSV file, it reads the data and converts it into a pandas DataFrame.
The DataFrame is then converted into a JSON object.
The resulting JSON object is saved to a new file with the same name as the original CSV file, but with the ".json" extension.
Please make sure the CSV files have proper headers and consistent data structures to ensure accurate conversion

## License

[MIT](https://choosealicense.com/licenses/mit/)

