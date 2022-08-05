# Project-My-Debtors-Team-38
A platform that allows schools in a certain locality list directory of people owing them to help them avoid going to other schools.


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


## Tech Stack

* __Design__<br/> Figma <img src="https://res.cloudinary.com/dc29czhf9/image/upload/v1659109673/Figma-logo_pw2gqg.svg" width="20" height="20">

* __Frontend__<br/>
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

* __Backend__<br/>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

* __Database__<br/>
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

* __Project Management and Version Control__<br/>
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


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

## How to Contribute
  1. Create a new branch to make your changes:<br/>
  
     `git checkout -b <your-name/task>`<br/> 
     
      and make the required changes.<br/>
  
  2. Stage the file: <br/>
  
     `git add <your-changed-file>`<br/>
  
  3. Make sure your commit message is detailed with what you changed and where you changed it and commit your file: <br/>
  
    `git commit -m <your-message>`
    
  4. Push your local changes: <br/>
  
     `git push origin <your-branch-name>` <br/>
  
     If an error occurs here, it means that someone has made changes to the original file while you were working. <br/>
    
     Simply run:<br/>
     
     `git pull origin main`  to sync your local file with the current main file<br/>
     
     run `git push origin <your-branch-name>` again.
    
  5. Visit the remote url on Github to create a pull request.
  
  6. Wait for a team member to review your pull request.
  
  7. Merge pull request after review.


## Acknowledgements 🚀 

<p>
  <img src="https://res.cloudinary.com/zuri-team/image/upload/zuriboard/tenant-logo/wmqxdxt4skv05wsvc21o.png"
       alt="Zuri Logo"
  >
</p>
