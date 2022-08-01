# Project-My-Debtors-Team-38
Creating a WebApp that functions for debt recovery and tracking. 


## Feature Requests

### User: Unauthenticated.

- Visit the platform to view basic information about it
- View and Interact with the documentation
- Register to view more details
- No access to data

### User: Authenticated
- Full access to the platform
- Verify details before full access to platform
- Post new data about a debtor
- Allow debtors to challenge - contend
- Comment on post by others
- Copy should be disabled


## Authors

- [Joseph Philip](https://www.github.com/jpphilips)
- [Add your name](https://www.github.com/your-username)


## Run Locally

Clone the project

```
git clone https://github.com/zuri-training/Project-My-Debtors-Team-38.git
```

Go to the project directory

```
cd Project-My-Debtors-Team-38
```

Create a Virtual Environment

```
python -m virtualenv env
```

Activate Virtual Environment

```
env\scripts\activate
```

Install Dependencies

```
pip install -r requirements.txt
```
Create .env file in SDM project level containing SECRET_KEY='' 


Migrate Database 

```
python manage.py migrate
```
Create Super User 
```
python manage.py createsuperuser
```
Finally, Start The Server.
```
python manage.py runserver
```


