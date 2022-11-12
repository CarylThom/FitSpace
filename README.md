![MainImage](https://user-images.githubusercontent.com/95102264/200198834-405e318f-cf53-49e3-8d7b-3615f2b73c6b.png)

# Title

## FitSpace

Milestone Project 4 Full Stack Frameworks with Django
## Description

* FitSpace is a site dedicated to the fitness and health of women. Users can register to join the community set up around the site. It is an e-commerce platform offering products for users to purchase to help aid their fitness, recovery and nutriton. 

 ## User Experience (UX)

### First Time Visitor Goals

* **As a First Time Visitor** - " I would like to visit a site that is easy to navigate " = The site landing page holds all navigation options such as links to all locations and a search bar

* **As a First Time Visitor** - " I would like to visit this site to discover what's available for my training needs " = The user can browse all the products available or sort them by price, categoy and rating

* **As a First Time Visitor** – " I would like to access guidance on how to manage my fitness/health " = The site offers specially constructed fitness packages for all the users needs.

### Returning/Frequent Visitor Goals

* **As a Returning Visitor** – " I will enjoy becoming part of the like-minded community set up around this site " = There are Social media links to keep users connected by sharing their own ideas, stories and images.  

* **As a Returning Visitor** -  " I will return to the site to purchase more items " = Being a registered user will allow for special offers and discounts on items. 

* **As a Returning Visitor** – " I will continue to gain fitness/health guidance from the site " = New products and specialist help will be added to the site regularly. 


## Features

Features of the FitSpace website include:

* **Log In & Register**: The site visitor can add their details to open an account or sign in to their existing account on the site from the My Account tab.<br>
![RegisterSignIn](https://user-images.githubusercontent.com/95102264/200604140-2498e867-f057-4b05-8724-dba16b511812.png)<br>
**Register**<br>
![RegisterForm](https://user-images.githubusercontent.com/95102264/201480161-020f526b-976f-44f3-8b7f-99130afc1cfd.png)<br>
**LogIn**
<br>
![SignInForm](https://user-images.githubusercontent.com/95102264/201480213-e5caeda9-9ebc-43ff-9bae-996061ea47ab.png)

* **Contact**: Any user can contact the site owner from the contact tab.<br>
![ContactTab](https://user-images.githubusercontent.com/95102264/200607528-29b44b79-9ff1-4fd1-9280-0363d6494ed7.png)<br>
 And then filling in the contact form or viewing the address and phone number<br>
![ContactForm](https://user-images.githubusercontent.com/95102264/201478741-4db58d13-c617-4e28-b007-3eeacb567a24.png)
* **Logout**: Allows users to log out of their account.<br>
![LogOut](https://user-images.githubusercontent.com/95102264/201480444-df827031-222b-4aae-93dc-a117dfd1ddd7.png)

* **My Profile**: Registered users can view their profile/shopping history.<br>
![ProfileTab](https://user-images.githubusercontent.com/95102264/200606500-ecbde75c-ce20-46c2-8396-df31660f21ea.png)<br>
![ProfilePage](https://user-images.githubusercontent.com/95102264/201480591-3c769a89-2ab7-46a1-9d8c-808f3cee2f51.png)

* **Sort**: Any user can sort the products by price, name or rating.<br>
![SortBar](https://user-images.githubusercontent.com/95102264/200605763-65901889-d910-419e-afaf-47ec01d1ac75.png)<br>
![SortBarOpen](https://user-images.githubusercontent.com/95102264/201478586-b0d39d17-fde0-4a23-a3d3-14d73463205e.png)
* **Search**: Any user can search the site using keywords. <br>
![SearchBar](https://user-images.githubusercontent.com/95102264/200603437-74525397-7822-4597-85b7-cdfddd96fa1e.png)<br>
* **Checkout**: Any user can make a secure purchase using Stripe.<br>
![CheckoutBtn](https://user-images.githubusercontent.com/95102264/200607935-b73ccc14-6bba-4a7a-94d3-27f1315fc6ca.png)<br>
* **Social Media**: Any user can access FitSpace social media links.<br>
![Social](https://user-images.githubusercontent.com/95102264/200605391-4f8ee83d-482a-4f3d-b953-b9fa3280e63f.png)<br>
* **Admin**: Admin/Superusers can access the Product Admin tab.<br>
![ProductAdminTab](https://user-images.githubusercontent.com/95102264/200607213-a1b7d1d8-4763-4755-8331-3b8342acf65f.png)<br>
![ProductAdmin](https://user-images.githubusercontent.com/95102264/201480759-d819f8c2-1b41-4225-9b6f-5c493ed76bfb.png)

### CRUD Functionality

The FitSpace website has been built around the principles of CRUD (Create, Read, Update, Delete). All of these actions can be implemented on the site:

* **Add Product:** The superuser (Admin) can add products to the database, and through the Product Admin tab as shown above<br>
![AddData](https://user-images.githubusercontent.com/95102264/200648019-3cb62a86-ffbd-436e-975a-4080380f38f4.png)<br>
* **View Products:** Any user can view the offered items. <br>
![Products](https://user-images.githubusercontent.com/95102264/201480977-7acf634e-72bb-4999-be56-57a4eaf975f3.png)
And the superuser (Admin) can also view them within the database.<br>
![ProductsData](https://user-images.githubusercontent.com/95102264/200648177-f5d9dab0-670c-4cd4-b765-dd4193415daa.png)<br>
* **Edit Product:** The superuser (Admin) can edit products that are already in the database.<br>
![EditProduct](https://user-images.githubusercontent.com/95102264/200648559-1083da32-ea4c-4b39-b764-074cf32a6a5e.png)<br>
By clicking on the edit link below the item <br>
![EditLink](https://user-images.githubusercontent.com/95102264/201481089-0f86864f-bbed-45da-8a8d-d40da5abb0c1.png)
* **Delete Product:** The superuser (Admin) can delete products that are already in the database by clicking on the delete button below the item.<br>
![DeleteProduct](https://user-images.githubusercontent.com/95102264/200648913-6c9c20b9-8fd5-4a2d-b3ad-da4ce4b43aaa.png)


## Design
### General design layout & Use
### Top Navbar:

* **Search box:** Search the site using key words.<br>
![SearchHoodie](https://user-images.githubusercontent.com/95102264/201481343-c4fe6ac7-406a-4c5b-bfde-226faa00944f.png)<br>
![ResultHoodie](https://user-images.githubusercontent.com/95102264/201481400-dc316426-8033-4ac2-a4a8-55b789454b15.png)

* **My Account:** is a dropdown menu with the following options:<br />
	**Login:** Login for existing users.<br />
    **Register:** Register as a user.<br>
    ![image](https://user-images.githubusercontent.com/95102264/200604140-2498e867-f057-4b05-8724-dba16b511812.png)

* **Shopping Bag Icon:** Click here to navigate to the shopping bag page.<br>
![ShoppingBag](https://user-images.githubusercontent.com/95102264/200649428-0868463f-8f8b-4c36-9f32-4491b1ddfc92.png)<br>
When bag is empty <br>
![BagEmpty](https://user-images.githubusercontent.com/95102264/201481484-797b4d9a-812b-4fa9-b201-f85631be0c9b.png)<br>
Or full<br>
![BagFull](https://user-images.githubusercontent.com/95102264/201481573-074a4f73-79c8-4a4c-a17e-f63687d09c5d.png)
### Main Navbar:

*  **FitSpace** is a dropdown menu with the following options:<br />
    **About Us:** A short biography of the company.<br />
    **Contact Us:** See contact details or contact the business via a contact form.<br />
    **Social media links:** links to the homepages of  Facebook, Twitter, Instagram, TikTok & YouTube.<br>
    ![FSdropdown](https://user-images.githubusercontent.com/95102264/200649636-cd3efbdc-d17d-4147-b6e6-70d3376af949.png)

*  **Fitness Products** is a dropdown menu with the following options:<br />
    **By Price:** Display items by price.<br />
    **By Ratings:** Display items by ratings.<br />
    **By Categories:** Display items by categories.<br />
    **All Products:** Display all products.<br>
    ![FPdropdown](https://user-images.githubusercontent.com/95102264/200649822-3ce81144-805f-43a4-8da1-8a4e6a60cd47.png)<br>
    Product details can then be seen when the item is choosen <br>
    ![ProductDetail](https://user-images.githubusercontent.com/95102264/201481727-979eec5a-a3ea-48b0-b9dd-e7e44f76301f.png)

*  **Your Fitness** is a dropdown menu with the following options:<br />
    **Clothing:** Show the selection of clothing on offer.<br />
    **Equipment:** Show the selection of fitness equipment on offer.<br />
    **Nutrition:** Show the selection nutritional supplements on offer.<br>
    ![YFdropdown](https://user-images.githubusercontent.com/95102264/200649997-ddfbccc5-d788-469c-b765-32b6e0617808.png)

* **Fitness Plans** is a dropdown menu with the following options:<br />
    **Fitness:** Show all products related to fitness.<br />
    **Nutrition:** Show all products related to nutrition.<br />
    **Recover:** Show all products on recovery and self-care.<br>
    ![FPlandropdown](https://user-images.githubusercontent.com/95102264/200650147-6cf525d8-0389-4ed5-9fc0-617172224d0e.png)

* **Alerts**
There are also a set of alerts that will inform the user of their actions around the site<br>
![Alert1](https://user-images.githubusercontent.com/95102264/201481997-4e108b5e-684e-4e71-bb03-ed9aa54a83d8.png)<br>
![Alert2](https://user-images.githubusercontent.com/95102264/201482058-664d35c1-f349-4bb9-9df0-97e39e76b354.png)<br>
![Alert3](https://user-images.githubusercontent.com/95102264/201482116-a98bd4eb-5fe4-40ca-af59-53ba95e06ecb.png)
* Accessible only to signed- in/registered users on the Top Navbar:<br />
**My Account:** > **My Profile:** To navigate to the session user's profile page.<br />
**Logout:** To logout of the site.

* Accessible only to Superusers/Admin on the Top Navbar:<br />
**Product Admin:** To Use CRUD functionality to manage the site.

* Accessible to all users on the Products page:<br />
**Sort Box:** Allows the user to sort the items by price, rating, name and category.

* Accessible to Superusers/Admin only on the Products page:<br />
**Edit:** Allows Admin to edit a product. <br />
**Delete:** Allows Admin to delete a product.

* Accessible to Superusers/Admin on the Product Admin page:<br />
**Edit:** Allows Admin to edit a product.<br />
**Delete:** Allows Admin to delete a product.

  

### Colour Scheme

* The custom colours added to this site are  - 

* ![#65a3b3](https://placehold.co/15x15/65a3b3/65a3b3.png) `#65a3b3`
* ![#D3BC8D](https://placehold.co/15x15/D3BC8D/D3BC8D.png) `#D3BC8D`
* ![#746661](https://placehold.co/15x15/746661/746661.png) `#746661`
* ![#fff](https://placehold.co/15x15/fff/fff.png) `#fff`
* ![#222](https://placehold.co/15x15/222/222.png) `#222`


  ### Typography

* 'Mulish' <br>![Mulish](https://user-images.githubusercontent.com/95102264/200651279-e142e3cd-52b5-40ef-989d-425e172ada05.png)<br>
(Designed by Vernon Adams, Cyreal, Jacques Le Bailly) was chosen as the main font of the site with 'sans-serif' as the fallback font.
* 'Kalam'<br>![Kalam](https://user-images.githubusercontent.com/95102264/200651924-3ba3d621-85e9-49fa-9c4f-04164acce70f.png)<br>
 (Designed by Indian Type Foundry) was used in the design of the FitSpace logo'.

### Imagery 

## Wireframes
![WireframeMain](https://user-images.githubusercontent.com/95102264/194755021-c2f90f47-3108-4cf4-af64-dee249d36c96.png)

![WireframeProducts](https://user-images.githubusercontent.com/95102264/194755115-4da331c7-2f5f-4a91-a9a4-c869fc601732.png)

* Although the final appearance of the site differs greatly from the initial wireframe idea (above), the concept of the site remains the same. The wireframe design shows the plan to create a site dedicated to fitness and health specifically of women (although site is obviously available to all). The intention is for the site to be aimed at those serious about changing their lifestyle and addressing their health issues - and this will hopefully be translated within the appearance of the site. The landing page will have links to items or services available to purchase. There will be a search bar for easy navigation and there will be links to social media where users can interact and gain support from likeminded users. 

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

* ### **To Heroku**
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
    *   `AWS_ACCESS_KEY_ID` = The access key supplied by AWS.
    *   `AWS_SECRET_ACCESS_KEY` = The secret key supplied by AWS.
    *   `STRIPE_PUBLIC_KEY` = The publishable key supplied by Stripe.
    *   `STRIPE_SECRET_KEY` = The secret key supplied by Stripe.
    *   `STRIPE_WH_SECRET` = The Stripe webhook secret key.
    *   `USE_AWS` = To verify the use of AWS.

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
5.  Type git clone, and then paste the URL that was copied from step 3 above - i.e., `git clone https://github.com/CarylThom/FitSpace`
6. Press Enter to create the local clone.

### Forking

A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

To fork this project go to the top left of the repository, where you see the Fork Icon and click Fork.  This will create a copy of the repository for you.

* ### **With AWS** <br>
All Static and media files for the deployed version of the site are hosted in a Amazon Web Services(AWS) S3 bucket. In order to create your own bucket, please follow the instructions on the AWS website [Here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).

Sign in to the AWS Management Console and open the Amazon S3 console at https://console.aws.amazon.com/s3/.<br>
Choose Create bucket. <br>
The Create bucket wizard opens.<br>
In Bucket name, enter a DNS-compliant name for your bucket.<br>
Add 'storages' to INSTALLED_APPS in settings.py. <br>
Add the following code to settings.py in order to link the AWS bucket to the website: (example)<br>

if 'USE_AWS' in os.environ:<br>
    # Bucket Config<br>
    AWS_STORAGE_BUCKET_NAME = 'fitspace'<br>
    AWS_S3_REGION_NAME = 'eu-west-2'<br>
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')<br>
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')<br>
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'<br>

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

Create a custom_storages.py file in the root level of the project. Inside it, include the locations of the Static Storage and Media Storage.<br>
Delete DISABLE_COLLECTSTATIC from the Heroku Config Variables.<br>
Finally, push to GitHub, and all changes should be automatically pushed to Heroku.

## Data Structure

* Entity Relationship Diagram (ERD) created using [draw.io](https://app.diagrams.net/)
![image](https://user-images.githubusercontent.com/95102264/200966065-c1c8ce85-2647-462c-b84d-9f48e7bdac47.png)

## Credits
### Acknowledgements

* Code Institute Boutique Ado Project: Much of this project was copied and adapted from the Code Institute 'Boutique Ado' project.
* My mentor Tim Nelson, for his help, guidance and patience throughout. 
* Tutors and student support at Code Institute.
* Reviewing/revisiting other lessons from the relevant sections of the course via Code Institute. 
* Code Institute Slack Channel, the tutors, staff and fellow students for help answering my many questions. 
* [Stack Overflow](http://www.stackoverflow.com)
* [w3schools](http://www.w3schools.com)

### Content

* All content on the site was either taken from the Boutique Ado project, or written by the developer.


### Media

* Images attributed to: 

* Product images taken from [Pexels](https://www.pexels.com/) =
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

* Product images taken from [Freepik](https://www.freepik.com/) = 
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

* Product images taken from [Unsplash](https://unsplash.com/) = 
[Weightball](https://unsplash.com/photos/9xL_8KCEQqE).
[Bottle](https://unsplash.com/photos/o6fSMrsqHOk).
[Blue pants](https://unsplash.com/photos/Y1drF0Y3Oe0).
[Vest](https://unsplash.com/photos/Z72YujnOrlY).


* Main background image = [By Senivpetro on Freepik](https://www.freepik.com/free-photo/young-woman-boxer-training-gym_6255898.htm#page=2&query=fitness&position=0&from_view=search&track=sph).<br>
![BGimage](https://user-images.githubusercontent.com/95102264/200653593-5cb5f680-5e19-4c01-a8b2-63fa6063849c.png)<br>

* About us image = [Created by Freepik on Freepik](https://www.freepik.com/free-photo/medium-shot-smiley-women-running-together_20081880.htm#query=healthy%20women%20outside&position=45&from_view=search&track=sph).<br>
![AUimage](https://user-images.githubusercontent.com/95102264/200654289-741327b3-b507-49f6-809e-d48614d784be.png)<br>

* Favicon & Site logo = [Created by monkik at Flaticon](https://www.flaticon.com/free-icon/lotus_2647603?term=yoga&page=1&position=23&page=1&position=23&related_id=2647603&origin=search). <br>
![Favicon](https://user-images.githubusercontent.com/95102264/200654714-dfa7abaf-ff33-430a-9a2d-a41d36903d94.png) 


### Future features

* With further time, development and knowledge of the code, the additional features that would idealy be added to the site include:<br>
More products for sale, especially home gym equipment and eventually own brand clothing.<br>
A site blog where admin can add inspirational stories and for members to see the fitness progressions of others and to add their own.<br>
A reviews section where members/customers can add their own comments about products and their uses.<br>
A newsletter subscription where customers can be kept up to date with news and special offers.<br>
Create personal bespoke designed email account for FitSpace. <br>
Create a barrier against accidental deletion of products by admin. <br>
Make sure that while in their account/profile the name/contact details of registered users is already autofilled within the contact form.


