# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(firstname = "Andrey", middlename = "Vladimirovich", lastname = "Tracevskij",
                                       nickname = "Zverun", title = "QA", company = "Adani",
                                       address = "Novodvorskij s/s 116", phone_home = "80172234522",
                                       phone_mobile = "8044777777", phone_work = "2222222", email = "test@ya.ru"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(firstname = "", middlename = "", lastname = "", nickname = "", title = "",
                                       company = "", address = "", phone_home = "", phone_mobile = "", phone_work = "",
                                       email = ""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)