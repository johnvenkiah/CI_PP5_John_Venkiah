# Testing

I have thoroughly tested the StepUp web application manually, and partially with automated tests.

I discovered some bugs during the testing phase, which you can read about [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah#bugs)

## Manual testing

### Overview

I have tested the features against their user stories that cover them. Though I am not including images on all screen sizes in this document, responsive design has been implemented and documetation of this with images is already in the [Existing Features](https://github.com/johnvenkiah/CI_PP5_John_Venkiah#existing-features) chapter of my README.md file. I found it repetetive and unnecessary to imclude this several times.

### Testing of user story 1:

*As a user, the intention of the specific page is made clear to me, so that I know the purpose of that page*

This test is difficult to document, as it is covered by all the features and pages. I will give it a shot here though.

**The Home Page**

- **Intention: to entice the user to want to browse products**

The carousel images are well taken photos, the menus are clear and the page is not cluttered.

<details>
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/tablet_home.png)

</details>

- **Conclusion: tests passed**

---

**The Products Page**

- **Intention: display the list of products according to the users query**

The user can filter results by search query, clicking on brand, gender, of items are new or on sale, or sort the products by name, category, price or rating.

<details>
    <summary>View Image</summary>

![Desktop Products Filtered](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_products_filter.png)

</details>

- **Conclusion: tests passed**

---

**The Product Detail Page**

- **Intention: display the relevant information for the product in a tasteful manner and making it easy for the user to add the product to their cart or Wishlist**

The displayed information of the product is the art nr, name, brand, gender, category, description, details, price, whether on discount or not and the product image. This info is generous according to me, giving me enough info to make my decision if the product falls to my liking.

The quantity and size controls are easy to understand, and adding to the cart or Wishlist is done by clicking once on the button in question.

<details>
    <summary>View Image</summary>

![Product Detail on desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_product_detail.png)

</details>

- **Conclusion: tests passed**

---

**The Cart Page**

- **Intention: to show the user an overview of what she or he has intended to buy so the user can adjust the quantity, proceed to checkout or continue browsing**

The user has a clear overview of the cart wherever they are on the site, thanks to the floating grand total and product count at the top right.

Going to the page, the user can clearly see the intention of the page. The count of items is at the top together with the page title. All items are visible as a table, including their image, name, size, art nr and price as well as fields where the user can adjust the quantity and remove the item from the cart. The grand total here is written in large fonts, and the buttons are large too.

The quantity and size controls are easy to understand, and adding to the cart or Wishlist is done by clicking once on the button in question.

<details>
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_cart_several_items.png)

</details>

- **Conclusion: tests passed**

---

**The Checkout Page**

- **Intention: Allow users to enter the needed information for them to purchase the items in their cart**

The Checkout Page is clear and simple, and contains the fields:

- Full Name
- Email Address
- Phone Number
- Street Address 1
- Street Address 2
- Town or City
- County or State
- Postal Code
- Country
- Card Details

As well as the Order summary, including the items added to the cart, their name, size, quantity and price. The Grand total is very visible at the bottom of the page.

Under the card details field, the grand total amount is displayed once more in red.

This to me is very clear, implying that after this step, the order is processed.

<details>
    <summary>View Images</summary>

---

**The Checkout Page, desktop**

![Checkout page on desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_checkout.png)
---

**Pay Button, Checkout on mobile**

![Pay Button, Checkout on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_pay_btn.png)
---

</details>

- **Conclusion: tests passed**


---

**The Contact Page**

- **Intention: Provide a simple form through which the user can contact the site owner**

This is one of the sites most simple pages, as the intention is so obvious to the user. The user should enter their name, email address, a subject and the message itself. On submission, a toast dialog window notifies the user that the message has been sent to the site owner and that they will reply shortly.

<details>
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_contact_form.png)

</details>

- **Conclusion: tests passed**


---

**The Sign Up/Sign In/Sign Out Pages**

- **Intention: Allow users to sign up, in or out**

I have designed these pages as dialog windows, so the users choices are even clearer. Also, upon signup, the links to the sites terms and policies can be viewed through links in the dialog window too.

<details>
    <summary>View Images</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_signup.png)

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_signin.png)

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_sign_out.png)

</details>

- **Conclusion: tests passed**


---

**The My StepUp Page**

- **Intention: To give the user a way to personalize their experience on the site, as well as a reason to return**

As the My StepUp page includes info that the user themselves have chosen, the feeling of a personal experience in my opinion is evident. This together with the purchases that have already been processed makes the page complete.

This to me is very clear, implying that after this step, the order is processed.
<details>
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_my_stepup.png)

</details>

- **Conclusion: tests passed**


---

**The Add Brand or Product Page**

- **Intention: Allow admin users to add a new brand or product to the site**

This page is also rather clear if you ask me, with two forms on the page, each with its own heading. The fields speak for themselves, the image file is displayed if a file is chosen and, with the click of a button at the bottom, the new product or brand is visible just like all the other ones in the Products or Manage Brands pages.

<details>
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/desktop_add_brand_product.png)

</details>

- **Conclusion: tests passed**


---

**The Edit Product Page**

- **Intention: Allow admin users to edit a product on the site**

The Edit Product page, just like the Add Brand or Product page, has a form in which the fields are clear to the user. The user can see the current product details, edit them and is prevented from entering false information, for example a false url, an initial price that is lower that the current one, or omit important details, like the description, details or name.

<details>
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/edit_product_desktop.png)

</details>

- **Conclusion: tests passed**


---

**The Manage Brands Page**

- **Intention: To make managing the brands of the products on the site easy**

The brands are nicely displayed as a grid, with their names, images, and a dedicated edit or delete button just like in the products list when viewed by an admin user.

Upon clicking on edit, the brand form appears, with easy to understand fields, allowing the user to update a brand in seconds.

<details>
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/manage_brands.png)

</details>

- **Conclusion: tests passed**

---

- **Conclusion, User story 1 - Tests passed**

---

### Testing of user story 2:

*As a user, I can access important links such as home, products, my cart, sign in/out, and My StepUp by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site*

The navbar is present throughout the site, with the exceptions of when a modal or dialog window is present. I have chosen to include the navbar in the authentication pages (sign up/in/out, change password etc) if the user should wish to access them.


<details>
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/mobile_accessing_nav_sign_out.png)

</details>

- **Conclusion, User story 2 - : tests passed**


---

### Testing of user story 3 and 4:

*As a user, I can see a form to register for newsletters repeatedly throughout the website, so that I can receive news on products and campaigns*

*As a user, I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook*

Like the navbar, the footer, which includes the mailchimp newsletter registration form and the Facebook pages link, is almost always visible on each page. Exceptions are the authetication pages and when a dialog window appears, such as when removing an item from the wishlist or viewing the privacy policy.


<details>
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/tablet_footer.png)

</details>

- **Conclusion, User story 3 - 4: tests passed**

--

### Testing of user story 5:

*As a user, it is visible if I am signed in or not, so that I am made aware of this*

As mentioned earlier, the navbar is visible almost everywhere on the site - and in the navbar, the user can see their authentication status. On desktop, the menu item says Sign In/Sign Up for non-authenticated users, and Account for authenticated ones.

On mobile, the text isn't visible in the navbar, but clicking on it once will show that the user is either not logged in, logged in or logged in as an admin, displaying the admin account menu items, Add Brand or Product and Manage Brands.

On top of this, the user is reminded of this in the Product Detail and Checkout pages, with links to sign in to use the Wishlist or save order details.

<details>
    <summary>View Image</summary>

**Navbar for non-authenticated users**

![Navbar for non-authenticated users](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_prod_nav.png)
---

**Navbar for authenticated users**

![Navbar for non-authenticated users](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_nav_logged_in.png)
---

**Navbar for admin users**

![Navbar for admin users](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/tablet_auth_nav.png)
---

**Navbar for admin users**

![Navbar for admin users](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/tablet_auth_nav.png)
---

**Links in place of functions for non-signed in users**

![Links to sign in if not signed in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_sign_in_links.png)
---

</details>

- **Conclusion, User story 5 - tests passed**

--

### Testing of user story 6:

*As a user, the choices I make on the site are confirmed to me, so that I am always aware of them*

A smart solution for giving users confirmation on when they have made a choice is the Toasts dialog function. Created with the help of Bootstrap and Django, the toast message is displayed to the user if the function they performed is successful. This includes everything from creating an account, signin in or out, adding or removing items from the wishlist or cart, updating the carts item quantity, and making a successful order, in excess of the order confirmation page of course.

The toast will also display items in the cart, if there are any.

For extra clarity, the border colours are coded for each type of message - blue for info, yellow for warnings, red for errors and green for success.

Also, if a user enters wrong or sufficient info, a message is given to the user if a choice cannot be made.

<details>
    <summary>View Images</summary>

**Confirmation of sign in**

![Conirmation of sign in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/toast_signed_in.png)
---

**Adding product to Wishlist**

![Adding product to Wishlist](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_add_to_wl.png)
---

**Choosing a too similar password**

![Choosing a too similar password](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/signup_val_2.png)
---

**Access denied message**

![Access denied message](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/mobile_access_denied.png)
---

</details>

- **Conclusion, User story 6 - tests passed**

--

### Testing of user story 7:

*As a user, I can browse a list of products for sale on the site so that I can find the product I seek*

The product list is accessible through the products navigation menu, via Products or the hamburger menu in the navbar. Here, users can choose to view all products, or filter them to their liking.

The products list is also accessible via the Browse Products button on the home page, or similiar buttons here and there throughout the site, urging the user to browse more.

<details>
    <summary>View Images</summary>

**Desktop view of the products list**

![Desktop view of the products list](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_products.png)
---

**Mobile view of the products list**

![Mobile view of the products list](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_clicked_womens.png)
---

**Tablet view of the products list for admin users**

![Tablet view of the products list for admin users](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/tablet_auth_products.png)
---

**Browse products button on Home page**

![Browse products button on Home page](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_home.png)
---

</details>

- **Conclusion, User story 7 - tests passed**

--

### Testing of user story 8:

*As a user, i can perform a search, so that products matching the search appear in the products list*

There is a search field in the navbar, in which users can search for products. performing a search on Nike for example will display the products list filtering to show products with Nike in the product name.

<details>
    <summary>View Image</summary>

**Search of sneakers performed**

![Search of sneakers performed](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_searched_sneakers.png)
---

</details>

- **Conclusion, User story 8 - tests passed**


--

### Testing of user story 9:

*As a user, I can sort the products list by category, alphabetically or by rating, so that i can quickly find the product I seek*

The products page always displays a dropdown bar to sort products, by price (low to high), price (high to low),rating(high to low), rating(low to high), name (a-z), name (z-a), category (a-z) or category (z-a).

This works as intended.

<details>
    <summary>View Image</summary>

**Search of sneakers performed**

![Search of sneakers performed](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_price_desc.png)
---

</details>

- **Conclusion, User story 9 - tests passed**


--

### Testing of user story 10:

*As a user, I can view the most important details of the product in the product list, such as model, brand, category, price, rating, and image so that i know most details without having to click on the product*

The products are displayed as cards, each with:

- Heading at the top
- Product image with badges saying if the product is on sale or new
- Price with intial price crossed out if on sale
- Rating
- Gender and category
- Edit and delete buttons if user is admin user

<details>
    <summary>View Image</summary>

**Product info in Products page for admin user**

![Product info for admin](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/desktop_closeup_two_products_admin.png)
---

</details>

- **Conclusion, User story 10 - tests passed**

