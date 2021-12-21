# StepUp

StepUp is an ecommerce web application for customers seeking to purchase shoes online.

This is the fifth and last milestone project for the Code Institute Diploma in Fullstack Software Development.

Users can create accounts and administrators have full write and delete access to all data. To test an administrator account, send me a pm at contact@johnvenkiah.com and I'll send the details.

You can view the deployed site [here](https://stepup-shoes.herokuapp.com/)

![Mockup of live site on different devices](#)


## Table of Contents

- [StepUp](#stepup)
  * [Project Overview](#project-overview)
  * [User Experience](#user-experience)
    + [Strategy](#strategy)
      - [Primary Goals](#primary-goals)
      - [Business Model](#business-model)
      - [Marketing](#marketing)
    + [Structure](#structure)
      - [Pages](#pages)
      - [Pages provided by Django](#pages-provided-by-django)
      - [Technical Design](#technical-design)
        * [Code Structure](#code-structure)
        * [Database](#database)
        * [Schema of models](#schema-of-models)
        * [Data Models](#data-models)
    + [Scope - Epics and User Stories](#scope---epics-and-user-stories)
      - [Epic 1: Base functionality and ease of use](#epic-1--base-functionality-and-ease-of-use)
      - [Epic 2: Products](#epic-2--products)
      - [Epic 3: The Cart](#epic-3--the-cart)
      - [Epic 4: Checkout](#epic-4--checkout)
      - [Epic 5: User registration and account](#epic-5--user-registration-and-account)
      - [Epic 6: The Wish List](#epic-6--the-wish-list)
      - [Epic 7: Reviews](#epic-7--reviews)
      - [Epic 8: Contact](#epic-8--contact)
      - [Epic 9: Site Owner functionality](#epic-9--site-owner-functionality)
    + [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
    + [Surface](#surface)
      - [Colors](#colors)
      - [Typography](#typography)
  * [Existing Features](#existing-features)
    + [Feature 1: The Navbar](#feature-1--the-navbar)
    + [Feature 2: The Home Page](#feature-2--the-home-page)
    + [Feature 3: The Products List](#feature-3--the-products-list)
    + [Feature 4: The Product Detail Page](#feature-4--the-product-detail-page)
    + [Feature 5: The Cart](#feature-5--the-cart)
    + [Feature 6: The Checkout Page](#feature-6--the-checkout-page)
    + [Feature 7: The Checkout Confirmation Page](#feature-7--the-checkout-confirmation-page)
    + [Feature 8: The Sign Up/In/Out Pages](#feature-8--the-sign-up-in-out-pages)
    + [Feature 9: The Profile](#feature-9--the-profile)
    + [Feature 10: The Wish List](#feature-10--the-wish-list)
    + [Feature 11: The Contact Page](#feature-11--the-contact-page)
    + [Feature 12: The Admin Features](#feature-12--the-admin-features)
    + [Feature 13: The Django Admin](#feature-13--the-django-admin)
  * [Features Yet to Implement](#features-yet-to-implement)
  * [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Frameworks, Libraries and Other Resources](#frameworks--libraries-and-other-resources)
  * [Testing](#testing)
  * [API's and Configuration](#api-s-and-configuration)
  * [Deployment](#deployment)
  * [Bugs](#bugs)
  * [Credits](#credits)
    + [Media](#media)
    + [Content](#content)
    + [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


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

* Profile - The users order history, billing and shipping info is here, as well as the users saved items, editable here in the profile page.

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

* Profile - functionality regarding the users profile and order data

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

* **Product** - the model for the product itself and its details

* **User** - the built in Django User model, facilitates the users basic information

* **Profile** - the model storing the users product and order information

* **Review** - a model for users to give the product a rating and a review

* **Cart** - the model for the users shopping cart

* **Order** - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data

* **LineItem** - a model holding the product information for a single product, binding the product model together with the order

* **WishListAdd** - the customer has the option to save an item, which will then appear in their profile wish list

### Scope - Epics and User Stories

#### Epic 1: Base functionality and ease of use

1. As a user, the intention of the specific page is made clear to me, so that I know the purpose of that page

2. As a user, I can access important links such as home, products, my cart, sign in/out, and profile by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site

3. As a user, I can register for newsletters while registering and on the home page, so that I can receive news on products and campaigns

4. As a user, it is visible if I am signed in or not, so that I am made aware of this

5. As a user, the choices I make on the site are confirmed to me, so that I am always aware of them

#### Epic 2: Products

6. As a user, I can browse a list of products for sale on the site so that I can find the product I seek

7. As a user, i can perform a search, so that products matching the search appear in the products list

8. As a user, I can sort the products list by category, alphabetically or by rating, so that i can quickly find the product I seek

9. As a user, I can view the most important details of the product in the product list, such as model, brand, category, price, rating, and image so that i know most details without having to click on the product

10. As a user, i can click the product in the products list so that I can view the products details

11. As a user, I can choose the size of the product, as well as the quantity, so that I can purchase the correct size/quantity

#### Epic 3: The Cart

12. As a user, I can add a product to my cart by clicking ’Add to Cart’ from the product detail page so that I can purchase the product

13. As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be

14. As a user, i can adjust the quantity of the product chosen after adding it to the shopping cart

15. As a user, I can view the products added to my cart by clicking the cart icon or by adding an item to the cart

16. As a user, I can click the remove from cart button, so that I can easily remove products from my cart

#### Epic 4: Checkout

17. As a user, I can click on Proceed to Checkout, so that I can purchase the items in my cart

18. As a logged in user, on the Checkout page, I can choose to save my delivery address to my profile, so that I can retain it for future orders

19. As a user, i can enter my card details on the checkout page, so that I can make the desired purchase

20. As a user, I am informed of whether my purchase was successful or not via the Order Successful page, as well as via an email sent upon order confirmation

#### Epic 5: User registration and account

21. As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits

22. As a user, I have to confirm my email address to complete my account registration

23. As a logged in user, i can view a profile page, so that I can view my previous orders, and view, update or remove my delivery and contact details

24. As a logged in user, I can add my address to my profile, so that it is my default delivery address for my order on the checkout page

25. As a logged in user, I can choose to inactivate my account, so that I can cancel my account should I wish to

#### Epic 6: The Wish List

26. As a logged in user, I can add a product to my Wish List, so that I can easily view it later

27. As a logged in user, I can remove a product from my Wish List, so that it no longer is there

28. As a logged in user, I can add products from my Wish List to my cart, so that I can easily purchase them

#### Epic 7: Reviews

29. As a logged in user, i can write a review and rate a product in the list, so that other users can benefit from this

30. As a logged in user, I can remove my review of a product, so that it no longer is there

#### Epic 8: Contact

31. As a user, I can get in touch with the site owner, regardless of whether I am signed in or not

#### Epic 9: Site Owner functionality

32. As a site owner, I can view an admin page, where I can view, add, edit and remove any model instance on the site including profiles, products, categories, orders etc

33. As a site owner, I can add, edit or remove any product on the site

34. As a site owner, I can receive an email from a user that fills in the contact form, so that they can get in touch with me

### Skeleton

#### Wireframes

![Wireframe of Homepage](#)

Wireframe images were made for all pages except for the ones rarely used by the site, for example password change and email confirmation.

All wireframes can be viewed [here](#)

### Surface

#### Colors

![Colors](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/surface/colors.png)

I have chosen the combination "Living Coral" and "Pacific Coast", as published on [designwizard.com's article](https://www.designwizard.com/blog/design-trends/colour-combination) on trending color combinations for 2021, as I thought they were sharp, trendy yet simple.

#### Typography



## Existing Features

### Feature 1: The Navbar

### Feature 2: The Home Page

### Feature 3: The Products List

### Feature 4: The Product Detail Page

### Feature 5: The Cart

### Feature 6: The Checkout Page

### Feature 7: The Checkout Confirmation Page

### Feature 8: The Sign Up/In/Out Pages

### Feature 9: The Profile

### Feature 10: The Wish List

### Feature 11: The Contact Page

### Feature 12: The Admin Features

### Feature 13: The Django Admin


## Features Yet to Implement

## Technologies Used

### Languages

### Frameworks, Libraries and Other Resources

## Testing

## API's and Configuration

## Deployment

## Bugs

## Credits

### Media

### Content

### Acknowledgments