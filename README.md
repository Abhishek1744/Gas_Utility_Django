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
# Gas Utility Application Development Case Study

## Introduction
The Gas Utility Application project aimed to develop a web application that allows users to submit service requests, check the status of their requests, and view their account information. The application was built using the Django framework and Python programming language.

## Development Process
The project followed an agile development methodology with iterative sprints. The development environment included Django for backend development, HTML/CSS for frontend, and SQLite for the database. The project was divided into several phases, including requirements gathering, design, implementation, testing, and deployment.

## Key Features Implemented
1. **Service Request Submission:** Users can submit service requests, including the type of request and a description.
2. **Request Status Checking:** Users can check the status of their service requests.
3. **Account Information:** Users can view their account information, including billing address, contact number, and consumption history.
4. **Authentication:** Implemented user authentication using Django's built-in authentication system.
5. **Responsive Design:** The application is responsive and works well on desktop and mobile devices.

## Challenges Faced
1. **Authentication and Authorization:** Implementing secure authentication and authorization for users accessing different parts of the application.
2. **UI/UX Design:** Designing a user-friendly interface that meets the needs of both technical and non-technical users.
3. **Testing:** Ensuring the application works correctly across different browsers and devices.

## Technologies Used
- Django framework for backend development
- Python programming language
- HTML/CSS for frontend
- SQLite for the database
- Git for version control
- Postman for API testing

## Results
The Gas Utility Application was successfully developed and deployed, providing users with a convenient way to submit service requests, check their status, and view their account information. The application has been well-received by users and has helped streamline the process of managing service requests for the gas utility company.

## Conclusion
The Gas Utility Application project demonstrated the effective use of Django and Python for developing a web application with complex functionality. The project showcased the importance of user-centric design and the challenges of implementing secure authentication and authorization mechanisms.

## Future Scope
Future enhancements to the application could include integrating with payment gateways for online bill payments, implementing notifications for service request updates, and expanding the application to support additional utility services.

## Acknowledgments
We would like to thank our team members for their hard work and dedication throughout the project. Their contributions were instrumental in the successful development and deployment of the Gas Utility Application.

## References
- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
