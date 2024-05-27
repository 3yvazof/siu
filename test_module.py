def test_search_functionality(selenium_helper, element_properties):
    search_box_properties = element_properties["search_box"]
    search_box = selenium_helper.find_element(search_box_properties["by"], search_box_properties["value"])
    search_box.send_keys("Youtube")

    search_button_properties = element_properties["search_button"]
    search_button = selenium_helper.find_element(search_button_properties["by"], search_button_properties["value"])
    search_button.click()

    assert "Youtube" in selenium_helper.driver.title