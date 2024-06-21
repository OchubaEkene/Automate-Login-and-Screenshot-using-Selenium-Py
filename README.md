# Automate Login and Screenshot using Python and Selenium

**This code automates login to a specific website using Selenium, and then screenshots the whole page, with the full height of the page if scrolled to the end.**

# 1. Install/Import necessary Libraries
**Install Libraries like Selenium which is the most important, it handles the automation.
Import load_dotenv, which load the env fiel with your saved login, and others**

# 2. List out User agents
**User agents are going to help avoid this script being blocked by the site from overloading**
**Randomize the selection of User agents for it to work**

# 3. Locate the downloaded Chrome WebDriver on the local system
**Create a variable and store the path to the webdriver in order to load it**
**Use the service library to load it**

# 4. Create an Options agent and set the user agent

# 5. Initialize the Chrome WebDriver

# 6. Navigate to the required URL
**Using the .get method from the Driver, navigate to the URL**

# 7. Maximize Window for better view & performance

# 8. Using the load_dotenv() method, load the .env file, which has the login credentials stored on it
**Assign the Username and Password to two different Variables**

