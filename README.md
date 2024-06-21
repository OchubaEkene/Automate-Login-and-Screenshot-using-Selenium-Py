# Automate Login and Screenshot using Python and Selenium

# Prerequisites needed
**1. Environmental variable file with login credentials**

**2. Chrome Webdriver**

**3. Install Selenium**

**4. Install dotenv and os**

**5. Good Internet connection, and you are good to go!**

# Setting up your environmental variable!
**Create a file with your username stored in a variable called NAME, password in a variable called PASSWORD, then make sure you save it as .env**

# How to run the script!
# To use the script, Install a Chrome Web driver with the same version as your chrome browser on your local machine and run it, open your IDE, run the code, relax and watch it work!

**This code automates login to a specific website using Selenium, and then screenshots the whole page, with the full height of the page if scrolled to the end.**

# 1. Install/Import necessary Libraries
**Install Libraries like Selenium which is the most important, it handles the automation.**

**Import load_dotenv, which load the env file with your saved login, and others**

# 2. List out User agents
**User agents are going to help avoid this script being blocked by the site from overloading.**

**Randomize the selection of User agents for it to work**

# 3. Locate the downloaded Chrome WebDriver on the local system
**Create a variable and store the path to the webdriver in order to load it.**

**Use the service library to load it**

# 4. Create an Options agent and set the user agent

# 5. Initialize the Chrome WebDriver

# 6. Navigate to the required URL
**Using the .get method from the Driver, navigate to the URL**

# 7. Maximize Window for better view & performance

# 8. Using the load_dotenv() method, load the .env file
**Load the env file that has the Username and Password stored on it.**

**Assign the Username and Password to two different Variables**

# 9. Use WebDriverWait to ensure the page is given enough time to load

# 10. Escape any Pop-up 
**Escape any Pop-up using the click() and WebDriverWait function**

# 11. Get the total height of the page
**Use .execute_script and .scrollHeight to get the total height of the page**

# 12. Take screenshot and save to path
**Scroll and take screenshots of each page, and save to path using .save_screenshot**

# 13. Stitch all screenshots together to form one
**Take the width, form one Screenshot and finally save to path, using the .makedirs method**

# 14. Quit the Web driver
**Quit the Web driver using the .quit() method**
