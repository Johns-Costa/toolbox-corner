# Deployment

- The database was deployed to [Neon](https://neon.tech/).

- The app can be reached by the [link](https://toolbox-corner-c9446b25bd36.herokuapp.com/)

# Payment Setup

1. Register a stripe account at https://dashboard.stripe.com/register.
2. Go to the developers' page:
3. Select API keys.
4. Copy the `public key` and `secret key` to the `env.py` file.
5. Add the following setting to `settings.py`:
```python
  STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY")
  STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
```
6. Install stripe package:
```python
  pip3 install stripe
```
7. Set up a checkout app to handle the payment.
8. Create an order model with the required fields in the checkout app.
9. Add a payment form to the checkout app template.
10. Create a View to handle payment setup:
  - Get public key: `stripe_public_key = settings.STRIPE_PUBLIC_KEY`
  - Get private key: `stripe_secret_key = settings.STRIPE_SECRET_KEY`
  - create intent: `intent = stripe.PaymentIntent.create(**kwargs)`
11. Create stripe_element.js to handle the payment .
12. In the checkout app views, you need to create a view to handle order creation.
13. The payment intent is created when the user clicks on the confirmation button. That stripe element prevents the user from multiple clicks and handles all errors. However, you must set alerts for the user to show the error.
14. To test the user's payment, you need to create a test payment intent with the card data provided by the stripe:

- No auth: 4242424242424242

- Auth: 4000002500003155
15. Create a success page to redirect the user after successful payment and add js functionality to handle the redirection.
16. Add URL to the stripe_webhook function in the checkout urls.py
```python
    path('webhook/', stripe_webhook),
```
17. Remember to set app stripe data in Heroku configs:

  - Create a webhook in the stripe dashboard and set the hosted endpoint.

  - `STRIPE_PUBLIC_KEY`
  - `STRIPE_SECRET_KEY`
  - `STRIPE_WEBHOOK_SECRET`

---

## Local deployment

---

1. Install the dependencies:

    - Open the terminal window and type:
    - `pip3 install -r requirements.txt`



1. Create a `.env` file. This will contain the following environment variables:

    ```python
    import os

      os.environ['SECRET_KEY'] = 'Add a secret key'
      os.environ['DATABASE_URL'] = 'will be used to connect to the database'
    ```


1. Run the following commands in a terminal to make migrations: 
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
1. Create a superuser to get access to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter the required information (your username, email and password).
1. Run the app with the following command in the terminal:
    - `python3 manage.py runserver`
1. Open the link provided in a browser to see the app.

1. If you need to access the admin page:
    - Add /admin/ to the link provided.
    - Enter your username and password (for the superuser that you have created before).
    - You will be redirected to the admin page.

## Heroku Deployment

* Set up a local workspace on your computer for Heroku:
    - Create a list of requirements that the project needs to run:
      - type this in the terminal: `pip3 freeze > requirements.txt`
    - Commit and push the changes to GitHub
    
* Go to [www.heroku.com](www.heroku.com) 
* Log in or create a Heroku account.
* Create a new app with any unique name <name app>.


* Create a Procfile in your local workplace:
    
    This file will will contain the following:
    ```python
        web: gunicorn <name app>.wsgi:application
    ```
    - Commit and push the changes to GitHub.

* Go to the settings app in Heroku and go to Config Vars.


Click on Reveal Config Vars and add the following config variables:

| Key      | Value          |
|-------------|-------------|
| DATABASE_URL | ... | 
| DISABLE_COLLECTSTATIC | 1 |
| SECRET_KEY | ... |
| EMAIL_HOST_PASS | ... |
| EMAIL_HOST_USER| ... |
| STRIPE_PUBLIC_KEY | ... |
| STRIPE_SECRET_KEY | ... |
| STRIPE_WH_SECRET | ... |


* Copy the value of DATABASE_URL and input it into the .env file and generate a secret key (you shoud use any secret key generator for secret key generation).
* Migrate changes.
* Set debug to False in settings.py
* Commit and push the changes to GitHub.
* Connect your repository to Heroku.
* Deploy the app to Heroku by clicking "Deploy Branch" button. If you want to enable auto-deployment, click "Enable Automatic Deployment".


The deployment process will start. 

Click "View build logs" to see the progress of the deployment.


**Final Deployment**

* Set debug to False locally + delete DISABLE_COLLECTSTATIC from config vars in Heroku dashboard.

* Commit and push the changes to GitHub.


### Create Database on Neon

1. Go to [Neon](https://neon.tech/) and create a new account.

2. Create a new instance of the database.

3. Select a name for your database and select the free plan.

4. Click "Select Region"

5. Select a region close to you.

7. Click "Create Instance"

8. Click on the name of your database to open the dashboard.

9. You will see the dashboard of your database. You will need the URL of your database to connect it to your Django project.