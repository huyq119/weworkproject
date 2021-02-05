import pytest
import yaml

from test_cases.test_bash import TestBase


class TestMain(TestBase):

    @pytest.mark.parametrize("name, phone, gender", yaml.safe_load(open("../test_cases/test_add_contacts.yml")))
    def test_add_contact(self, name, phone, gender):
        """
        添加联系人，返回查看联系人列表
        :param name:
        :param phone:
        :return:
        """
        result = self.app.start().main().goto_contacts().goto_add_contact_option() \
            .goto_add_contact().add_contact(name, phone, gender).get_toast()
        # 判断添加的姓名已保存在列表里
        assert result == "添加成功"

    @pytest.mark.parametrize("name1, phone1, gender1", yaml.safe_load(open("../test_cases/test_add_contacts.yml")))
    def test_contact_fail(self, name1, phone1, gender1):
        """
        添加联系人失败，证明已存在
        :param name:
        :param phone:
        :return:
        """
        result = self.app.start().main().goto_contacts(). \
            goto_add_contact_option().goto_add_contact().add_contact_fail(name1, phone1, gender1).get_message_text()

        assert "手机已存在于通讯录，无法添加" == result
