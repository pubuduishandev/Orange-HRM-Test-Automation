**Project: OrangeHRM Test Automation** <br>
_Automate the login , leave and log out processes for the OrangeHRM site_
Course Module: IC 4305 - Software Quality Management and Test Automation <br>
Prepared by: W.A.P. Pubudu Ishan <br>
Index No:- 2020t00876 <br>
Email:- 2020t00876@stu.cmb.ac.lk <br>
Assignment Submission Date : 24th April 2025 <br>
Toolset: Selenium, Python, PyTest, Page Object Model (POM) <br>

**Introduction** <br>
This test plan outlines the strategy and scope of the automated functional testing effort for the OrangeHRM demo web application using Selenium WebDriver and Python. The goal is to validate the successful execution of login, leave application, and logout workflows using a maintainable and scalable Page Object Model (POM) based automation framework. <br>

**Test Items**
OrangeHRM Demo Web Application
URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

**Features to be Tested** <br>
01. Home page title validation <br>
02. Login functionality with valid credentials <br>
03. Leave page navigation via "My Leave" Quick Launch icon <br>
04. Logout functionality <br>

**Features Not to Be Tested** <br>
  - Backend/API layers <br>
  - UI responsiveness (mobile/tablet views) <br>
  - Cross-browser compatibility (only Chrome will be used) <br>
  - Security, performance, and stress testing <br>

**Approach** <br>
A modular and layered Page Object Model (POM) architecture will be used for test development: <br>
  - Page Objects Layer: Contains reusable element locators and methods. <br>
  - Test Layer: Contains PyTest test cases that invoke Page Object methods. <br>
  - Tests will be written in Python using the Selenium WebDriver. <br>
  - Execution will be via the command line using PyTest. <br>
  - Reports will be generated using pytest-html or HTMLTestRunner. <br>

**Environmental Needs** <br>
  - Operating System: Windows <br>
  - PyCharm IDE (latest) (Professional Edition) <br>
  - Browser: Google Chrome (latest) <br>
  - Python: Version 3.13.3 <br>
  - Required Libraries: <br>
      - selenium <br>
      - pytest <br>
      - webdriver-manager <br>
      - pytest-html (optional) <br>
      - Openpyxl <br>
      - Allure <br>
      - pytest-order <br>
      - reportlab <br>
  - Internet connectivity for accessing OrangeHRM demo site <br>

