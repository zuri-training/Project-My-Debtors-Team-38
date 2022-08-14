## Jp
##### Branches Worked on <br/>
- https://github.com/zuri-training/Project-My-Debtors-Team-38/branches/all?query=jp

##### Tasks <br/>
- Created db schema
- setup SDM project and pushed to github
- created custom user models and forms
- created school, guardian and student profile models
- worked on post model
- linked multiple pages with django views and jinja templating
- used jinja templating system to include pages based on conditions
- worked on post page hifi design
- worked on contend page hifi design
- worked on school directory hifi page layout
- worked on guardian add child user flow
- coded post and comment feature 
- coded add child feature 



| Issues      | Solutions |
| :----------- | :----------- |
| convert django defaut username login to email login| extend django user model, custom user manager, override create user function to use email instead|
| separate users to enforce role based user flow | used proxy models to extend AbstractBaseUser and created profile models for the seperated users as a 1-1 relationship|
| pull urls from different django apps  | used django's namespace feature|
|get nav bar and side bar to show based on requested page| used conditions to check nav variable passed by views to pages|

