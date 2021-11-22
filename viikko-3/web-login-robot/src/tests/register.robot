*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  A new user account can be created if a proper unused username and a proper password are given

*** Test Cases ***
Register With Valid Username And Password
    Set Username  keijo
    Set Password  keijo123
    Set Password Confirmation  keijo123
    Submit Credentials
    Login Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ke
    Set Password  keijo123
    Set Password Confirmation  keijo123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  keijo
    Set Password  kei123
    Set Password Confirmation  kei123
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  keijo
    Set Password  keijo123
    Set Password Confirmation  keijo321
    Submit Credentials
    Register Should Fail With Message  Nonmatching password and password confirmation

Login After Successful Registration
    Set Username  keijotin
    Set Password  keijo123
    Set Password Confirmation  keijo123
    Submit Credentials
    Welcome Page Should Be Open
    Go To Login Page
    Set Username  keijotin
    Set Password  keijo123
    Submit Login Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  ke
    Set Password  keijo123
    Set Password Confirmation  keijo123
    Submit Credentials
    Go To Login Page
    Set Username  ke
    Set Password  keijo123
    Submit Login Credentials
    Login Page Should Be Open

*** Keywords ***
Login Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

A new user account can be created if a proper unused username and a proper password are given
    Go To Register Page