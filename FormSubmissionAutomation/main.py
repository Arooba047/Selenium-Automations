import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# -----------------------------
# 1. Load CSV
# -----------------------------
csv_path = os.path.abspath("data.csv")
data = pd.read_csv(csv_path)

# -----------------------------
# 2. Launch Selenium
# -----------------------------
driver = webdriver.Chrome()

# -----------------------------
# 3. Open local HTML file
# -----------------------------
form_path = os.path.abspath("test_form.html")
driver.get("file://" + form_path)

# -----------------------------
# 4. Resume file path
# -----------------------------
resume_path = os.path.abspath("Arooba_Resume_Automation.pdf")

# -----------------------------
# 5. Fill the form for each CSV row
# -----------------------------
for index, row in data.iterrows():

    # Name
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys(str(row["Name"]))

    # Email
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(str(row["Email"]))

    # Phone
    driver.find_element(By.ID, "phone").clear()
    driver.find_element(By.ID, "phone").send_keys(str(row["Phone"]))

    # Dropdown (Position)
    position_dropdown = Select(driver.find_element(By.ID, "position"))
    position_dropdown.select_by_value(str(row["Position"]))  
    # CSV should contain: dev / qa / pm

    # Experience Radio buttons
    exp_value = str(row["Experience"]).lower()   # junior / mid / senior
    driver.find_element(By.ID, f"exp_{exp_value}").click()

    # Checkbox (Relocation)
    relocate_value = str(row["Relocate"]).lower()  # yes/no

    checkbox = driver.find_element(By.ID, "relocate")

    if relocate_value == "yes":
        if not checkbox.is_selected():
            checkbox.click()
    else:
        if checkbox.is_selected():
            checkbox.click()

    # Upload Resume
    driver.find_element(By.ID, "resume").send_keys(resume_path)

    # Cover Letter
    driver.find_element(By.ID, "cover").clear()
    driver.find_element(By.ID, "cover").send_keys(str(row["CoverLetter"]))

    # Submit
    driver.find_element(By.ID, "submitBtn").click()

    # Pause so user can see submitted data
    time.sleep(5)

# End pause
time.sleep(5)
driver.quit()
