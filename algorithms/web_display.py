from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

csv_file_path = 'csv/sorted_by_frequency.csv'

@app.route('/')
def display_csv():

    try:
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        return f"<h1>Error: The file '{csv_file_path}' was not found.</h1>", 404

    table_html = df.to_html(index=False, classes='table table-striped')

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CSV Viewer</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1>CSV File Viewer</h1>
            {table_html}
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True)
