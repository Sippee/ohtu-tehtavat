*** Settings ***
Resource  resource.robot
Test Setup  A new user account can be created if a proper unused username and a proper password are given

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  abc  abcde123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  abcde123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  abcde123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  abc  abc123
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  abc  abcdefghijkl
    Output Should Contain  Password contains only letters

*** Keywords ***
A new user account can be created if a proper unused username and a proper password are given
    Create User  kalle  kalle123
    Input New Command