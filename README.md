# Papa Scraper (Google Web scraper)

### **Overview**

This Python project is a graphical user interface (GUI) application that allows users to scrape email addresses from web pages on google and convert the results into an Excel file. It uses requests, selenium, and beautifulsoup4 for web scraping, PyQt5 for the GUI, and MySQL for database management.

### **Features**

1. __Local Login System:__ Users can register and login on the local computer 
2. __Web Scraping:__ The application performs web scraping on all google pages and extracts emails from websites
3. __Display Results:__ The results, including email addresses and their associated links, are displayed in a table within the GUI.
4. __Convert To Excel:__ Users have the option to convert the displayed email addresses and links into an Excel file for further analysis.
5. __Database Integration:__ The project integrates with a MySQL database to store and check results, preventing duplicates.
6. __Multithreading:__ Web scraping is performed in a separate thread to prevent the GUI from freezing during the search.

### **Installation**
1. __Python Environment:__ Make sure you have Python 3.x installed on your system.
2. __Required Libraries:__ Install the required Python libraries using the following command:
```
Pip install PyQt5 requests selenium beautifulsoup4 mysql-connector-python openpyxl pandas 
```
3. __Database Setup:__ You need a MySQL database. Update the database configuration in the 'sqlstuff.py' file to match your database settings. Ensure that the necessary tables are created as described in the code comments.
4. __Web Driver:__ Download the appropriate WebDriver for your browser (e.g., Chrome) and update the path to the WebDriver in the 'next_page' function of 'sel.py'.

### **Usage**
1. __Run the Application:__ Execute the main.py script to launch the GUI application.
2. __Register/Login:__ Register your username and password and login
3. __Enter URL:__ Enter a URL in the input field provided
4. __Find Emails:__ Click the __Find__ button to initiate the email search process. The results will be displayed in the table.
5. __Convert to Excel:__ Click the __Convert to Excel File__ button to save the displayed email addresses and links in an Excel file. You can specify the file name in the input field.



