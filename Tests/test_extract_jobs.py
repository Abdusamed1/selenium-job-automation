import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
pytest

from Code.job_scrapper import Indeed_Script

PATH = "/usr/local/bin/chromedriver-mac-arm64/chromedriver"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

@pytest.mark.empty
def test_job_cards_found():
    test_indeed = Indeed_Script()
    test_indeed.indeed_script()

    job_cards = test_indeed.driver.find_elements(By.XPATH, "//*[@id='mosaic-provider-jobcards']/ul/li")
    assert len(job_cards) > 0, "No job cards were found."

def test_job_details_extraction():
    test_indeed = Indeed_Script()
    test_indeed.indeed_script()
    job_list = test_indeed.job_info()

    assert all('title' in job and 'location' in job and 'url' in job for job in
               job_list), "Job details not correctly extracted."

def test_strengthen_profile_skipped():
    test_indeed = Indeed_Script()
    test_indeed.indeed_script()
    job_list = test_indeed.job_info()

    for job in job_list:
        assert "Strengthen your profile" not in job['title'], "'Strengthen your profile' should be skipped."

def test_no_job_cards_found():
    test_indeed = Indeed_Script()
    test_indeed.driver.get("https://www.indeed.com/q-NONEXISTENT-JOB.html")

    job_list = test_indeed.job_info()
    assert len(job_list) == 0, "Job cards were found when there should be none."

def test_list_of_jobs_returned():
    test_indeed = Indeed_Script()
    test_indeed.indeed_script()
    job_list = test_indeed.job_info()

    assert isinstance(job_list, list), "The returned job list is not a list."
    assert len(job_list) > 0, "The job list is empty."
