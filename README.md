# COVID_19_TRACKER
A simple Python application to track COVID-19 cases globally and country-wise using data from Worldometers. This application features a graphical user interface (GUI) built with the Tkinter library. It fetches live COVID-19 data using web scraping with the requests and BeautifulSoup libraries.

**Features**
Global COVID-19 Data: Displays the total number of cases, deaths, and recoveries worldwide.
Country-Specific Data: Allows users to input a country's name and view its COVID-19 statistics.
Live Data Reload: Fetches the latest data with a simple button click.
User-Friendly Interface: Easy-to-use GUI built with Tkinter.
**Prerequisites**
To run this application, ensure you have the following installed:
Python 3.x
Required Python libraries:
requests
bs4 (BeautifulSoup)
tkinter (comes pre-installed with Python)
**Installation**
1. Clone the repository:
   git clone https://github.com/your-username/covid-tracker.git
   cd covid-tracker
2. **Install dependencies:**
   pip install requests beautifulsoup4
3. **Add the banner image:**
   Place a COVID-19-related banner image in the project folder and name it covid 19.png.
4. **Run the application:**
   python covid_tracker.py

**Usage**
Global Data:
The application automatically displays global COVID-19 data when launched.
Country-Specific Data:
Enter the name of a country in the input field (e.g., india, usa, germany) and click Get Data.
The application will display COVID-19 statistics for the specified country.
Reload Data:
Click Reload to refresh the global COVID-19 data.

**Code Overview**
**Main Functions**
get_html_data(url): Fetches HTML content of a webpage using the requests library.
get_covid_data(): Scrapes global COVID-19 data from Worldometers.
get_country_data(): Scrapes COVID-19 data for a specific country entered by the user.
reload(): Updates the GUI with the latest global data.
**GUI Components**
Banner: Displays a COVID-19-themed banner image at the top.
Input Field: A text field to input the country name.
Buttons:
Get Data: Fetches and displays country-specific COVID-19 data.
Reload: Updates the global data.
Main Label: Displays COVID-19 statistics.

      

