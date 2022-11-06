# Title

## FitSpace

Milestone Project 4 Full Stack Frameworks with Django
## Description

* FitSpace is a site dedicated to the fitness and health of women. Users can register to join the community set up around the site. It is an e-commerce platform  offering products for users to purchase to help aid their fitness, recovery and nutriton. 

 ## User Experience (UX)

### First Time Visitor Goals

* As a First Time Visitor - I would like to visit a site that is easy to navigate = Landing page holds all navigation options, links and search bar

* As a First Time Visitor - I would like to visit this site to whats available for my training needs = Browse through the products available.

* As a First Time Visitor – I would like to access guidance on how to manage my fitness/health = Site provides specially constructed fitness packages.

### Returning/Frequent Visitor Goals

* As a Returning Visitor – I will enjoy becoming part of the like-minded community set up around this site = There are Social media links to keep users connected by sharing further ideas, stories and images. 

* As a Returning Visitor - I will return to the site to purchase more items = Being a registered user will allow for special offers and discounts on items. 

* As a Returning Visitor – I will continue to gain fitness/health guidance from the site = New products and specialist help will be added regularly. 


## Features

Features of the FitSpace website include:

* Register: The site visitor can add their details to open an account on the site.
* Sign In: The site visitor can login to the site if they are an existing user.
* Contact: Any User can contact the site owner by email.
* Logout: Alows users to log out of their account.
* Sort: Any user can sort the products by price, name or category.
* Search: Any user can search the site using keywords.
* Checkout: Any user can make a secure purchase using Stripe.

### CRUD Functionality

The FitSpace website has been built around the principles of CRUD (Create, Read, Update, Delete). All of these actions can be implemented on the site:

* Add Product: The superuser (Admin) can add products to the database.
* View Products: Any user can view the offered items and the superuser (Admin) can also view them within the database.
* Edit Product: The superuser (Admin) can edit products that are already in the database.
* Delete Product: The superuser (Admin) can delete products that are already in the database.


## Design
### General design

* The site has a  

### Colour Scheme

* The custom colours added to this site are  - 

* ![#65a3b3](https://placehold.co/15x15/65a3b3/65a3b3.png) `#65a3b3`
* ![#D3BC8D](https://placehold.co/15x15/D3BC8D/D3BC8D.png) `#D3BC8D`
* ![#746661](https://placehold.co/15x15/746661/746661.png) `#746661`
* ![#fff](https://placehold.co/15x15/fff/fff.png) `#fff`
* ![#222](https://placehold.co/15x15/222/222.png) `#222`


  
### Typography

* 'Mulish' was chosen as the main font of the site with 'sans-serif' as the fallback font.
* 'Kalama' was used in the design of the FitSpace logo'.

### Imagery 

## Wireframes
![image](https://user-images.githubusercontent.com/95102264/194755021-c2f90f47-3108-4cf4-af64-dee249d36c96.png)

![image](https://user-images.githubusercontent.com/95102264/194755115-4da331c7-2f5f-4a91-a9a4-c869fc601732.png)

* Although the final appearance of the site differs from the initial wireframe idea (above), the concept of the site remains the same. The wireframe design shows the plan to create a site dedicated to fitness and health specifically of women (although site is obviously available to all). The intention is for the site to be aimed at those serious about changing their lifestyle and addressing their health issues - and this will hopefully be translated within the appearance of the site. The landing page will have links to items or services available to purchase. There will be a search bar for easy navigation and there will be links to social media where users can interact and gain support from likeminded users. 


 ## Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3)
* [JavaScript (ES6)](https://en.wikipedia.org/wiki/JavaScript)
* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks, Libraries & Programs Used

* [Django](https://www.djangoproject.com/)
* Django Crispy Forms: was used for all forms on the site.
* Django Allauth: was used for user authentication on the site.
* [Stripe](https://stripe.com/en-gb): Was used to handle payments on the site.
* [Bootstrap](https://getbootstrap.com/): Was used to aid reponsive design.
* [Amazon Web Services S3](https://aws.amazon.com/): Used to store static CSS and Javascript files, and images.
* [Google Fonts](https://fonts.google.com/): Was used for the main font(s).
* [Font Awesome](https://fontawesome.com/): Was used for all icons.
* [Google Fonts](https://fonts.google.com/): Was used for all font choices.
* [Git](https://www.gitpod.io): Was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/): Was used to store the project code after being pushed from Git. 
* Pencil: Pencil was used to create the wireframe.
* [Heroku](https://heroku.com/): Hosts the Milestone Project 4 (FitSpace) website.
* [SQLite3](https://www.sqlite.org/): The database that was used in production.
* [PostgreSQL](https://www.postgresql.org/): The database used by the deployed site.
* [JQuery](https://jquery.com/): Used extensively throughout the site to provide functionality for Bootstrap elements, and for Stripe.
* [https://www.Responsivedesignchecker.com]: Used to check the responsive design of the site on various devices.
* [Canva](https://www.canva.com/): Was used to create the FitSpace logo.

## Testing

For all testing documentation, please refer to the [TESTING.md](TESTING.md) file.
## Deployment

The site was deployed to Heroku. The live link can be found at [FitSpace](https://fit-space.herokuapp.com/)

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

* Code Institute Boutique Ado Project: Much of this project was copied and adapted from the Code Institute 'Boutique Ado' project.
* My Mentor Tim Nelson, for his great help, guidance and patience throughout. 
* Tutors and student support at Code Institute.
* Reviewing/revisiting other lessons from the relevant sections of the course via Code Institute. 
* Code Institute Slack Channel, the tutors, staff and fellow students for help answering my many questions. 
* [Stack Overflow](http://www.stackoverflow.com)
* [w3schools](http://www.w3schools.com)

### Content

* All content on the site was either taken from the Boutique Ado project, or written by the developer.


### Media

* Images attributed to: 

* Images taken from [Pexels](https://www.pexels.com/) =
[Exercise Wheel](https://images.pexels.com/photos/8033019/pexels-photo-8033019.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1).
[White Tshirt](https://www.pexels.com/photo/cheerful-black-woman-wearing-white-t-shirt-and-pants-6311641/).
[Yellow top](https://www.pexels.com/photo/serious-black-woman-with-hands-in-pockets-against-rusty-wall-6311674/).
[Gray vest](https://www.pexels.com/photo/fit-woman-in-sportswear-touching-her-hair-6311313/).
[Hoodie 1](https://www.pexels.com/photo/young-ethnic-woman-in-gray-activewear-standing-against-wooden-wall-6311392/).
[Hoddie 2](https://www.pexels.com/photo/content-black-woman-in-comfy-sportswear-standing-in-studio-6311317/).
[Hoddie 3](https://www.pexels.com/photo/content-black-woman-in-comfy-sportswear-in-studio-6311384/).
[Joggers](https://www.pexels.com/photo/determined-black-boxer-hitting-heavy-bag-during-training-in-gymnasium-6998875/).
[Shorts](https://www.pexels.com/photo/a-woman-boxing-while-wearing-virtual-reality-goggles-8097324/).
[Loose vest](https://www.pexels.com/photo/crop-sportswoman-carrying-sport-mat-and-bottle-of-water-before-exercising-4498574/).

* Images taken from [Freepik](https://www.freepik.com/) = 
[Yoga self care](https://img.freepik.com/free-photo/young-woman-exercising-home_1303-29307.jpg?w=740&t=st=1665952098~exp=1665952698~hmac=59ba9b1df76cbca495a5890fe9e4665b97a2ada3d2e89ecc0e0db14c6e4ef84f).
[Nutritionist](https://img.freepik.com/free-photo/bag-groceries-with-copy-space_23-2148262102.jpg?w=740&t=st=1665952182~exp=1665952782~hmac=ed68bafbf86169b756aa348dca5c0bc2bc8b1e5f7c34591e17689750eafd1c93).
[Resistance Band](https://www.freepik.com/free-photo/slim-woman-doing-squats-with-fitness-loop-band-isolated_8471811.htm#query=exercise%20bands&position=13&from_view=search&track=sph).
[Personal Training](https://www.freepik.com/free-photo/sporty-young-woman-doing-plank-exercise-indoors-home_21130290.htm#query=fitness%20training%20at%20home&position=6&from_view=search&track=sph).
[Dumbbell](https://www.freepik.com/free-photo/purple-dumbbells-fitness-concept-isolated-white-background-fitness-concept-isolated-white-background-sport-body-building-concept-healthy-lifestyle-sport-diet-sport-equipment-copy-space_1192649.htm#query=dumbells&position=0&from_view=search&track=sph).
[Kettlebell](https://www.freepik.com/free-photo/woman-training-with-weight-lifting_23440814.htm#query=kettlebell&position=15&from_view=search&track=sph).
[Trainers](https://www.freepik.com/free-photo/pair-trainers_6048744.htm#query=racool_studio%20trainers&position=2&from_view=search&track=sph).
[Yoga mat](https://www.freepik.com/free-photo/close-up-hands-holding-mat_10942103.htm#query=yoga%20mat&position=0&from_view=search&track=sph).
[Vitamins](https://www.freepik.com/free-psd/amber-medicine-bottles-mockup_12582612.htm#page=2&query=pills%20bottle%20mockup&position=11&from_view=search&track=sph).
[Powder](https://www.freepik.com/free-psd/plastic-whey-protein-powder-jar-mockup_23009843.htm#query=protein%20pwder%20mokup&position=3&from_view=search&track=ais).

* Images taken from [Unsplash](https://unsplash.com/) = 
[Weightball](https://unsplash.com/photos/9xL_8KCEQqE).
[Bottle](https://unsplash.com/photos/o6fSMrsqHOk).
[Blue pants](https://unsplash.com/photos/Y1drF0Y3Oe0).
[Vest](https://unsplash.com/photos/Z72YujnOrlY).


* Background image = [Background image by Senivpetro on Freepik](https://www.freepik.com/free-photo/young-woman-boxer-training-gym_6255898.htm#page=2&query=fitness&position=0&from_view=search&track=sph).

* About us image = [About us page image by Freepik on Freepik](https://www.freepik.com/free-photo/medium-shot-smiley-women-running-together_20081880.htm#query=healthy%20women%20outside&position=45&from_view=search&track=sph).
* Favicon at [Flaticon](https://www.flaticon.com/free-icon/lotus_2647603?term=yoga&page=1&position=23&page=1&position=23&related_id=2647603&origin=search).  


### Future features

* With further development,         