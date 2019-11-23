*** Settings ***
Documentation    Suite description

Library    Collections


# One possible way to pass variables from py files
Variables  env.py
# Another way is to set "variablefile", see run_robot.py


*** Variables ***
${VDC_NAMES}=    ${vds_names}


*** Test Cases ***
Test Ex 1
    @{reversed_vdc_names} =    Set Variable    @{VDC_NAMES}
    Reverse List   ${reversed_vdc_names}
    :FOR   ${vdc_name}   IN   @{reversed_vdc_names}
    \   Select VDC   ${vdc_name}
    \   Prepare cluster.ini file for service console

Test Ex 2
    Fail

Test Ex 3
    [Tags]    noncritical
    Fail


*** Keywords ***
Select VDC
    [Arguments]    ${vdc_name}
    Log    Select VDC ${vdc_name}

Prepare cluster.ini file for service console
    Log    Prepare cluster.ini file for service console
