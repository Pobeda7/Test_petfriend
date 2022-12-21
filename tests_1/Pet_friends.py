import pytest
from settings import valid_email, valid_password

def test_show_pet_friends():
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element_by_id('email').send_keys(valid_email)
   pytest.driver.find_element_by_id('pass').send_keys(valid_password)
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/'

   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   assert names[0].text != ''

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0