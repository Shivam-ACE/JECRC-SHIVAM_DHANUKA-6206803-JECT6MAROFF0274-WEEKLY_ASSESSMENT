### Task 1
#
#### Myntra Automation using Robot Framework
#
#1. Launch the browser (Chrome) and navigate to Myntra https://www.myntra.com/
#2. Maximize the browser window for better visibility.
#3. Hover the mouse over the Women section in the top navigation menu.
#4. Click on the Lehenga Choli category.
#5. Once the product listing page is loaded, scroll down to the filter section.
#6. Locate and select the Blue or your fav color filter option.
#7. Store the name/text of a specific product (e.g., Madhuram Floral Embroidered Choli with Skirt).
#8. Print the captured product name in the console.
#9. Close the browser.

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://www.myntra.com/

*** Test Cases ***
Myntra Automation using Robot Framework
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Mouse Over    xpath=//a[@data-group="women"]
    Sleep    1s
    
    Click Element    xpath=//a[text()="Lehenga Cholis"]
    Sleep    2s

    Scroll Element Into View    xpath=//span[@style="background-color: rgb(0, 116, 217);"]
    Sleep    2s

    Click Element    xpath=//span[@style="background-color: rgb(0, 116, 217);"]/parent::label/div
    Sleep    2s

    ${prod_name}=  Get Text    xpath=//li[@id="36763558"]//h3
    
    Log To Console    ${prod_name}
    
    Close Browser