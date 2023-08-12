*** Settings ***
Library           restapitest.py

*** Test Cases ***
Get Single User Data
    Log    Hello
    ${email}=    get_single_user_email    5
    Should Not Be Empty    ${email}

Add Single User
    ${Data}=    Add User    Anyone    Engineer

    Log To Console    ${Data}


Register User
# Complete adding the Keyword.
