# Adfocus-Money-Maker

## Requirements

### System Requirements
- **Recommended:** A Windows 10/11 computer with more than 8GB of RAM

### Software Requirements
- **Python Version:** 3.12.1

### PIP Dependencies
Ensure you have the latest versions of the following Python packages installed:
- selenium
- requests
- keyboard
- ChromeDriverManager
- webdriver_manager

## How to Run

1. Open Command Prompt (CMD) and navigate to the directory containing `main.py`. Execute the script by running `python main.py`.
2. Visit the Adfocus website to retrieve your API Key. Detailed instructions on obtaining the API Key are provided below.
3. When prompted, paste your Adfocus API Key into the script.
4. The script will inquire if you wish to use threading. If yes, specify the number of threads you want to use (10 threads are recommended for optimal performance).
5. You will then be asked if you want to optimize the process for maximizing earnings. If you choose yes, the script will wait for 60 seconds after generating an Adfocus URL before proceeding.
6. Specify the number of repetitions per thread. The total number of clicks generated will be calculated based on the formula: `Threads * Repeat_amount`.
7. The script will generate a valid URL for the Adfocus link and create it.
8. Finally, it will initiate the threads responsible for managing the Adfocus clicks and operate ChromeDriver instances in the background.

### Obtaining Your Adfocus API Key
- **Login** to your Adfocus account.
- At the top of the page, click on **"Tools"**.
- Then, select **"API"** from the menu.
- Copy your API Key as specified in the provided API URL.
