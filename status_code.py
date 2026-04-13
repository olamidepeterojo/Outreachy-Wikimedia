import os
import csv
import requests

def read_urls_from_csv(file_path):
    """
    Reads a CSV file and extracts URLs.

    Assumes the first column contains the URLs.
    Ignores empty rows and header.
    """
    urls = []

    with open(file_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)

        # Skip header row
        next(reader, None)

        for row in reader:
            if not row:
                continue

            url = row[0].strip()
            if url:
                urls.append(url)

    return urls


def fetch_status_code(url):
    """
    Sends a HEAD request to the given URL and returns the status code.

    Returns a tuple:
    - (status_code, reason) if the request is successful
    - ("Error", error_name) if the request fails
    """
    try:
        response = requests.head(url, timeout=5)
        return response.status_code, response.reason
    except requests.exceptions.RequestException as e:
        error_name = type(e).__name__
        return "Error", error_name


def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the path to the input CSV file
    file_path = os.path.join(script_dir, 'data', 'input.csv')
    urls = read_urls_from_csv(file_path)

    for url in urls:
        result = fetch_status_code(url)

        if isinstance(result, tuple):
            status_code, reason = result
            print(f"({status_code} {reason}) {url}")
        else:
            print(f"(error) {url}")



if __name__ == "__main__":
    main()