import pandas as pd
from collections import Counter
import re

def process_file(file_path, output_csv_path):
    # Read and process the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    text = re.sub(r'\[\d{2}/\d{2}/\d{2}, \d{2}:\d{2}:\d{2}\]', '', text)  # Remove [date, time]
    text = re.sub(r'\b\w+:‎?\b', '', text)  # Remove "Name:"
    text = re.sub(r'<attached:.*?>', '', text)  # Remove "<attached...>"

    words = re.findall(r'\b\w+\b', text)  # Extract words using regex

    word_counts = Counter(words)

    df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])

    df.sort_values(by='Word', inplace=True)

    df.reset_index(drop=True, inplace=True)

    df.to_csv(output_csv_path, index=False)

    return df
