## Building Restful API with Django & DRF

## The Authentication System

### Overview

This project is an authentication system for users. It is an introductory project that shows areas of django rest framework which includes concepts like endpoints and serializers. In this work django, django rest framework, postman for testing api and swagger for project documentation and API testing.


### Endpoints

1. register/:
User should be able to register using email address, username and password. In this project upon user registration a user is sent an OTP code in their email.
3. email-verify/: Using the OTP code sent to the user email upon registration, we pass the otp in order to verify the user(user.is_verified). Only user that their email has been verified can login.
4. Login/: Login is done using the email and password, only verified users can login and upon login a token is sent to the user.
5. Logout/: User should be able to log out of the authentication system. in this endpoint users can logout.
6. forgot_password/: users that forgot their password are able to use their email to verify when the password is lost, upon provision of email the user is sent an otp code to the email.
7. reset_password/: users using the token from the forgot password can then pass the token and then allowed to update their formal password.

### Features

- Registered user are able to login and logout.
- users that forgot their password can easily use the forgot password endpoint to just make  a new password.
- Swagger Api was used to document and test the various api endpoints.
- Views was tested.
- Email verification using email sent otp codes. in order to specified verified user.
- OTP generated with only 6 numeric characters, that are randomized before being sent to the user emial.


### Project Authentication Flow

![Authentication Workflow](./assets/auth.png)
