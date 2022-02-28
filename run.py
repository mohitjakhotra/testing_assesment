from test_cases.testcases import *
from time import sleep



with tcscenarios() as bot:
    bot.land_first_page()
    bot.invalid_login()
    bot.pwd_masked()
    bot.create_acc_name()
    bot.goto_signup()
    bot.confrmpwd()
    bot.test_pwd_allcombo()
    bot.account_creation()



