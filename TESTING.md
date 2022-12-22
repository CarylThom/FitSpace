## Testing Report for FitSpace Project.

### HTML5 

* W3 Markup Validation report: Using [W3C Markup Validator](https://validator.w3.org/)<br>
Almost all the HTML code passed with no errors - <br>
![htmlPass](https://user-images.githubusercontent.com/95102264/201435675-4fbbdf42-c2f9-4922-8377-d4077d32f20e.png)<br>
**Please Note** - Warnings and errors were given on some pages due to template logic (or templates used form the Boutique Ado project). These were sections of code that I was unable to change due to limited knowledge or time restrictions, or could not change because of the negative effect it had on the functionality of the site.<br>

Example<br>
![htmlError](https://user-images.githubusercontent.com/95102264/201492350-e81c45c8-3fe4-4f54-8c78-b9f96abd36e5.png)

### CSS3 
*CSS Validation report: Using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)<br>

* Checkout.css has no errors. <br>
![image](https://user-images.githubusercontent.com/95102264/201081802-d9a82003-a816-4478-bc99-640d591de7d9.png)

* Static.css has warnings that do not affect the code. <br>
![image](https://user-images.githubusercontent.com/95102264/201081663-98a78196-7a0d-4457-bbed-1c626ffd0333.png)

* Profile.css has no errors. <br>
![image](https://user-images.githubusercontent.com/95102264/201437098-7be56b9e-0d28-469f-9d64-e4c2a23e1a4e.png)<br>

**Please Note** - Warnings and errors were given on some pages due to template logic (or templates used form the Boutique Ado project). These were sections of code that I was unable to change due to limited knowledge or time restrictions, or could not change because of the negative effect it had on the functionality of the site.<br>

### Javascript (ES6) 

* Javascript validation report: Using [beautifytools](https://beautifytools.com/javascript-validator.php)<br>
Javascript tests came out with no errors only warnings that $ was not defined.<br>
Example <br>
![jsError](https://user-images.githubusercontent.com/95102264/201492529-d2b4144f-64ce-4271-b8d6-1ade099e636b.png)<br>

**Please Note** - Warnings and errors were given on some pages due to template logic (or templates used form the Boutique Ado project). These were sections of code that I was unable to change due to limited knowledge or time restrictions, or could not change because of the negative effect it had on the functionality of the site.<br>

### Python3 

* PEP8 Python Validation report: [pep8ish](https://pep8ish.herokuapp.com/)<br>
Almost all Python files have no errors<br>
![pythonTest](https://user-images.githubusercontent.com/95102264/201492664-fb130a63-f954-4044-86b9-fb6f3ad1f7d6.png)<br>
Although, due to my currently limited knowledge and/or time restrictions, Checkout views.py still has 1 error <br>
![pythonError1](https://user-images.githubusercontent.com/95102264/201492831-1a4e2e18-05a6-4b2c-b47b-2a5c7f8c3b59.png)<br>
As well as, Checkout models.py still with 2 errors <br>
![pythonError2](https://user-images.githubusercontent.com/95102264/201492895-7ea1eb8c-9c8c-4373-9d22-ced84453c895.png)<br>
And, Product views.py with 2 errors <br>
![pythonError3](https://user-images.githubusercontent.com/95102264/201492987-80f7467e-9e2f-4576-b8e9-92f05c2c5e7f.png)


**Please Note** - Warnings and errors were given on some pages due to template logic (or templates used form the Boutique Ado project). These were sections of code that I was unable to change due to limited knowledge or time restrictions, or could not change because of the negative effect it had on the functionality of the site.<br>

### Stripe Payment

* All Stripe payments are being processed correctly<br>
![image](https://user-images.githubusercontent.com/95102264/201218882-86b79ac6-cc17-415b-a188-ac6fc2b046ef.png)

### Admin

* **Orders**
* All orders are being processed <br>  
![image](https://user-images.githubusercontent.com/95102264/201215815-f0250465-525b-4476-8066-5d3bec728113.png)<br>

And entering the database <br>
![image](https://user-images.githubusercontent.com/95102264/201216126-fa7b36d5-2bb4-4252-a797-9cff81cdc88c.png)

* **Register**
* Users are fully able to register for an account that is then stored in the database<br>
![image](https://user-images.githubusercontent.com/95102264/201216666-34ebb66e-b698-4123-ad12-cc1794833385.png)<br>

Users are then able to view order history in their Profile <br>
![image](https://user-images.githubusercontent.com/95102264/201217048-34840a0d-53cd-47f2-805e-2e32517772cb.png)<br>

Users can then log out of their account/profile <br>
![image](https://user-images.githubusercontent.com/95102264/201217404-e37fdeb1-c76f-4a64-8b47-c23174adfa8b.png)

* **Contact**
* Information gathered from the contact form is stored within the database <br>
![image](https://user-images.githubusercontent.com/95102264/201218298-7e504117-d94d-4ffb-8b8c-319a47e69f96.png)

* **Newsletter**
* Information gathered from newsletter form is stored within the database <br>
![image](https://user-images.githubusercontent.com/95102264/209242441-30539bd9-181b-4414-b87f-5ae44cdff086.png)

### Email Confirmation

* **Checkout** 
* Confirmation of payment email is shown in the terminal<br>
![image](https://user-images.githubusercontent.com/95102264/201415640-83ab3561-34c6-451c-8b07-b7494757c3d9.png)<br>

Confirmation email is also sent to customer <br>
![image](https://user-images.githubusercontent.com/95102264/201422817-a9655999-de3f-490d-88c7-5308939b9482.png)

* **Contact**
* Email sent by customers show in the terminal<br>
![image](https://user-images.githubusercontent.com/95102264/201416497-71e99d41-68e8-4d7f-9b76-8f56e1f34f37.png)<br>

Email sent by customers are sent to site email address<br>
![image](https://user-images.githubusercontent.com/95102264/201417935-a260b501-731f-4802-a55d-224e206d902e.png)

* **Newsletter**
* Confirmation email for newsletter subscription is shown in the terminal <br>
![image](https://user-images.githubusercontent.com/95102264/209241752-6160cdd9-4133-47ea-a048-593ae27d46c5.png)<br>



## Lighthouse test report

* ![image](https://user-images.githubusercontent.com/95102264/200916026-ce92c4e1-8dd3-49dd-8e3e-8718644954d1.png)

## Browser Compatibility

* ### Site is responsive on all main browsers:

* **Microsoft Edge** <br>
![image](https://user-images.githubusercontent.com/95102264/200917199-a76f072b-3559-435e-a8ab-580bac68bf6c.png)

* **Google Chrome** <br>
![image](https://user-images.githubusercontent.com/95102264/200917558-3b8923f0-1aea-4da6-9eba-fd10aa62ab80.png)

* **Mozilla Firefox** <br>
![image](https://user-images.githubusercontent.com/95102264/200918257-aab2228c-8729-4c20-8cbd-0c31a00e8246.png)

* ### Site is responsive on all mobile devices:

* **Phone** <br>
![image](https://user-images.githubusercontent.com/95102264/200919414-61d02a1b-33f1-4424-915e-cc59ada0a957.png)


* **Tablet** <br>
![image](https://user-images.githubusercontent.com/95102264/200919700-bc1d34a3-699a-4daa-82b2-e68108bd2802.png)