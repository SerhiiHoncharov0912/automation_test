## 🛠️ Setup Instructions
To run the program, follow these steps:

1. Clone the repository to your local machine.
2. Open the project in any IDE that supports Python — for example, PyCharm or Visual Studio Code.
3. In the terminal, from the root directory of the project, run the command `pip install -r requirements.txt` to install all required dependencies.
4. Once all packages are installed, start the program by running the command `python main.py`.

## 🔍 Functionality Overview
This program automatically tests both positive and negative login scenarios for the website `https://www.saucedemo.com/`.
After a successful login, it:
  1. Extracts product information from the Inventory page;
  2. Saves product names and prices to `products.csv`;
  3. Logs all UI interactions in `automation.log`;
  4. In case of errors, saves screenshots to the `automation_screenshots/` directory.

## ❓ Answers
### * What steps did you prioritize first? Why?
  I prioritized the positive login case first, as it is a critical part of the functionality. If the system fails to log in successfully, continuing with the rest of the tests would be meaningless.
  
### * What was critical to complete in the 1 hour?
  During the first hour, it was critical to implement the successful login, the logic for collecting product information, and logging that data into the `products.csv file`, since one of the main goals of the program is to gather information about the products.
  
### * How long did you actually spend on the project?
  I spent approximately an hour and a half on the project. I used ChatGPT to generate a base version of the code, which could have been slightly refactored to finish the task in about 20 minutes. However, that code wouldn’t have demonstrated the level of skill and understanding I wanted to show in my test assignment. That’s why I chose to invest more time in writing clean, readable, maintainable, and reusable code.

### * How did you know your automation was working?
  I verified that the automation was working by observing the expected outcomes at each step. The script successfully handled both positive and negative login scenarios, navigated to the inventory page, collected product names and prices, and wrote them into the `products.csv` file. Additionally, all interactions were logged into `automation.log`, and for negative test cases, expected errors were logged and corresponding screenshots were saved. This confirmed that both successful and failing flows were handled correctly.

### * What would you improve with more time?
  Given the scope of this test task, I don't currently see any major improvements needed in the implemented logic. With more time, I would consider covering additional login edge cases and extending the automation to include testing of the Checkout functionality.
