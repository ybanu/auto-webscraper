# Automated Web Scraper

## Overview
This project is an automated web scraper built using Python and Flask. The scraper fetches data from any given website, converts it into a CSV file, and then into an Excel sheet for dataset use. It features a simple web interface where users can input a URL, extract data, and display the extracted table directly on the interface.

## Features
- Extracts data from any website with a structured table format.
- Converts the extracted data into CSV and Excel formats.
- Displays the extracted table on the web interface.
- User-friendly web interface for inputting URLs and managing data.
- Built using Python, Flask, BeautifulSoup (bs4), Pandas, and OpenPyXL.

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Web framework for building the interface.
- **BeautifulSoup (bs4)**: For web scraping.
- **Pandas**: For data manipulation and conversion to CSV.
- **OpenPyXL**: For handling Excel file conversion.
- **HTML, CSS, Bootstrap**: For building the web interface.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/auto-web-scraper.git
   cd auto-web-scraper
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```
3. Enter a URL containing tabular data and click "Scrape Data."
4. View the extracted data on the interface.
5. Download the data as a CSV or Excel file.

## Project Structure
```
auto-web-scraper/
│── static/
│── templates/
│── app.py
│── requirements.txt
│── README.md
```

## Future Enhancements
- Support for scraping non-tabular data.
- Option to filter and clean extracted data.
- Support for more output formats (JSON, Database storage).
- Implement authentication for secure scraping.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

---

**Author:** Bhanu Teja  
**LinkedIn:** [Bhanu Teja Yaragala](https://www.linkedin.com/in/bhanu-teja-yaragala-701225255)  
**Email:** bhanuyadavyaragala@gmail.com

