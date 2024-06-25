# Testing

## Manual Testing

Testing was done throughout site development.

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users.


|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Sign Up (Register)     |                        |                  |      |             |
| 1           | Click on the "Sing in" link | Redirection to sign in page | Y |          |
| 2           | Enter valid email | Field will only accept email address format | Y |  |
| 3           | Enter valid email confirmation | Field will only accept the same email from the previous field | Y |  |       
| 4           | Enter valid username | Field will only accept no more than 50 characters |
| 5           | Enter valid password | Field will only accept secure passwords | Y |          |
| 6           | Enter valid password confirmation | Field will only accept the same password from the previous field | Y |          |
| 7           | Click on the "Sign Up" button | Redirects user to home page, if form is accepted. | Y |          |
| 8           | Click on the "Back to Login" button | Redirects user to Login | Y |          |
| Sign In     |                        |                  |      |             |
| 1           | Click on the "Sign Up" link in the form | Redirection to Sign Up page | Y |          |
| 2           | Enter valid username | Field will only accept valid, already registered, user name | Y |          |
| 3           | Enter valid password | Field will only accept a correct password for that user name | Y |          |
| 4           | Click on the "Sign In" | Takes user to home page, if form is accepted | Y |          |
| 5           | Click on the "Home"| Takes user to products page | Y |          |
| Sign Out    |                        |                  |      |             |
| 1           | Click on "Sign out" | Redirection to Products (home) page with user signed out | Y |          |
| 2           | Click on "Cancel" | Redirection to Products (home) page with user still signed in | Y |          |
| Navbar Menu |                        |                  |      |             |
| 1           | Click on the "hamburger" Menu | Dropdown menu with the options depending if user or staff member | Y | Available to everyone |
| 2           | Click on "Home" | Redirection to Products page | Y | Available to everyone |
| 3           | Click on "Contact us" | Redirection to Contact us page | Y | Available to everyone |
| 4           | Click on "My Account" | Drop down with different options depending if loggin in/logged out, Staff member or regular user | Y | Available only to Staff members |
| 5           | Click on My Account - "Register" | Redirection to Sign up page | Y | Available to everyone. Only visible when not signed in |
| 6           | Click on My Account - "Login" | Redirection to Sign in page | Y |  Available to everyone. Only visible when not signed in |
| 7           | Click on My Account - "Logout" button | Takes user to Sign Out page to confirm logout | Y | Available to everyone. Only visible when logged in|
| 8           | Click on My Account - "Add product" button | Takes user to Add product page | Y | Available only to Admin and staff members. Only visible when logged in|
| 9           | Click on Bag button | Takes user to Bag page | Y | Available to everyone. Only visible when logged in|
| 10           | Click on Categories button | Drop down with different Categories | Y | Available to everyone. |
| 11           | Click on Click on Categories - "categories option" button | Takes user to that specific Category products page | Y | Available to everyone. |
| 12           | Write on search bar | When magnifying lens or enter are pressed, Takes user to the search results page showing the available products that contain the written words. | Y | |
| Welcome        |                        |                  |      |             |
| 1           | Click on "Start Shopping" | Redirection to Products (home) page | Y |  |
| Home        |                        |                  |      |             |
| 1           | Click on any product (product card) | Redirection to product detail page of that specific product | Y |  |
| Prooduct Detail|                        |                  |      |             |
| 1           | Click on "Edit product" | Redirect to Edit product page | Y | Only available for Admin and Staff members |
| 2           | Click on "Delete product" | Redirect to Delete product page | Y | Only available for Admin and Staff members |
| 3           | Click on "Add/View reviews" | Redirect to the Review list page of that product | Y |          |
| 4           | Select Size| Select produc size | Y | Onyl available for products with sizes. Only shows when logged in |
| 5           | Click on Quantity "-" or "+" | increases os decreases the number of items of that product | Y | Only accepts from 1 to 99 Only shows when logged in|
| 6           | Click on "Keep Shopping" | Redirection to the Products (home) page | Y | Only shows when logged in |
| 7           | Click on "Add to bag" | Adds the selected number of item if that product to the bag | Y | A message of success is shown and the bag in the nav bar increases its value. Only shows when logged in. |
| 8           | Click on "Sign in to Shop" | Redirection to the Sign in page | Y | Only shows when logged out |
| Add Product |                        |                  |      | Only available for Staff Members and Admin |
| 1           | Enter Product Name | Field will only accept no more than 100 characters and is mandatory | Y |          |
| 2           | Enter Product Description | Field will only accept no more than 400 characters and is mandatory | Y |          |
| 3           | Enter Product Price | Field will only accept no more than 10 digits and is mandatory | Y |          |
| 4           | As sizes | Field acepts yes or no and is mandatory | Y |  |
| 5           | Enter Product Category | Mandatory to choose Category | Y |          |
| 6           | Click "Choose image" | Computer browser pops up to choose an image. Not mandatory | Y |          |
| 7           | Enter image alt | Fiel will only accept up to 50 characters and is mandatory when image is selected | Y |          |
| 8           | Check/Uncheck Delete | If delete is checked the image is deleted when the for is submited | Y |          |
| 9           | Click "Add another image" | A new for to add another image pops out | Y |          |
| 10          | Click "Save" | Product is saved and redirection to the product detail  | Y | A message with product added pops up |
| Edit Product|                        |                  |      | Only available for Staff Members and Admin |
| 1           | Enter Product Name | Field will only accept no more than 100 characters and is mandatory | Y |          |
| 2           | Enter Product Description | Field will only accept no more than 400 characters and is mandatory | Y |          |
| 3           | Enter Product Price | Field will only accept no more than 10 digits and is mandatory | Y |          |
| 4           | Select sizes | Field acepts yes or no and is mandatory | Y |  |
| 5           | Enter Product Category | Mandatory to choose Category | Y |          |
| 6           | Click "Choose image" | Computer browser pops up to choose an image. Not mandatory | Y |          |
| 7           | Enter image alt | Fiel will only accept up to 50 characters and is mandatory when image is selected | Y |          |
| 8           | Check/Uncheck Delete | If delete is checked the image is deleted when the for is submited | Y |          |
| 9           | Click "Save" | Product is saved and redirection to the product detail  | Y | A message with product updated pops up |
| Review list|                        |                  |      |             |
| 1           | Click on "Log in to add a review" | Redirection to Sign in page | Y |  Only shows if logged out |
| 2           | Click on "-->Add Review<--" | Redirection to add review page | Y | Only shows if logged in |
| 3           | Click on No reviews yet.Be the first to "Add review" | Redirection to add review page | Y | Only shows if logged in and no review was added yet |
| 4           | Click No reviews yet."Log in" to add a review  | Redirection to Sign in page | Y | Only shows if logged out and no review was added yet |
| 5           | Click on "Edit"  | Redirection to Edit review page of that product review | Y | Only shows in in the users reviews and when logged in |
| 6           | Click on "Delete"  | Redirection to Delete review page of that product review | Y | Only shows in in the users reviews and when logged in |
| Add Review  |                        |                  |      | Only available when logged in |
| 1           | Enter content | Field will accept a maximum of 500 characters | Y |          |
| 2           | Select Stars | Field will only 1 to 5 stars | Y |          |
| 3           | Click "Submit Review" | Redirect to the Product detail | Y |          |
| Edit Review |                        |                  |      | Only available when logged in |
| 1           | Enter content | Field will accept a maximum of 500 characters | Y |          |
| 2           | Select Stars | Field will only 1 to 5 stars | Y |          |
| 3           | Click "Update Review" | Redirect to the Product detail | Y |          |
|Delete Review|                        |                  |      | Only available when logged in |
| 1           | Click "Delete" | Redirect to the Product detail and review is deleted | Y |          |
| 2           | Click "Cancel" | Redirect to the Product detail | Y |          |
| Contact Us  |                        |                  |      |     |
| 1           | Select Subject | Select one of the available options. It is mandatory | Y |          |
| 2           | Enter content | Field will accept a minimum of 10 and a maximum of 500 characters | Y |   |         
| 3           | Enter email | Field only accepts an email format | Y |          |
| 4           | Click "Send" | Redirect to Contact Us page | Y | A confirmation message shows |
| Bag         |                        |                  |      | Only available when logged in |
| 1           | Click on Quantity "-" or "+" | Increases or decreases the number of items of that product | Y | Only accepts from 1 to 99 |
| 2           | Click "Update" | Updates the number of items if changed in the quantity | Y | |
| 3           | Click "Remove" | Removes product from the bag | Y | If 0 is selected, the product is removed |
| 4           | Click "Keep Shopping" | Redirects to Products (home) page | Y |  |
| 4           | Click "Secure Checkout" | Redirects to Checkout page | Y |  |
| Checkout    |                        |                  |      | Only available when logged in and only from the bag |
| 1           | Enter Full name | Field will accept a maximum of 50 characters. Mandatory | Y |  |
| 2           | Enter email | Field only accepts an email format. Mandatory | Y |          |
| 3           | Enter Full name | Field will accept a maximum of 20 characters. Mandatory | Y |  |
| 4           | Enter Street adress 1 | Field will accept a maximum of 80 characters. Mandatory | Y |  |
| 5           | Enter Street adress 1 | Field will accept a maximum of 80 characters. | Y |  |
| 6           | Enter Town or City | Field will accept a maximum of 40 characters. Mandatory | Y |  |
| 7           | Enter County, state or locality | Field will accept a maximum of 80 characters. | Y |  |
| 8           | Enter Postal code | Field will accept a maximum of 20 characters. | Y |  |
| 9           | Select Country | Select country from list. Mandatory | Y |  |
| 10          | Enter Card number | Enter a valid card number. Mandatory | Y |  |
| 11          | Click "Adjust Bag" | Redirects to the Bag page | Y |  |
| 12          | Click "Complete Order" | Redirects to checkout success page | Y | If payment not succesfull redirects back to checkout page with an error |
|Checkout Success|                        |                  |      | Only available when logged in and only from the checkout |
| 1           | Click "Ready for to buy more??" | Redirects back to Products (home) page | Y |  |

---

## Validation:
### HTML Validation:


- No errors or warnings were found when passing through the official [W3C](https://validator.w3.org/) validator. This checking was done manually by copying the view page source code (Ctrl+C) and pasting it into the validator.

- [HTML validation report](documentation/validation/html_validation.pdf)

### CSS Validation:

- [Full CSS Validation Report](documentation/validation/css_validation.pdf)

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator.

### JS Validation:

- [Full JS Validation Report](documentation/validation/js_validation.pdf)

- No errors or warning messages were found when passing through the official [JSHint](https://www.jshint.com/) validator.

### Python Validation:

- No errors were found when the code was passed through [CI pep8 validator](https://pep8ci.herokuapp.com/) besides from some lines that were too long. The lines mentioned bellow were not possible to break:
  - 2 lines in the settings.py, 
  - 1 line in the webhook_handler, 
  - 1 line in the checkout views,
  - 2 lines in the checkout models
  - 3 lines in the bag views.
- According to the reports, the code is [Pep 8-compliant](https://legacy.python.org/dev/peps/pep-0008/). This checking was done manually by copying python code and pasting it into the validator.

- [Pep8 Validation Report](documentation/validation/pep8_validation.pdf)

---
## Lighthouse Report

LightHouse is a web performance testing tool that can be used to evaluate the performance of a website. The report is generated by Google Chrome.

[Lighthouse Report](documentation/testing/lighthouse.pdf)

---

## Compatibility

Testing was conducted on the following browsers;

- Chrome;
- Safari;

---
## Responsiveness

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development.

---

## Bugs

### Known bugs

There are no current known bugs

### Solved bugs

There were plenty of bugs during the development process since this project was a learning platform for me. This allowed me to improve my skills and knowledge significantly.

However, I tried to solve the majority of them. One bug that took me a while to figure out was that I wasn't being able to pass some js code. It turned out to be the fact that I had accidentaly deleted the js bock from the base.html
Another bug was that the app was throwing an error if a user tried to add a second review to the same product. Only one review per product per user is allowed. The views add to be fixed and an if statement was added with error messages to prevent a user from trying to add a second review.


---