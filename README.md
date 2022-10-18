# Title

## FitSpace

Milestone Project 4 Full Stack Frameworks with Django
## Description

* FitSpace is a site dedicated to the fitness and health of women. Users can register/subscribe/join the community set up around the site. Products will be availabe for users to purchase to help aid their fitness, recovery and nutriton.

 ## User Experience (UX)

### First Time Visitor Goals

* As a First Time Visitor - I would like to visit a site that is easy to navigate = Landing page holds all navigation options, links and search bar

* As a First Time Visitor - I would like to visit this site to whats available for my training needs = Browse through the products available.

* As a First Time Visitor – I would like to access guidance on how to manage my fitness/health = Site provides specially constructed fitness packages.

### Returning/Frequent Visitor Goals

* As a Returning Visitor – I will enjoy becoming part of the like-minded community set up around this site = There are Social media links to keep users connected by sharing further ideas, stories and images. 

* As a Returning Visitor - I will return to the site to purchase more items = Being a registered user will allow for special offers and discounts on items. 

* As a Returning Visitor – I will continue to gain fitness/health guidance from the site = New products and specialist help will be added regularly. 


## Design

### Features

* The site features a Register and Log in page 
* The site features 
* The site has extra features for admin only (where admin can add and remove categories/products) 
* The site has a feature for 
* The site has a feature where  

### General design

* The site has a  

### Colour Scheme

* The colours used within this site are  - 
  
### Typography

* There are two fonts used for this site 

### Imagery 

## Wireframes
![image](https://user-images.githubusercontent.com/95102264/194755021-c2f90f47-3108-4cf4-af64-dee249d36c96.png)

![image](https://user-images.githubusercontent.com/95102264/194755115-4da331c7-2f5f-4a91-a9a4-c869fc601732.png)

* The initial concept of the wireframe design was to create an app/site dedicated to fitness and health specifically of women (although site is obviously available to all). The intention is for the site to be aimed at those serious about changing their lifestyle and addressing their health issues - and this will hopefully be translated within the appearance of the site. The landing page will have links to items or services available to purchase. There will be a search bar for easy navigation and there will be links to social media where users can interact and gain support from likeminded users. 

## CRUD Functionality

* Full CRUD functionality is demonstrated within the site

*   Create - Admin can create a new record within the database by adding new categories or products.
* Read - Admin and/or users can then read the information from the database when they click on the relevant sections.
* Update - Admin can edit or update the categories and products.
* Delete - Admin can also delete the categories and products.

 ## Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3)
* [JavaScript (ES6)](https://en.wikipedia.org/wiki/JavaScript)
* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))


## Frameworks, Libraries & Programs Used

* [Google Fonts](https://fonts.google.com/): Was used for the main font(s).

* [Font Awesome](https://fontawesome.com/): Was used for all icons.

* [Git](https://www.gitpod.io): Was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

* [GitHub](https://github.com/): Was used to store the project code after being pushed from Git. 
 
* [https://www.Responsivedesignchecker.com]

* Pencil: Pencil was used to create the wireframe.

* Materialize or Bootstrap?

## Testing

For all testing documentation, please refer to the [TESTING.md](TESTING.md) file.
## Deployment

The site was deployed to Heroku. The live link can be found at [FitSpace]()

The steps to deploy a Heroku app are as follows: 
1.  Log in to Heroku or create an account if required.
2.  Create a Heroku app - select 'New', from the drop-down menu select Create New App. The app name provided must be unique.
3.  Select a region.
4.  click Create.
5.  Navigate to the Resources tab and add a Heroku Postgres database.
6.  Access the Settings Tab and find the Config Vars. For this project you will need the following config vars:
    *   `DATABASE_URL` = the url of your heroku postgres database.
    *   `SECRET_KEY` = a secret key for your app.
    *   `PORT` = 5000
    *   `DEBUG` = set to 'True' during development and 'False' upon deployment.
    *   `IP` = 0.0.0.0

Please see this [official documentation](https://devcenter.heroku.com/articles/config-vars) on Heroku configuration for more details.

7.  Navigate to the Deploy tab.
8.  Select GitHub as the deployment method.
9.  Follow steps to link to the appropriate GitHub account.
10. If you wish, enable Automatic Deploys for automatic deployment when you push updates to GitHub. Or alternatively, select the correct branch for deployment from the drop-down menu and click "Deploy Branch" for manual deployment.

Final steps: 
1. Create a `Procfile` in your repository containing `web: python app.py` so that Heroku will identify the app as a Python app.
2. Create an untracked file called `env.py` in your repo and input the config vars you previously established in Heroku above.
3. Create a `requirements.txt` file
    - If you want to freeze your own packages into this file, run `pip3 freeze --local > requirements.txt` in the console.
    - To install only the packages that are already listed in the "allveggie" repo requirements (if making a local copy/clone) run `pip3 install -r requirements.txt` in the console.

### Cloning

Cloning a repository makes it easier to contribute, fix merge conflicts, add or remove files, and push larger commits. To clone this repository from GitHub to a local computer use the following steps:

1.  On GitHub, navigate to the main page of the repository.
2.  Above the list of files, click Code.
3.  Click Use GitHub CLI, then the copy icon.
4.  Open Git Bash and change the current working directory to the location where you want the cloned directory.
5.  Type git clone, and then paste the URL that was copied from step 3 above - i.e., `git clone https://github.com/CarylThom/FitSpace.git`
6. Press Enter to create the local clone.

### Forking

A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

To fork this project go to the top left of the repository, where you see the Fork Icon and click Fork.  This will create a copy of the repository for you.

## Data Structure
## Browser Compatibility

* Microsoft Edge 

* Google Chrome 

* Mozilla Firefox 

* Site is responsive on all mobile devices:

* Phone 

* Tablet 


## Credits

### Acknowledgements

* Mentor Tim Nelson at Code Institute

* Reviewing/revisiting lessons from the relevant sections of the course via Code Institute. 

* Tutors and student support at Code Institute

* Slack

* [Stack Overflow](http://www.stackoverflow.com)

* [w3schools](http://www.w3schools.com)

### Content

* All content was written by the developer except for sections of code that was learned from relevant lessons of the course.


### Media

* Images attributed to: 
* Background image by 
* Favicon at [Flaticon](https://www.flaticon.com/) 


### Future features

* With further development,         