# Project Documentation

### Overview
This is the documentation for the Test Automation assignment given by VOLVO. It provides an overview of the project, its components, and how to use them.

### Project Structure

The project is structured as follows:

- Root Directory
    - PageObjects
        - FlipkartPages.py
    - TestCases
        - test_TC1_Search_And_Order_Mobile.py
        - test_TC2_Order_BestRated_MensTShirt.py
        - test_TC3_Compare_Two_Products.py
    - Utilities
        - BaseClass.py
        - Logger.py
    - TestEvidences
        - TC1_Search_And_Order_Mobile.log
        - TC2_Order_BestRated_MensTShirt.log
        - TC3_Compare_Two_Products.log
        - AutomationReport.html
    - conftest.py
    - requirements.txt

### Modules

The project consists of the following modules:

- `BaseClass`: A base class for test cases.
- `Logger`: A module for logging.
- `FlipkartPages`: A module containing page objects for the Flipkart website.
- `conftest`: Test configuration file.
- `config.properties`: File is used to store configuration settings for the project.
- `AutomationReport.html`: Test file for generating the automation report.

### Test Cases

The project includes the following test cases:

- `test_TC1_Search_And_Order_Mobile.py`: A test case for searching and ordering a mobile on the Flipkart website.
- `test_TC2_Order_BestRated_MensTShirt.py`: A test case for ordering the best rated men's t-shirt.
- `test_TC3_Compare_Two_Products.py`: A test case for comparing two products.

### Classes

The project includes the following classes:

- `Test_Search_And_Order_Mobile`: A test case class for searching and ordering a mobile.
- `Test_Order_BestRated_MensTShirt`: A test case class for ordering the best rated men's t-shirt.
- `Test_Compare_Two_Products`: A test case class for comparing two products.

### Usage

To use the project, follow these steps:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the test cases using the command `pytest`.
4. You can use the command `python -m pytest --html=TestEvidences/AutomationReport.html` to  generate HTML Report

[View Demo](https://github.com/Praveen-Raj-B/VOLVO)

## Contact

Praveen Raj Balasubramanian - [praveenrajkct@gmail.com ](mailto:praveenrajkct@gmail.com)

Project Link: [https://github.com/your_username/repo_name](https://github.com/Praveen-Raj-B/VOLVO)


## License

[MIT](https://choosealicense.com/licenses/mit/)