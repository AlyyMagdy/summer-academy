*** Settings ***
Library           restapitest.py

*** Test Cases ***
Run My Python Script
    Log    Hello
    get_single_user_email    5
    Log    Hello
