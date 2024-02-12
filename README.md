# Web Scraping Boilerplate Code

This repository contains boilerplate code to scrape data from any website using Python. It includes functions to fetch HTML, scrape data, and store it in both JSON and Excel formats.

## Libraries Used

- `requests`: For making HTTP requests.
- `urllib.parse`: For URL encoding.
- `bs4` (Beautiful Soup): For parsing HTML.
- `json`: For JSON manipulation.
- `pandas`: For data manipulation and Excel export.

## Usage

1. **Set up your environment**: Make sure you have Python installed, along with the required libraries mentioned above.

2. **Clone the repository**:

   ```bash
   git clone <repository_url>
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Modify the code**:
   
   - Change the `url` variable in `fetchAndSave` function to the website page you want to scrape.
   - Adjust the class names and fields in the `scrapeAndStore` function according to the HTML structure of the website you're scraping.

5. **Run the code**:

   ```bash
   python scrap.py
   ```

## Functions

- `fetchAndSave(url, path)`: Fetches HTML from the specified URL and saves it to the provided file path.

- `scrapeAndStore(path, jsonPath)`: Scrapes data from the HTML file, extracts relevant information, and stores it in a JSON file.

- `saveInExcel(jsonPath, excelPath)`: Reads data from a JSON file, converts it into a DataFrame, and saves it in an Excel file.

## Example

```python
# Change name or location as per your convenience

fetchAndSave(url, "data/scrap.html")
scrapeAndStore("data/scrap.html", "data/products.json")
```

## License

Feel free to contribute and improve the code!

Make sure to replace `<repository_url>` with the actual URL of your repository. This README provides an overview of your code, instructions on how to use it, and information about the functions included.