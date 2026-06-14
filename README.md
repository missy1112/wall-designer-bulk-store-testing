# wall-designer-bulk-store-testing
Bulk QA automation testing project for Wall Designer online store using Selenium and Pytest.
# Wall Designer Bulk Store Testing

This is a QA automation project for the Wall Designer online store.
The project uses Selenium and Pytest to test important store pages, product listing content, product page navigation, and basic cart flow.

## Project Objective

The goal of this project is to practice real-world website testing on an e-commerce store by checking that key pages load correctly and that important shopping features work as expected.

## Website Tested

https://walldesigner.co.za/

## Tools Used

* Python
* Selenium
* Pytest
* WebDriver Manager
* Git
* GitHub
* Visual Studio Code

## Test Scenarios Covered

| Test Case                    | Description                                                                | Status |
| ---------------------------- | -------------------------------------------------------------------------- | ------ |
| Bulk Page Load Test          | Checks that important store pages load successfully from `urls.txt`        | Passed |
| Homepage Test                | Verifies the homepage loads without page errors                            | Passed |
| Collection Page Test         | Verifies the all-products collection page loads successfully               | Passed |
| Contact Page Test            | Verifies the contact page loads successfully                               | Passed |
| Cart Page Test               | Verifies the cart page loads successfully                                  | Passed |
| Product Listing Test         | Checks that the collection page displays product-related content           | Passed |
| Product Page Navigation Test | Opens a product page from the collection page                              | Passed |
| Cart Flow Test               | Selects a product option/size and checks that cart-related content appears | Passed |

## Project Structure

```text
wall-designer-bulk-store-testing/
├── screenshots/
├── tests/
│   └── test_bulk_pages.py
├── .gitignore
├── README.md
├── requirements.txt
└── urls.txt
```

## How to Install

Clone the repository:

```bash
git clone https://github.com/missy1112/wall-designer-bulk-store-testing.git
```

Go into the project folder:

```bash
cd wall-designer-bulk-store-testing
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## How to Run the Tests

Run all tests using:

```bash
pytest
```

## Test Result

Current result:

```text
7 passed
```

## Screenshots

Test result screenshots are saved in the `screenshots` folder.

## What I Learned

Through this project, I practiced:

* Testing a real e-commerce website
* Reading multiple URLs from a text file
* Running bulk page load checks
* Using Selenium to open and inspect live web pages
* Using Pytest to run automated tests
* Finding product links from a collection page
* Testing product page navigation
* Testing a basic cart flow
* Handling real website behaviour and adjusting tests when needed
* Using Git and GitHub to save and document the project

## Notes

This project does not complete real payments or place real orders.
The checkout/payment process is not tested because this is a live e-commerce store.
