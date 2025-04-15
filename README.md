---------------------------------------------------------------------------------------------------------- <br>
**Project: OrangeHRM Test Automation** <br>
_Automate the login , leave and log out processes for the OrangeHRM site_
Course Module: IC 4305 - Software Quality Management and Test Automation <br>
Prepared by: W.A.P. Pubudu Ishan <br>
Index No:- 2020t00876 <br>
Email:- 2020t00876@stu.cmb.ac.lk <br>
Assignment Submission Date : 24th April 2025 <br>
Toolset: Selenium, Python, PyTest, Page Object Model (POM) <br>
---------------------------------------------------------------------------------------------------------- <br>
**Introduction** <br>
This test plan outlines the strategy and scope of the automated functional testing effort for the OrangeHRM demo web application using Selenium WebDriver and Python. The goal is to validate the successful execution of login, leave application, and logout workflows using a maintainable and scalable Page Object Model (POM) based automation framework. <br>
---------------------------------------------------------------------------------------------------------- <br>
**Test Items**
OrangeHRM Demo Web Application
URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
---------------------------------------------------------------------------------------------------------- <br>
**Features to be Tested** <br>
01. Home page title validation <br>
02. Login functionality with valid credentials <br>
03. Leave page navigation via "My Leave" Quick Launch icon <br>
04. Logout functionality <br>
---------------------------------------------------------------------------------------------------------- <br>
**Features Not to Be Tested** <br>
01. Backend/API layers <br>
02. UI responsiveness (mobile/tablet views) <br>
03. Cross-browser compatibility (only Chrome will be used) <br>
04. Security, performance, and stress testing <br>
---------------------------------------------------------------------------------------------------------- <br>
**Approach** <br>
A modular and layered Page Object Model (POM) architecture will be used for test development: <br>
  01. Page Objects Layer: Contains reusable element locators and methods. <br>
  02. Test Layer: Contains PyTest test cases that invoke Page Object methods. <br>
  03. Tests will be written in Python using the Selenium WebDriver. <br>
  04. Execution will be via the command line using PyTest. <br>
  05. Reports will be generated using pytest-html or HTMLTestRunner. <br>
---------------------------------------------------------------------------------------------------------- <br>
**Environmental Needs** <br>
01. Operating System: Windows <br>
02. PyCharm IDE (latest) (Professional Edition) <br>
03. Browser: Google Chrome (latest) <br>
04. Python: Version 3.13.3 <br>
05. Required Libraries: <br>
      - selenium <br>
      - pytest <br>
      - webdriver-manager <br>
      - pytest-html (optional) <br>
      - Openpyxl <br>
      - Allure <br>
      - pytest-order <br>
      - reportlab <br>
06. Internet connectivity for accessing OrangeHRM demo site <br>
---------------------------------------------------------------------------------------------------------- <br>
