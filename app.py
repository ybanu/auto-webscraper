from flask import Flask, render_template, request, send_file
import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import BytesIO

app = Flask(__name__)

def extract_tables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tables = soup.find_all('table')
    extracted_tables = []

    for table in tables:
        data = []
        headers = [th.text.strip() for th in table.find_all('th')]

        for row in table.find_all('tr'):
            cols = [td.text.strip() for td in row.find_all('td')]
            if cols:
                data.append(cols)

        if data:
            df = pd.DataFrame(data, columns=headers if headers else None)
            extracted_tables.append(df)

    return extracted_tables

@app.route("/", methods=["GET", "POST"])
def index():
    tables = []
    url = ""

    if request.method == "POST":
        url = request.form["url"]
        tables = extract_tables(url)

    return render_template("index.html", tables=tables, url=url)

@app.route("/download/<format>/<int:index>", methods=["GET"])
def download(format, index):
    url = request.args.get("url")
    tables = extract_tables(url)

    if 0 <= index < len(tables):
        df = tables[index]
        
        if format == "csv":
            output = BytesIO()
            df.to_csv(output, index=False)
            output.seek(0)
            return send_file(output, download_name="table.csv", as_attachment=True, mimetype="text/csv")

        elif format == "excel":
            output = BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df.to_excel(writer, index=False)
            output.seek(0)
            return send_file(output, download_name="table.xlsx", as_attachment=True, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    return "Invalid table index", 400

if __name__ == "__main__":
    app.run(debug=False)

