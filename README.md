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
      - [Code Structure](#code-structure)
      - [Other Directories and files](#other-directories-and-files)
      - [Database](#database)
      - [Data Models](#data-models)
    + [Scope](#scope)
      - [Customer User Stories](#customer-user-stories)
      - [Site Owner User Stories](#site-owner-user-stories)
    + [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
    + [Surface](#surface)
      - [Colors](#colors)
      - [Typography](#typography)
    + [Features](#features)
      - [Existing Features](#existing-features)
      - [Features Yet to Implement](#features-yet-to-implement)
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

* Payment Successful - The page show when a payment has successfully been made, showing the order information

#### Pages provided by Django

These pages are provided by the Allauth package of the Django framework, but are customised by me to fit in with the rest of the site. Read more about Allauth [here](https://django-allauth.readthedocs.io/en/latest/)

* Sign Up - where users can register for an account on the site

* Sign in - Registered users can log accessing their personal info etc by signing in

* Sign Out - The same goes for signing out

* Various pages for email verification and password reset, etc (16 pages)

#### Code Structure

I have devided the code into apps as per the Django best practice, for the different areas of functionality.

* Home - basic functionality for the home page

* Products - all functionality related to the products on the site

* Profile - functionality regarding the users profile and order data

* Cart - functionality for the users shopping cart

* Checkout - functionality for the user to go through with the order and payment

* Contact - basic functionality for users to get in touch

#### Other Directories and files

* step_up - project folder containing settings, urls and other configuration files for the whole project

* templates - contains the base template and templates (HTML-files with Django logic) for the Django allauth authentication

* manage.py - the main python project file to get the web application running
* README.md - the document you are reading right now, documentation of the whole project

* TESTING.md - documentation of testing the project

* custom_storages.py - configuration for storage of media and static files on AWS S3

* Procfile - needed for deployment to Heroku to specify commands to be executed by the app on startup

* requirements.txt - a list of dependancies (installed packages) that the project requires for the application to function

Enviromental Variables such as API-keys, passwords etc are stored securely in the back end (in the development environment and in the Heroku App settings) so that regular users do not have access to them.

#### Database

The [SQLite](https://www.sqlite.org/index.html) database was used for the development environment, and the [Postgres](https://www.postgresql.org/) database for production as an add-on via Heroku. Both are relational databases and work well with the Django framework used for this project.

#### Data Models

The following models have been used to populate the database and for the site to function as it should:

* Category - the category in which the product is placed

* Product - the model for the product itself and its details

* User - the built in Django User model, facilitates the users basic information

* Profile - the model storing the users product and order information

* Review - a model for users to give the product a rating and a review

* Cart - the model for the users shopping cart

* Order - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data

* LineItem - a model holding the product information for a single product, binding the product model together with the order

* WishList - the customer has the option to save an item, which will then appear in their profile wish list

### Scope

#### Customer User Stories

#### Site Owner User Stories

### Skeleton

#### Wireframes

### Surface

#### Colors

#### Typography

### Features

#### Existing Features

#### Features Yet to Implement

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