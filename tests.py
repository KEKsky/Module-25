from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_email, valid_password, user_name


def test_show_my_pets(browser):
    browser.find_element(By.ID, 'email').send_keys(valid_email)

    browser.find_element(By.ID, 'pass').send_keys(valid_password)

    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    submit_button.click()

    assert browser.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link')))
    submit_button.click()

    assert browser.find_element(By.TAG_NAME, 'h2').text == user_name

    pet_info = browser.find_element(By.CSS_SELECTOR, 'div.left:nth-child(1)').text.split('\n')[1]
    number_of_pets = int("".join(filter(str.isdigit, pet_info)))

    assert len(browser.find_elements(By.CSS_SELECTOR, 'tbody tr')) == number_of_pets

    images = browser.find_elements(By.CSS_SELECTOR, 'tr th[scope=row] img')
    names = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(2)')
    descriptions = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(3)')
    age = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(4)')
    print(names)

    num_photos_pets = 0
    count_names = len(names)
    name_list = []
    age_list = []
    descriptions_list = []

    for i in range(count_names):
        assert names[i].text != ''
        name_list.append(names[i].text)
        if images[i].get_attribute('src'):
            num_photos_pets += 1
        assert descriptions[i].text != ''
        descriptions_list.append(descriptions[i].text)
        assert age[i].text != ''
        age_list.append(age[i].text)
        assert 0 <= int(age[i].text) < 100
        assert 0 < len(names[i].text) < 255
        assert 0 < len(descriptions[i].text) < 255

    assert len(name_list) == len(set(name_list))
    assert len(age_list) == len(set(age_list))
    assert len(descriptions_list) == len(set(descriptions_list))

    assert count_names / 2 <= float(num_photos_pets)
