import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_have_different_names(go_to_my_pets):

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

   pets_name = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      pets_name.append(split_data_pet[0])

   r = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         r += 1
   assert r == 0
   print(r)
   print(pets_name)