*** Settings ***
Library           restapitest.py

*** Test Cases ***
Run My Python Script
    Log    Hello
    ${email}=    get_single_user_email    5
    Should Not Be Empty    ${email}
