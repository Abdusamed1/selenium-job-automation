# Indeed Job Scraper
**Purpose
This project is a Python-based web scraper that extracts job postings from Indeed. It retrieves job listings based on title, location, date posted, and experience level, and organizes the data neatly into an Excel file using openpyxl. The Excel file includes columns for job title, location, URL, date posted, applied status, and offer/rejected status. You can easily open the Excel file, click on the URLs to apply for jobs, and keep track of the jobs you’ve applied to.

<img width="1440" alt="scrapper-results" src="https://github.com/user-attachments/assets/60738527-f8db-4534-b672-42001387cb78">


## Prerequisites**
Before you begin, ensure you have the following installed on your computer:

Python (version 3.7 or higher)
pip (Python package installer)
Google Chrome (latest version)
ChromeDriver (see instructions below)

## Installation
## 1. Clone the Repository
Clone the project repository from GitHub to your local machine:
git clone https://github.com/Abdusamed1/selenium-job-automation.git
cd indeed-job-scraper

## 2. Create a Virtual Environment
It's a good practice to use a virtual environment to manage dependencies:
python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

## 3. Install Dependencies
Install the required Python packages using pip:
pip install -r requirements.txt

## 4. Install ChromeDriver
For macOS:
Download the ChromeDriver from the ChromeDriver download page.
https://developer.chrome.com/docs/chromedriver
Heres a youtube video you can follow if you're having trouble downloading chromedriver for MacOs
https://www.youtube.com/watch?v=m4-Z5KqDHpU&t=14s

Move the chromedriver binary to /usr/local/bin/:
sudo mv chromedriver /usr/local/bin/

Now for Windows:
Download the ChromeDriver from the ChromeDriver download page.
https://developer.chrome.com/docs/chromedriver/get-started
Heres a youtbe video you can follow if you're having trouble downloading chromedriver for Windows
https://www.youtube.com/watch?v=KqWUC-xWYpA

Extract the chromedriver.exe file and place it in a directory of your choice.
Add this directory to your system’s PATH environment variable:

Open the Start Search, type in "env", and select "Edit the system environment variables".
In the System Properties window, click on the "Environment Variables" button.
In the Environment Variables window, find the "Path" variable in the "System variables" section, and click "Edit".
Click "New" and add the path to the directory where you placed chromedriver.exe.
Click "OK" on all windows to apply the changes.

## 5. Run the Scraper
Execute the scraper script:
python job_scraper.py

The script will start scraping Indeed for job postings based on the parameters defined in config.py. The results will be saved in an Excel file located in the output directory.

# If you experience indeed authorization pages, then you can click on the challenege response test to verify you are a human, 

<img width="1431" alt="authentication-page" src="https://github.com/user-attachments/assets/b003a137-894c-474b-8430-79bb92e7eae9">

 script will wait 10 seconds for you to bypass that


## 6. Excel Output
The Excel will be saved as job_listings by default, you can change them name. The file will contain the following columns:

Job Title: The title of the job posting.
Location: The location of the job.
URL: The URL of the job posting.
Date Posted: The date when the job was posted.
Applied: Status of whether the job has been applied to.
Offer/Rejection: Status of whether the job has resulted in an offer or rejection.

## 7. (Optional) Test the Setup
To ensure everything is working correctly, you can run any included test cases:
pytest
Troubleshooting
Dependencies Issues: If you encounter issues with package installations, ensure your requirements.txt file is up-to-date and try reinstalling dependencies.

ChromeDriver Version Mismatch: Ensure the version of ChromeDriver matches your Chrome browser version.
Permissions Issues: Ensure chromedriver has execute permissions on macOS. You can modify permissions using:
chmod +x /usr/local/bin/chromedriver

## 8.Contribution
If you'd like to contribute to this project, please fork the repository and create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.



