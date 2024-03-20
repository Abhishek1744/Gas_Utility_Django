# Gas Utility Django Application

This Django application is designed to manage service requests for a gas utility company. Users can submit service requests, track the status of their requests, and view their account information.

## Setup Instructions

### Linux and Unix

1. Clone the repository: `git clone https://github.com/your-username/gas-utility-django.git`
2. Navigate to the project directory: `cd gas-utility-django
3. Apply database migrations: `python3 manage.py makemigrations` followed by `python3 manage.py migrate`
4. Create a superuser for administrative access: `python3 manage.py createsuperuser`
5. Run the development server: `python3 manage.py runserver`

### Windows

1. Clone the repository: `git clone https://github.com/your-username/gas-utility-django.git`
2. Navigate to the project directory: `cd gas-utility-django`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py makemigrations` followed by `python manage.py migrate`
5. Create a superuser for administrative access: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`

## How to Run the Application

1. After setting up the application, open your web browser.
2. Navigate to `http://127.0.0.1:8000/` to access the application's home page.
3. To submit a service request, click on the "Submit Request" link and fill out the form.
4. To view the status of your request, click on the "View Request Status" link.
5. To access the administrative interface, go to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials created earlier.

## Additional Information

- The application uses Django's built-in authentication system. Users need to log in to access certain features.
- Service request status updates will be sent via email to the user.
- For any issues or questions, please refer to the project's documentation or contact the project maintainers.

---
**Note:** Replace `your-username` in the clone command with your actual GitHub username.
