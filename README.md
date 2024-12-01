# linkedin-profile-scraper-app
Write an API which will take a linkedin profile url as input and return the profile details as a json response. The scraper should not login to linkedin.

# Prerequisites
Python 3.8 or higher installed on your system.
Google Chrome browser installed.
ChromeDriver compatible with your Chrome browser version (automatically managed by webdriver-manager).

# Installation
1> Clone the Repository
2> Set Up a Virtual Environment
3> Install Dependencies

# Usage
1> Start the Flask Server

# API Endpoint
Endpoint: /scrape_linkedin
Method: GET
Query Parameter:
url (required): The LinkedIn profile URL to scrape.

# Example Request:
curl "http://localhost:5000/scrape_linkedin?url=https://www.linkedin.com/in/example-profile/"

# Sample Input:
https://www.linkedin.com/in/radhikagupta2/
https://www.linkedin.com/in/bhavishaggarwal/
https://www.linkedin.com/in/pankaj-chaddah/
https://www.linkedin.com/in/aman-gupta-7217a515/
https://www.linkedin.com/in/ritu-rathee-taneja-4194191a0/
https://www.linkedin.com/in/anupammittal007/
https://www.linkedin.com/in/riteshagar/
https://www.linkedin.com/in/kunalshah1/
https://www.linkedin.com/in/peyushbansal/
https://www.linkedin.com/in/apekshagupta/

# Sample Output:
<img width="921" alt="image" src="https://github.com/user-attachments/assets/073c96e0-1388-4c84-a3ba-6cb63018cc28">

