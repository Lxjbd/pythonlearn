from test_selenium.test_po.pages.main_page import MainPage


class TestAddPartment:
    def setup_class(self):
        self.main = MainPage()

    def test_add_partment(self):
        result = self.main.goto_addpartment().add_department().get_list()
        assert "谢境" in result

    def test_add_partment_fail(self):
        result = self.main.goto_addpartment().add_department_fail().get_toast()
        assert "该部门已存在" == result