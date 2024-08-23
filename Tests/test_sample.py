import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Code.job_scrapper import Indeed_Script
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


PATH = "/usr/local/bin/chromedriver-mac-arm64/chromedriver"
service = Service(PATH)
driver = webdriver.Chrome(service=service)


def test___init__():
    test_indeed = Indeed_Script()
    assert test_indeed.driver is not None
    assert test_indeed.wait is not None
    assert test_indeed.service is not None

# @pytest.mark.job
def test_job_field_is_blank_before_writting_job_title():
    test_indeed = Indeed_Script()
    # Invoke the method to test
    test_indeed.indeed_script()
    try:
        # Wait for the job field to be visible
        clear_field = WebDriverWait(test_indeed.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='text-input-what']"))
        )
        # Ensure the field is empty
        assert clear_field.get_attribute("value") != "", "The job field is not empty"

    except NoSuchElementException as e:
        print(f"Error: {e}")
        assert False, "The job field could not be found"

# Add this check; make sure field is empty before typing
# @pytest.mark.job
def test_can_write_job_title_in_field():
    test_indeed = Indeed_Script()
    # Invoke the method to test
    test_indeed.indeed_script()
    try:
        job_field = WebDriverWait(test_indeed.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='text-input-what']"))
        )
        # Ensure the field is empty
        assert job_field.get_attribute("value") == "qa automation", "The job field is empty"

    except NoSuchElementException as e:
        print(f"Error: {e}")
        assert False, "The job field could not be found"

def test_location_field_is_blank_before_writing_location():
    test_indeed = Indeed_Script()
    test_indeed.indeed_script()

    try:
        location = WebDriverWait(test_indeed.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='text-input-where']"))
        )
        assert location.get_attribute("value") != "", "The job field is empty"

    except NoSuchElementException as e:
        print(f"Error: {e}")
        assert False, "The job field is empty"


def test_write_location_in_field():
    test_indeed = Indeed_Script()
    test_indeed.indeed_script()

    try:
        location = WebDriverWait(test_indeed.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='text-input-where']"))
        )
        assert location.get_attribute("value") == "united states", "The job field is not empty"

    except NoSuchElementException as e:
        print(f"Error: {e}")
        assert False, "The job field could not be found"

def test_search_with_job_title_and_location():
    test_indeed = Indeed_Script()
    test_indeed.indeed_script()

    try:
        search = WebDriverWait(test_indeed.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Search')]"))
        )
        search.click()
        # Wait for job cards to load
        WebDriverWait(test_indeed.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='mosaic-provider-jobcards']/ul/li/div"))
        )
        job_cards = test_indeed.driver.find_elements(By.XPATH, "//*[@id='mosaic-provider-jobcards']/ul/li/div")
        num_cards = len(job_cards)
        assert num_cards > 0, "No job results were returned after the search"
    except NoSuchElementException as e:
        print(f"Error: {e}")
        assert False, "Cannot click search"




