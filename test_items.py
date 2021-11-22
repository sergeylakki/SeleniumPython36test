import time


class TestAnswer():

    def test_find_button_basket(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(30)
        btn_add_basket = browser.find_elements_by_css_selector(".btn-add-to-basket")
        assert len(btn_add_basket) == 1, "Нет кнопки для добавления товара"

