# StepUp

StepUp is an ecommerce web application for customers seeking to purchase shoes online.

This is the fifth and last milestone project for the Code Institute Diploma in Fullstack Software Development.

Users can create accounts and administrators have full write and delete access to all data. To test an administrator account, send me a pm at contact@johnvenkiah.com and I'll send the details.

You can view the deployed site [here](https://stepup-shoes.herokuapp.com/)

![Mockup of live site on different devices](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/mockup.jpg)


## Table of Contents

- [Project Overview](#project-overview)
- [User Experience](#user-experience)
  * [Strategy](#strategy)
    + [Primary Goals](#primary-goals)
    + [Business Model](#business-model)
    + [Marketing](#marketing)
  * [Structure](#structure)
    + [Pages](#pages)
    + [Pages provided by Django](#pages-provided-by-django)
    + [Technical Design](#technical-design)
      - [Code Structure](#code-structure)
      - [Database](#database)
      - [Schema of models](#schema-of-models)
      - [Data Models](#data-models)
  * [Scope - Epics and User Stories](#scope---epics-and-user-stories)
    + [Epic 1: Base functionality and ease of use](#epic-1-base-functionality-and-ease-of-use)
    + [Epic 2: Products](#epic-2-products)
    + [Epic 3: The Cart](#epic-3-the-cart)
    + [Epic 4: Checkout](#epic-4-checkout)
    + [Epic 5: User registration and account](#epic-5-user-registration-and-account)
    + [Epic 6: The Wish List](#epic-6-the-wish-list)
    + [Epic 7: Reviews](#epic-7-reviews)
    + [Epic 8: Contact](#epic-8-contact)
    + [Epic 9: Site Owner functionality](#epic-9-site-owner-functionality)
  * [Skeleton](#skeleton)
    + [Wireframes](#wireframes)
  * [Surface](#surface)
    + [Colors](#colors)
    + [Typography](#typography)
- [Existing Features](#existing-features)
  * [Feature 1: The Navbar](#feature-1-the-navbar)
  * [Feature 2: The Home Page](#feature-2-the-home-page)
  * [Feature 3: The Footer](#feature-3-the-footer)
  * [Feature 3: The Products List](#feature-3-the-products-list)
  * [Feature 4: The Product Detail Page](#feature-4-the-product-detail-page)
  * [Feature 5: The Cart](#feature-5-the-cart)
  * [Feature 6: The Checkout Page](#feature-6-the-checkout-page)
  * [Feature 7: The Order Successful Page](#feature-7-the-order-successful-page)
  * [Feature 8: The Sign Up/In/Out Pages](#feature-8-the-sign-upinout-pages)
  * [Feature 9: MyStepUp](#feature-9-my-stepup)
  * [Feature 10: The Wish List](#feature-10-the-wish-list)
  * [Feature 11: The Contact Page](#feature-11-the-contact-page)
  * [Feature 12: The Admin Features](#feature-12-the-admin-features)
  * [Feature 13: The Django Admin](#feature-13-the-django-admin)
- [Features Yet to Implement](#features-yet-to-implement)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries and Other Resources](#frameworks-libraries-and-other-resources)
- [Testing](#testing)
- [API's and Configuration](#apis-and-configuration)
- [Deployment](#deployment)
  * [Forking the GitHub Repository](#forking-the-github-repository)
  * [Making a Local Clone](#making-a-local-clone)
  * [Heroku](#heroku)
  * [AWS S3](#aws-s3)
- [Validation](#validation)
- [Bugs](#bugs)
- [Credits](#credits)
  * [Copyrights](#copyrights)
    + [Media](#media)
    + [Content](#content)
  * [Coding Tips and Tricks](#coding-tips-and-tricks)
  * [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>






## Project Overview

StepUp is an assignment for the Code Institute Diploma in Full Stack Software Development, but also meant to be applicable in a real world scenario (except for the products being fictional of course).

The focus points for this application are ecommerce, using the Django framework and the ability to go through with a payment for an order.

## User Experience

### Strategy

#### Primary Goals

**The site owners primary goals are:**

* To be able to sell the stores products online

* To have the ability to add, remove or edit products in the store

* To access a customers order, edit and/or remove it if necessary

* To access and keep track of customer information

* To own a website which is easy to use and navigate, for all types of users on all devices.

**A potential customers primary goals are:**

* To be able to view details of and purchase any of the available products from the online store.

* To be able to register for an account

* To see my order history in their account

* To be able to edit their account details or remove their account

* To easily navigate the whole website and keep track of all user interactions, for example the products in their cart and how much they have spent

#### Business Model

I have chosen a fairly traditional B2C (Business to Customer without middle person) application, which has a straightforward and user friendly interface. This online store offers no products of their own and relies on the wholesale of branded products. A real world version of the store would list all the retailers it is affiliated with.

The intentions should be obvious and users should know as soon as they enter the site what it offers and how to use it's features.

#### Marketing

This site has a Facebook Business page with a link on the home page too. It can be viewed [here](https://www.facebook.com/stepupshoes-estore/)

Upon registering for an account, customers can check a box to receive news and offers through email via Mailchimp.

### Structure

This website has 9 custom pages, with a dynamic navigation bar at the top of the screen, giving users access to the most important pages at all times.

#### Pages

* Home - The landing page of the site, with a full screen carousel hero image giving first time visitors a nice welcome

* Products List - This is a list of the products when clicking on a category in the navbar, or performing a search

* Product Detail - The dedicated page for a specific product, where users can read a description and perform all given tasks for the product

* Add Product - This is where admin users can add new products to the website

* Edit Product - The page for admins to edit or delete products

* My StepUp - The users order history, billing and shipping info is here, as well as the users wish list, editable here in the My StepUp page.

* Cart - A user purchases an item by adding it to the cart; clicking on it will show all cart items

* Checkout - Here users enter their delivery details and card info to proceed with their order

* Order Successful - The page show when a payment has successfully been made, showing the order information

#### Pages provided by Django

These pages are provided by the Allauth package of the Django framework, but are customised by me to fit in with the rest of the site. Read more about Allauth [here](https://django-allauth.readthedocs.io/en/latest/)

* Sign Up - where users can register for an account on the site

* Sign in - Registered users can log accessing their personal info etc by signing in

* Sign Out - The same goes for signing out

* Various pages for email verification and password reset, etc (16 pages in total)

#### Technical Design

##### Code Structure

I have devided the code into apps as per the Django best practice, for the different areas of functionality.

* Home - basic functionality for the home page

* Products - all functionality related to the products on the site

* Profile - functionality regarding the users profile and order data (My StepUp)

* Cart - functionality for the users shopping cart

* Checkout - functionality for the user to go through with the order and payment

* Contact - basic functionality for users to get in touch

**Other Directories and files**

* step_up - project folder containing settings, urls and other configuration files for the whole project

* templates - contains the base template and templates (HTML-files with Django logic) for the Django allauth authentication

* manage.py - the main python project file to get the web application running
* README.md - the document you are reading right now, documentation of the whole project

* TESTING.md - documentation of testing the project

* custom_storages.py - configuration for storage of media and static files on AWS S3

* Procfile - needed for deployment to Heroku to specify commands to be executed by the app on startup

* requirements.txt - a list of dependancies (installed packages) that the project requires for the application to function

Enviromental Variables such as API-keys, passwords etc are stored securely in the back end (in the development environment and in the Heroku App settings) so that regular users do not have access to them.

##### Database

The [SQLite](https://www.sqlite.org/index.html) database was used for the development environment, and the [Postgres](https://www.postgresql.org/) database for production as an add-on via Heroku. Both are relational databases and work well with the Django framework used for this project.

##### Schema of models

Below is a schema of the models used in this application, created with [Lucidchart](https://lucid.co/product/lucidchart)

![Schema of models](#)

##### Data Models

The following models have been used to populate the database and for the site to function as it should:

* **Category** - the category in which the product is placed

* **Brand** - the brand of the product

* **Product** - the model for the product itself and its details

* **User** - the built in Django User model, facilitates the users basic information

* **Profile** - the model storing the users product and order information

* **Review** - a model for users to give the product a rating and a review

* **Order** - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data

* **LineItem** - a model holding the product information for a single product, binding the product model together with the order

* **WishListItem** - the customer has the option to save an item, which will then appear in their wish list on the My StepUp page

### Scope - Epics and User Stories

#### Epic 1: Base functionality and ease of use

1. As a user, the intention of the specific page is made clear to me, so that I know the purpose of that page

2. As a user, I can access important links such as home, products, my cart, sign in/out, and My StepUp by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site

3. As a user, I can see a form to register for newsletters repeatedly throughout the website, so that I can receive news on products and campaigns

4. As a user, I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook

5. As a user, it is visible if I am signed in or not, so that I am made aware of this

6. As a user, the choices I make on the site are confirmed to me, so that I am always aware of them

#### Epic 2: Products

7. As a user, I can browse a list of products for sale on the site so that I can find the product I seek

8. As a user, i can perform a search, so that products matching the search appear in the products list

9. As a user, I can sort the products list by category, alphabetically or by rating, so that i can quickly find the product I seek

10. As a user, I can view the most important details of the product in the product list, such as model, brand, category, price, rating, and image so that i know most details without having to click on the product

11. As a user, i can click the product in the products list so that I can view the products details

12. As a user, I can choose the size of the product, as well as the quantity, so that I can purchase the correct size/quantity

#### Epic 3: The Cart

13. As a user, I can add a product to my cart by clicking ’Add to Cart’ from the product detail page so that I can purchase the product

14. As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be

15. As a user, i can adjust the quantity of the product chosen after adding it to the shopping cart

16. As a user, I can view the products added to my cart by clicking the cart icon or by adding an item to the cart

17. As a user, I can click the remove from cart button, so that I can easily remove products from my cart

#### Epic 4: Checkout

18. As a user, I can click on Proceed to Checkout, so that I can purchase the items in my cart

19. As a logged in user, on the Checkout page, I can choose to save my delivery address to My StepUp, so that I can retain it for future orders

20. As a user, i can enter my card details on the checkout page, so that I can make the desired purchase

21. As a user, I am informed of whether my purchase was successful or not via the Order Successful page, as well as via an email sent upon order confirmation

#### Epic 5: User registration and account

22. As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits

23. As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users

24. As a user, I have to confirm my email address to complete my account registration

25. As a logged in user, i can view a My StepUp page, so that I can view my previous orders, and view, update or remove my delivery and contact details

26. As a logged in user, I can add my delivery details to the My StepUp page, so that it is my default delivery address for my order on the checkout page

27. As a logged in user, I can choose to delete my account, so that my user account no longer exists

#### Epic 6: The Wish List

28. As a logged in user, I can add a product to my Wish List, so that I can easily view it later

29. As a logged in user, I can remove a product from my Wish List, so that it no longer is there

30. As a logged in user, I can add products from my Wish List to my cart, so that I can easily purchase them (user story removed for now)

#### Epic 7: Reviews

31. As a user, i can read user reviews for products that have received them, so that I easier know if the product is right for me

32. As a logged in user, i can write a review and rate a product in the list, so that other users can benefit from this

33. As a logged in user, I can remove my review of a product, so that it no longer is there

#### Epic 8: Contact

34. As a user, I can get in touch with the site owner, regardless of whether I am signed in or not

#### Epic 9: Site Owner functionality

35. As a site owner, I can view an admin page, where I can view, add, edit and remove any model instance on the site including profiles, products, categories, orders etc

36. As a site owner, I can add, edit or remove any product on the site

37. As a site owner, I can add, edit or remove any brand on the site

38. As a site owner, I can receive an email from a user that fills in the contact form, so that they can get in touch with me

### Skeleton

#### Wireframes

![Wireframe of Homepage](#)

Wireframe images were made for all pages except for the ones rarely used by the site, for example password change and email confirmation.

All wireframes can be viewed [here](#)

### Surface

#### Colors

![Colors](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/surface/colors.png) (palette generated at https://imagecolorpicker.com/en)

I have chosen the combination of a dark purple night sky as the background, orange and white.

#### Typography



## Existing Features

### Feature 1: The Navbar

The navbar allows users to easily navigate the website, no matter which page they are on. From here they can navigate to all pages of relevance, Home, Products, My StepUp, Cart, Contact, and Sign In/Sign Up.

The navbar is also dynamic, showing the current total of the shopping cart, as well as showing relevant information for that page, for example the checkout button on the cart page.

**User stories covered**

2. As a user, I can access important links such as home, products, my cart, sign in/out, and My StepUp by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site

5. As a user, it is visible if I am signed in or not, so that I am made aware of this

6. As a user, the choices I make on the site are confirmed to me, so that I am always aware of them

8. As a user, i can perform a search, so that products matching the search appear in the products list

14. As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be

16. As a user, I can view the products added to my cart by clicking the cart icon or by adding an item to the cart

23. As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users


### Feature 2: The Home Page

The home page is the landing page of the site, with the purpose to entice the user to proceed to the products.

The user is presented with, apart from the navbar, a two hero image carousel at the top, with short descriptions and links to the relevant categories. Below that are short paragraphs of the sites philosophy and products, as well as a few images to improve the user experience.

**User stories covered:**

1. As a user, the intention of the specific page is made clear to me, so that I know the purpose of that page

2. As a user, I can access important links such as home, products, my cart, sign in/out, and My StepUp by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site

6. As a user, the choices I make on the site are confirmed to me, so that I am always aware of them

### Feature 3: The Footer

The footer is dynamic, and will on most pages display a signup form for a newsletter, as well as a link to the site's Facebook business page and important links, such as contact or home. The footer will display less if the user is on the checkout page, to bring focus to the purchase.

**User stories covered:**

2. As a user, I can access important links such as home, products, my cart, sign in/out, and My StepUp by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site

3. As a user, I can see a form to register for newsletters repeatedly throughout the website, so that I can receive news on products and campaigns

4. As a user, I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook

### Feature 3: The Products List

The products list is dynamic and will show the relevant products, depending on if the user has performed a search, clicked on a category or filtered the products in any other way.

**User stories covered:**

7. As a user, I can browse a list of products for sale on the site so that I can find the product I seek

8. As a user, i can perform a search, so that products matching the search appear in the products list

9. As a user, I can sort the products list by category, alphabetically or by rating, so that i can quickly find the product I seek

10. As a user, I can view the most important details of the product in the product list, such as model, brand, category, price, rating, and image so that i know most details without having to click on the product

### Feature 4: The Product Detail Page

This page shows a dedicated page for the specific product. Here users can choose the size and the quantity of the product, as well as read a description and user reviews of it.

Logged in users can also write and remove their own reviews here.

**User stories covered:**

11. As a user, i can click the product in the products list so that I can view the products details

12. As a user, I can choose the size of the product, as well as the quantity, so that I can purchase the correct size/quantity

31. As a user, i can read user reviews for products that have received them, so that I easier know if the product is right for me

32. As a logged in user, i can write a review and rate a product in the list, so that other users can benefit from this

33. As a logged in user, I can remove my review of a product, so that it no longer is there

### Feature 5: The Cart

The Cart is the users digital shopping cart, containing all products the user has added to it.
It is partially visible in the navbar but has a dedicated page through which users can go through with the payment when they are done shopping.

**User stories covered:**

13. As a user, I can add a product to my cart by clicking ’Add to Cart’ from the product detail page so that I can purchase the product

14. As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be

15. As a user, i can adjust the quantity of the product chosen after adding it to the shopping cart

16. As a user, I can view the products added to my cart by clicking the cart icon or by adding an item to the cart

17. As a user, I can click the remove from cart button, so that I can easily remove products from my cart

### Feature 6: The Checkout Page

The checkout page features a form for the user to fill in, with delivery address, contact and card info. Here, users can also opt in for a newsletter, should they wish to do so.

**User stories covered:**

18. As a user, I can click on Proceed to Checkout, so that I can purchase the items in my cart

19. As a logged in user, on the Checkout page, I can choose to save my delivery address to My StepUp, so that I can retain it for future orders

20. As a user, i can enter my card details on the checkout page, so that I can make the desired purchase

### Feature 7: The Order Successful Page

If the user has made a successful purchase, the order created will be displayed to the user. This also informs the user that the order confirmation was sent to the users email address, so that the user can close their browser window should they wish.

**User stories covered:**

21. As a user, I am informed of whether my purchase was successful or not via the Order Successful page, as well as via an email sent upon order confirmation

### Feature 8: The Sign Up/In/Out Pages

Signing up, in and out are vital parts of this site, allowing users to save customer details to improve the users experience of the site. It also creates a possibility for the site owner to gain revisiting customers.

**User stories covered:**

22. As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits

23. As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users

24. As a user, I have to confirm my email address to complete my account registration

### Feature 9: My StepUp

Each user can access their own personal profile where they can enter their delivery information, subscribe or unsubscribe to the newsletter and keep track of their orders.

**User stories covered:**

25. As a logged in user, i can view a My StepUp page, so that I can view my previous orders, and view, update or remove my delivery and contact details

26. As a logged in user, I can add my delivery details to the My StepUp page, so that it is my default delivery address for my order on the checkout page

27. As a logged in user, I can choose to inactivate my account, so that I can cancel my account should I wish to

### Feature 10: The Wish List

Users can also add products to their Wish List, if they do not wish to purchase items straght away. The products will remain in the wish list until the user has purchased them or removed them from the list.

**User stories covered:**

28. As a logged in user, I can add a product to my Wish List, so that I can easily view it later

29. As a logged in user, I can remove a product from my Wish List, so that it no longer is there

30. As a logged in user, I can add products from my Wish List to my cart, so that I can easily purchase them

### Feature 11: The Contact Page

This is a standard contact form, through which users can contact the site owner. The form is sent by email to the site owner.

**User stories covered:**

34. As a user, I can get in touch with the site owner, regardless of whether I am signed in or not

37. As a site owner, I can receive an email from a user that fills in the contact form, so that they can get in touch with me

### Feature 12: The Admin Features

There are extra features for admin users, so that site owners can edit products on the site.

**User stories covered:**

36. As a site owner, I can add, edit or remove any product on the site

### Feature 13: The Django Admin

The Django framework provides an excellent admin interface which this site has taken full advantage of. The admin panel of this site contains all instances of all database models, and the ability to edit, remove or add instances.

**User stories covered:**

35. As a site owner, I can view an admin page, where I can view, add, edit and remove any model instance on the site including profiles, products, categories, orders etc

## Features Yet to Implement

## Technologies Used

### Languages

- [Python 3.8](https://www.python.org/) was used for backend programming

- [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for building all web pages

- [CSS3](https://en.wikipedia.org/wiki/CSS) was utilized for styling the website

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for frontend programming

### Frameworks, Libraries and Other Resources

This project is built solely through the framework [Django](https://www.djangoproject.com/), and I have tried to make use of its many powerfiul features.

- I have used [Bootstrap 4](https://getbootstrap.com/) as a framework for styling for efficiency purposes.

- The JavaScript framework [JQuery](https://jquery.com/) was used to minimize written code.

- [Font Awesome](https://fontawesome.com/) fonts were used for all icons in this project.

- [Google Fonts](https://fonts.google.com/) - Were used for all fonts in this project.

- [Facebook Pages](https://www.facebook.com/pages/create/?ref_type=site_footer) was used to create the Facebook Business Page that is linked on the site.

- [Mailchimp](https://mailchimp.com/) was used to create the newsletter signup form.

- [Git](https://git-scm.com/) - Version control system used to commit and push to Github via Gitpod.

- [Github](https://github.com/) - The projects repository and all its branches were commited,
and pushed to Github.

- [Heroku](https://www.heroku.com) - Used to deploy the application.

- [AWS S3 Bucket](https://aws.amazon.com/s3/) - Used to host media (images) and static(CSS and JavaScript) files for the site.

- [Gitpod](https://gitpod.com/) - All code was written and tested with the Gitpod web-based IDE.

- [Balsamiq Wireframes](https://balsamiq.com/wireframes/) was used to create wireframe images of the website which you can view [here](#).

- [Lucidchart](https://lucid.co/product/lucidchart) was used to create the visual [model schema](#schema-of-models) of the project.

## Testing

## API's and Configuration

## Deployment

### Forking the GitHub Repository

To make a clone, or 'Fork' this repository, follow the steps below.

1. Access your GitHub account and find the relevant repository.
2. Click on 'Fork' on the top right of the page.
3. You will find a copy of the repository in your own Github account.

### Making a Local Clone

1. Access your GitHub account and find the relevant repository.
2. Click the 'Code' button next to 'Add file'.
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Open Git Bash.
5. Access the directory you want the clone to be have.
6. In your IDE's terminal type 'git clone' and the paste the URL you copied.
7. Press Enter.
8. You now have a local clone.

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at [heroku.com](https://www.heroku.com/)
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to <Python> and <NodeJS> in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository
11. All done!

### AWS S3

The deployed version of this website has static(CSS and JavaScript) and media files hosted to it via a web based service called Amazon Web Services S3 Bucket.

The steps to take are:

1. Create an account at aws.amazon.com
2. Navigate to the IAM application and create a user and group
3. Set the AmazonS3FullAccess for the user and copy the AWS ACCESS and SECRET keys as config vars to your workspace and deployment environment
4. Create a new Bucket within the S3 application with an appropriate name.
5. Enable public access for your bucket so users can access and use the services on your website (upload, view, download, etc). More info can be read in the official documentation: https://aws.amazon.com/s3/

## Validation

Thourough validation of all code was made without errors. The results can be viewed [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/validation/VALIDATION.md).

## Accessibility

Accessibility tests were also performed with the [WAVE](https://wave.webaim.org/) Web Accessibility Evaluation Tool and passed all tests. They can be viewed [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/accessibility/ACCESSIBILITY.md).

## Bugs

## Credits

### Copyrights

#### Media

#### Content

### Coding Tips and Tricks

### Acknowledgments
