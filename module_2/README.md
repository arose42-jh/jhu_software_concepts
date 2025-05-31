# Module 2: Data Scraping and Cleaning Due June 1st 2025
Andrew Rose | arose42

## Compliance with robots.txt
per robots.txt, all are allowed everywhere except /cgi-bin/ and /index-ad-test.php. This program does not interact with either of these
I am not any of the other listed entities what are disallowed from parsing.

## Contents
- `run.py`: Main script to run the full scraping and cleaning pipeline
- `scrape.py`: Functions for scraping, using urllib and beautiful soup, and saving data
- `clean.py`: Functions for loading and cleaning, uses a mix of beautifulsoup and regex
- `requirements.txt`: Python dependencies for this module

## Setup Instructions

1. **Navigate to the module directory:**
   ```powershell
   cd module_2
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

## Running the Pipeline

Run the main script to scrape, save, load, and clean the data:

```powershell
python run.py
```

- The script will scrape up to 500 pages (with a 0.5s delay between requests to avoid overloading the server).
- Scraped data is saved to `scraped_data.json`.
- The data is then loaded and cleaned.
- The process may take 4+ minutes to complete.

## Notes
- You can adjust the number of pages to scrape by editing the loop in `run.py`.
- Ensure you have a stable internet connection during scraping.
- Output and intermediate files will be created in the same directory.

## Stopping the Script
- Press `Ctrl+C` in the terminal to stop execution at any time.

## Known issues
- With the comments, I have seen some issues with special characters, its not all of them, but sometimes they show up very strange in the applicants_data.json