# Testing

I have thoroughly tested the StepUp web application manually, and partially with automated tests.

I discovered some bugs during the testing phase, which you can read about [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah#bugs)

## Manual testing

### Overview

As manual testing can be overwhelming for both the tester and the reader, I have created three user cases, in which the tests were performed. As I have tested responsivity on mobile, tablet and desktop screen sizes, I have included images on different pages from different screen sizes.



1. **Regular User Case** - User experience for non-authenticated users, performing all operations available to them. User stories covered in this user case:

    **Epic 1: Base functionality and ease of use**

    1. As a user, the intention of the specific page is made clear to me, so that I know the purpose of that page

    2. As a user, I can access important links such as home, products, my cart, sign in/out, and My StepUp by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site

    3. As a user, I can see a form to register for newsletters repeatedly throughout the website, so that I can receive news on products and campaigns

    4. As a user, I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook

    5. As a user, it is visible if I am signed in or not, so that I am made aware of this

    6. As a user, the choices I make on the site are confirmed to me, so that I am always aware of them

    **Epic 2: Products**

    7. As a user, I can browse a list of products for sale on the site so that I can find the product I seek

    8. As a user, i can perform a search, so that products matching the search appear in the products list

    9. As a user, I can sort the products list by category, alphabetically or by rating, so that i can quickly find the product I seek

    10. As a user, I can view the most important details of the product in the product list, such as model, brand, category, price, rating, and image so that i know most details without having to click on the product

    11. As a user, i can click the product in the products list so that I can view the products details

    12. As a user, I can choose the size of the product, as well as the quantity, so that I can purchase the correct size/quantity

    **Epic 3: The Cart**

    13. As a user, I can add a product to my cart by clicking ’Add to Cart’ from the product detail page so that I can purchase the product

    14. As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be

    15. As a user, i can adjust the quantity of the product chosen after adding it to the shopping cart

    16. As a user, I can view the products added to my cart by clicking the cart icon or by adding an item to the cart

    17. As a user, I can click the remove from cart button, so that I can easily remove products from my cart

    **Epic 4: Checkout**

    18. As a user, I can click on Proceed to Checkout, so that I can purchase the items in my cart

    19. As a logged in user, on the Checkout page, I can choose to save my delivery address to My StepUp, so that I can retain it for future orders

    20. As a user, i can enter my card details on the checkout page, so that I can make the desired purchase

    21. As a user, I am informed of whether my purchase was successful or not via the Order Successful page, as well as via an email sent upon order confirmation

    **Epic 5: User registration and account**

    22. As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits

    23. As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users

    **Epic 7: Reviews**

    31. As a user, i can read user reviews for products that have received them, so that I easier know if the product is right for me

    **Epic 8: Contact**

    34. As a user, I can get in touch with the site owner, regardless of whether I am signed in or not

    **Epic 10: Terms and Policy**

    40. As a user, I can view a terms document on the sites footer

    41. As a user, I can view a privacy policy document on the sites footer

---

2. **Registered User Case** - User experience for a user that creates an account and performs all available operations for authenticated users. User stories fulfilled in this user case:

    * All of the above plus:

    **Epic 5: User registration and account**

    24. As a user, I have to confirm my email address to complete my account registration

    25. As a logged in user, i can view a My StepUp page, so that I can view my previous orders, and view, update or remove my delivery and contact details

    26. As a logged in user, I can add my delivery details to the My StepUp page, so that it is my default delivery address for my order on the checkout page

    27. As a logged in user, I can choose to delete my account, so that my user account no longer exists

    **Epic 6: The Wish List**

    28. As a logged in user, I can add a product to my Wish List, so that I can easily view it later

    29. As a logged in user, I can remove a product from my Wish List, so that it no longer is there

    30. As a logged in user, I can add products from my Wish List to my cart, so that I can easily purchase them (user story removed for now)

    **Epic 7: Reviews**

    32. As a logged in user, i can write a review and rate a product in the list, so that other users can benefit from this

    33. As a logged in user, I can remove my review of a product, so that it no longer is there

---

3. **Admin User Case** - User experience for an admin user, able to perform all operations on the site. User stories fulfilled in this user case:

    * All of the above plus:

    **Epic 9: Site Owner functionality**

    35. As a site owner, I can view an admin page, where I can view, add, edit and remove any model instance on the site including products, categories, orders etc

    36. As a site owner, I can add, edit or remove any product on the site

    37. As a site owner, I can add, edit or remove any brand on the site

    38. As a site owner, I can remove any products review on the site

    39. As a site owner, I can receive an email from a user that fills in the contact form, so that they can get in touch with me


### Manual Testing - Regular User Case

#### Step 1 - User accesses the landing page

![Home Desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_home.png)

The user is presented with the landing page of the site, which consists of a window-sized (half window on tablet/mobile) carousel, consisting of three hero images giving the user a feel of edecation and quality on first sight. The images link to displaying the products results page, with different filtering (fitness, new and sneakers).

<details>
    <summary>View Images on mobile and tablet</summary>
  
![Home Mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_home.png)

![Home tablet](/workspace/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/tablet_home.png)

</details>

The navbar is visible, as on any page on the site, and this consists of:
    - The products navigation menu, with sorting or filtering possibilities
    - A search bar, displaying results based on product name
    - A Sign In/Sign Up icon
    - Cart

<details>
    <summary>View Images on mobile and tablet</summary>

![Navbar mobile Products nav](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_products_nav.png)

![Home Desktop Products nav](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_prod_nav.png)

![Navbar Sign In Up](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/sign_in_up_menu.png)

![Navbar mobile Sign In](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_account_nav.png)

</details>