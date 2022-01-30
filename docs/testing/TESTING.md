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

---

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_contact_form.png)

</details>

- **Conclusion: tests passed**


---

**The Sign Up/Sign In/Sign Out Pages**

- **Intention: Allow users to sign up, in or out**

I have designed these pages as dialog windows, so the users choices are even clearer. Also, upon signup, the links to the sites terms and policies can be viewed through links in the dialog window too.

<details>
    <summary>View Images</summary>

---

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

---

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_my_stepup.png)

</details>

- **Conclusion: tests passed**


---

**The Add Brand or Product Page**

- **Intention: Allow admin users to add a new brand or product to the site**

This page is also rather clear if you ask me, with two forms on the page, each with its own heading. The fields speak for themselves, the image file is displayed if a file is chosen and, with the click of a button at the bottom, the new product or brand is visible just like all the other ones in the Products or Manage Brands pages.

<details>
    <summary>View Image</summary>

---

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/desktop_add_brand_product.png)

</details>

- **Conclusion: tests passed**


---

**The Edit Product Page**

- **Intention: Allow admin users to edit a product on the site**

The Edit Product page, just like the Add Brand or Product page, has a form in which the fields are clear to the user. The user can see the current product details, edit them and is prevented from entering false information, for example a false url, an initial price that is lower that the current one, or omit important details, like the description, details or name.

<details>
    <summary>View Image</summary>

---

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

---

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

---

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

---

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/tablet_footer.png)

</details>

- **Conclusion, User story 3 and 4 - tests passed**

---

### Testing of user story 5:

*As a user, it is visible if I am signed in or not, so that I am made aware of this*

As mentioned earlier, the navbar is visible almost everywhere on the site - and in the navbar, the user can see their authentication status. On desktop, the menu item says Sign In/Sign Up for non-authenticated users, and Account for authenticated ones.

On mobile, the text isn't visible in the navbar, but clicking on it once will show that the user is either not logged in, logged in or logged in as an admin, displaying the admin account menu items, Add Brand or Product and Manage Brands.

On top of this, the user is reminded of this in the Product Detail and Checkout pages, with links to sign in to use the Wishlist or save order details.

<details>
    <summary>View Image</summary>

---

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

---

### Testing of user story 6:

*As a user, the choices I make on the site are confirmed to me, so that I am always aware of them*

A smart solution for giving users confirmation on when they have made a choice is the Toasts dialog function. Created with the help of Bootstrap and Django, the toast message is displayed to the user if the function they performed is successful. This includes everything from creating an account, signin in or out, adding or removing items from the wishlist or cart, updating the carts item quantity, and making a successful order, in excess of the order confirmation page of course.

The toast will also display items in the cart, if there are any.

For extra clarity, the border colours are coded for each type of message - blue for info, yellow for warnings, red for errors and green for success.

Also, if a user enters wrong or sufficient info, a message is given to the user if a choice cannot be made.

<details>
    <summary>View Images</summary>

---

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

---

### Testing of user story 7:

*As a user, I can browse a list of products for sale on the site so that I can find the product I seek*

The product list is accessible through the products navigation menu, via Products or the hamburger menu in the navbar. Here, users can choose to view all products, or filter them to their liking.

The products list is also accessible via the Browse Products button on the home page, or similiar buttons here and there throughout the site, urging the user to browse more.

<details>
    <summary>View Images</summary>

---

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

---

### Testing of user story 8:

*As a user, i can perform a search, so that products matching the search appear in the products list*

There is a search field in the navbar, in which users can search for products. performing a search on Nike for example will display the products list filtering to show products with Nike in the product name.

<details>
    <summary>View Image</summary>

---

**Search of sneakers performed**

![Search of sneakers performed](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_searched_sneakers.png)
---

</details>

- **Conclusion, User story 8 - tests passed**


---

### Testing of user story 9:

*As a user, I can sort the products list by category, alphabetically or by rating, so that i can quickly find the product I seek*

The products page always displays a dropdown bar to sort products, by price (low to high), price (high to low),rating(high to low), rating(low to high), name (a-z), name (z-a), category (a-z) or category (z-a).

This works as intended.

<details>
    <summary>View Image</summary>

---

**Search of sneakers performed**

![Search of sneakers performed](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_price_desc.png)
---

</details>

- **Conclusion, User story 9 - tests passed**


---

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

---

**Product info in Products page for admin user**

![Product info for admin](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/desktop_closeup_two_products_admin.png)
---

</details>

- **Conclusion, User story 10 - tests passed**


---

### Testing of user story 11:

*As a user, i can click the product in the products list so that I can view the products details*

**Steps:**

- User is on Products page and clicks a single product
- User is taken to the detail page of the product clicked on

<details>
    <summary>View GIF</summary>

---

**Clicking on product in list**

![Clicking on product in list](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/gif_clicking_on_product.gif)
---

</details>

- **Conclusion, User story 11 - tests passed**


---

### Testing of user story 12:

*As a user, I can choose the size of the product, as well as the quantity, so that I can purchase the correct size/quantity*

**Steps:**

- User clicks on the plus or minus signs to choose quantity
- User chooses the size of the product in the dropdown size input
- User clicks on the Add to Cart button
- Item is added to the cart with the chosen quantity and size

<details>
    <summary>View GIF</summary>

---

**Clicking on product in list**

![Clicking on product in list](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/gif_choosing_prod_size_qty.gif)
---

</details>

- **Conclusion, User story 12 - tests passed**


---

### Testing of user story 13:

*As a user, I can add a product to my cart by clicking ’Add to Cart’ from the product detail page so that I can purchase the product*

This user story is already tested and displayed in [Testing of user story 12](#testing-of-user-story-12), and passed too.

- **Conclusion, User story 13 - tests passed**


---

### Testing of user story 14:

*As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be*

The cart total (and count) is visible as a floating badge/button at the top right corner when the user scrolls up, and dissapears again when scrolling down as not to distract the user. This is true on all pages where the navbar is displayed, which is virtually all pages, except for when dialog modal windows appear.
<details>
    <summary>View Image</summary>

---

**Cart total badge**

![Cart total badge](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/cart_badge_filled.png)
---

</details>

- **Conclusion, User story 14 - tests passed**


---

### Testing of user story 15 and 16:

*As a user, i can adjust the quantity of the product chosen after adding it to the shopping cart*

*As a user, I can view the products added to my cart by clicking the cart icon or by adding an item to the cart*

Passed testing of this user story is displayed in user story 13, where adding the item caused the toast to appear. I have included a GIF file below displaying the actions.

**Actions:**

- Clicking on the Cart icon in the navbar
- Being shown the Cart page
- Changing the quantity of the product and clicking Update
- The cart items and quantity are displayed both in the toast message at the top and on the Cart page

<details>
    <summary>View Image</summary>

---

**Clicking the Cart icon and updatinge the quantity**

![Clicking the Cart icon and updatinge the quantity](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/gif_clicking_on_and_updating_cart.gif)
---

</details>

- **Conclusion, User story 15 and 16 - tests passed**


---

### Testing of user story 17:

*As a user, I can click the remove from cart button, so that I can easily remove products from my cart*

**Actions**

- User clicks on the red X button in the relevant products field
- Toast is displayed telling the user the item is remove and displaying the updated cart and
- The Cart page is reloaded, updated with the changes made (removal)

<details>
    <summary>View GIF</summary>

---

**Removing item from Cart**

![Removing item from Cart](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/gif_remove_from_cart.gif)
---

</details>

- **Conclusion, User story 17 - tests passed**


---

### Testing of user story 18:

*As a user, I can click on Proceed to Checkout, so that I can purchase the items in my cart*

**Actions**

- User clicks on the Checkout button at the bottom of the Cart page
- User is taken to the Checkout page

<details>
    <summary>View GIF</summary>

---

**Clicking on the Checkout button**

![Clicking on the Checkout button](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/gif_clicking_on_checkout.gif)
---

</details>

- **Conclusion, User story 18 - tests passed**


---

### Testing of user story 19:

*As a logged in user, on the Checkout page, I can choose to save my delivery address to My StepUp, so that I can retain it for future orders*

**Actions**

- Authenticated user clicks on the checkbox to save details to their profile
- User proceeds with the order and it is processed
- The details the user entered are now saved on the My StepUp page

<details>
    <summary>View Images</summary>

---

**Details filled in on checkout**

![Details filled in on checkout](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/details_checkout.gif)
---

**Details in My StepUp after checkout**

![Details in My StepUp after checkout](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/details_my_stepup_after_checkout.gif)
---

</details>

- **Conclusion, User story 19 - tests passed**


---


### Testing of user story 20:

*As a user, i can enter my card details on the checkout page, so that I can make the desired purchase*

**Actions**

- User enters the card details (test card for stripe tested, details 4242 4242 4242 4242, cvc and postal code can be anything)
- User proceeds with the order and it is processed
- The order is completed

<details>
    <summary>View Images</summary>

---

**Card details are filled in**

![Details filled in on checkout](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_pay_btn.png)
---

**Payment processing screen after clicking Complete Order**

![Details in My StepUp after checkout](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_payment_processing.png)
---

</details>

- **Conclusion, User story 20 - tests passed**


---


### Testing of user story 21:

*As a user, I am informed of whether my purchase was successful or not via the Order Successful page, as well as via an email sent upon order confirmation*

**Actions**

- User has entered their card information and clicked on Complete Order and the processing screen appears
- Either the order is completed and user is cofirmed of this, in which case an email is sent to the user.
- If this email is invalid, a message is sent to the site owner informing them of this

<details>
    <summary>View Images</summary>

---

**Error message if invalid details**

![Error message if invalid details](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/error_message_card_details_invalid.png)
---

**Order Confirmation**

![Order Confirmation](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_order_confirmation.png)
---

**Email sent to user (different order)**

![Email sent to user](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/order_confirmation_email_received.png)
---

</details>

- **Conclusion, User story 21 - tests passed**


---

### Testing of user story 22 and 24:

*As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits*

*As a user, I have to confirm my email address to complete my account registration*

**Actions**

- User clicks on Sign Up in the nav or through any of the sign up links on the site
- User is brought to the Sign Up page, where they are promted to enter their email and choose a username and password (password to be entered twice)
- If the username and email address is unique for the site, the user is greeted with the email confirm page, letting the user know that an email has been sent to them with a confirmation link.
- The user clicks the link and cofirms their email address, and 

<details>
    <summary>View Images</summary>

---

**The Sign Up page on Tablet**

![The Sign Up page on Tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_signup.png)
---

**Page letting user know that an email has been sent**

![Page letting user know that an email has been sent](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_verification_sent.png)
---

**Email is received by user**

![Page letting user know that an email has been sent](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/signup_email_received.png)
---

**User clicks confirmation link in email and is brought to the confirm email page**

![User clicks confirmation link in email and is brought to the confirm email page](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_confirm_email.png)
---

**User is notified that the email is confirmed and can now sign in**

![User is notified that the email is confirmed and can now sign in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_signin_after_email_confirm.png)
---

**Sign in is successful**

![Sign in is successful](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/signin_successful.png)
---

</details>

- **Conclusion, User story 22 and 24 - tests passed**


---


### Testing of user story 23:

*As a user, I am not able to access pages that require authentication if I am not signed in*

As links to these pages are not present if the user is not signed in, users cannot access these pages through any link on the page without signing in. If however a non authenticated user tries to enter any of the urls to the pages that are restricted to authenticated users, the user is brought to the signin page instead.

**Actions**

- User enters the url of a page restricted to authenticated users
- User is brought to the sign in page instead

<details>
    <summary>View Images</summary>

---

**User enters a url that requires sign in**

![User enters a url that requires sign in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/entering_url.png)
---

**User brought to the Sign In page and is taken to My StepUp after signing in**

![Order Confirmation](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_sign_in_page_next_my_stepup.png)
---

</details>

- **Conclusion, User story 23 - tests passed**


---

### Testing of user story 25 and 26:

*As a logged in user, i can view a My StepUp page, so that I can view my previous orders, and view and update my delivery and contact details*

*As a logged in user, I can add my delivery details to the My StepUp page, so that it is my default delivery address for my order on the checkout page*

**Actions**

- User needs to be registered and signed in.
- User clicks on the Account nav menu item
- User is brought to the My Stepup page where she or he can update their details
- The details are now visible on the Checkout page

<details>
    <summary>View Images</summary>

---

**Checkout page only displays email from registering the account**

![Checkout page only displays email from registering the account](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_checkout_details_not_saved.png)
---

**User enters the My StepUp page and clicks on update information**

![User enters the My StepUp page and clicks on update information](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_my_stepup_details_saved.png)
---

**Checkout page now has this data prefilled**

![Checkout page now has this data prefilled](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_checkout_saved_details.png)
---

</details>

- **Conclusion, User story 25 and 26 - tests passed**


---

### Testing of user story 27:

*As a logged in user, I can choose to delete my account, so that it no longer exists*

The delete account link is at the bottom of the My StepUp page. Usually, the link to remove an account is well hidden on pages like these, to keep members active. This leads to too many unwanted memberships. Instead, I put a clear "Danger Area" in the My StepUp page, where users are notified that the action is irriversible.

**Actions**

- User clicks on the Delete Account button
- User is presented with a dialog modal window, where she or he has to confirm deletion by ticking a checkbox
- If the checkbox is checked, clicking the Delete Account button signs the user out, takes them to the home page and notifies them that their account has been deleted.

<details>
    <summary>View Images</summary>

---

**Account Operations/Danger Area on My StepUp page**

![Danger Area on My StepUp page](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/mobile_account_operations.png)
---

**Delete Account modal window (showing validation if user does not check box**

![Delete Account modal window](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/delete_account_validation.png)
---

**Account Successfully deleted**

![Account Successfully deleted](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/account_successfully_deleted.png)
---

</details>

- **Conclusion, User story 27 - tests passed**


---

### Testing of user story 28:

*As a logged in user, I can add a product to my Wish List, so that I can easily view it later*

**Actions**

- User clicks on the Add to Wishlist button on the product detail page
- User is notified that the product is added to their Wishlist
- User can view the itme in their Wishlist

<details>
    <summary>View GIF</summary>

---

**User adding item to their Wishlist**

![User adding item to their Wishlist](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/gif_add_to_wishlist.gif)
---

</details>

- **Conclusion, User story 28 - tests passed**


---

### Testing of user story 29:

*As a logged in user, I can add a product to my Wish List, so that I can easily view it later*

**Actions**

- User clicks on the Add to Wishlist button on the product detail page
- User is notified that the product is added to their Wishlist
- User can view the itme in their Wishlist

<details>
    <summary>View GIF</summary>

---

**Removing from Wishlist on Product Detail page**

![Removing from Wishlist on Product Detail page](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/gif_remove_wl_pr_detail.gif)
---

**Removing from Wishlist on My StepUp page**

![Removing from Wishlist on My StepUp page](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/gif_remove_wl_my_stepup.gif)
---

</details>

- **Conclusion, User story 29 - tests passed**


---

**User story 30 was removed so testing of that has not been performed**


### Testing of user story 31:

*As a user, i can read user reviews for products that have received them, so that I easier know if the product is right for me*

**Actions**

- User navigates to the product detail page of the product in question
- If there are reviews for that product, they will be visible at the bottom of the page

<details>
    <summary>View Image</summary>

---

**Reviews visible at the bottom of the Product Detail page**

![Reviews visible at the bottom of the Product Detail page](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_reviews.png)
---

</details>

- **Conclusion, User story 31 - tests passed**


---

### Testing of user story 32:

*As a logged in user, i can write a review and rate a product in the list, so that other users can benefit from this*

**Actions**

- Authenticated user fills in the Review This Product form at the bottom of the Product Detail page
- Review is posted and product rating takes effect of this

<details>
    <summary>View GIF and Image</summary>

---

**Posting a user review (initial rating is 5)**

![Posting a user review](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/gif_post_review.gif)
---

**Review is visible in the Product Reviews area**

![Review is visible](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/review_box_after_posting_review.png)
---

</details>

- **Conclusion, User story 32 - tests passed**


---

### Testing of user story 33:

*As a logged in user, I can remove my review of a product, so that it no longer is there*

**Actions**

- User clicks on the Delete button, on their review in the review box, on the Product Detail page
- User is promted to cofirm this with a modal dialog window
- Users review is removed from the product and user is notified of this with a toast

<details>
    <summary>View GIF and Image</summary>

---

**Posting a user review (initial rating is 5)**

![Posting a user review](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/gif_remove_review.gif)
---

</details>

- **Conclusion, User story 33 - tests passed**


---

### Testing of user story 34:

*As a user, I can get in touch with the site owner, regardless of whether I am signed in or not*

**Actions**

- User clicks on the Contact link in the page footer on any page (except for account operations or when a dialog modal is present)
- User fills in the contact form
- User is notified that the form is sent if all fields are filled in and the email address is valid
- Site owner recieves an email with the message sent

<details>
    <summary>View Images</summary>

---

**Contact form is filled in**

![Contact form is filled in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/contact_form_filled.png)
---

**Notification that message is sent**

![Contact form is filled in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/toast_contact_form_sent.png)
---

**Site owner recieves an email**

![Site owner recieves an email](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_email_from_user_recieved.png)
---

</details>

- **Conclusion, User story 34 - tests passed**


---

### Testing of user story 35:

*As a site owner, I can view an admin page, where I can perform batch editing of model instances on the site including products, categories, orders and brands*

The models available in the Django Admin panel are:

- Product
- Brand
- Category
- Review
- Order
- Order Line Items (at the bottom of each order)

Admin users can log in to the admin panel by signing in at https://stepup-shoes.herokuapp.com/admin. Here they have read write and remove access to these instances.

For example, an admin user can change the products in an order that has already been processed, which they cannot do on the regular site. They can also remove multiple items at once, which is also an operation limited to this admin panel.

**Performed tests**

- Updating a processed order, user details and order line items
- Removing multiple Brand instances
- Adding a category
- Updating a product with the new category
- Removing a brand image

<details>
    <summary>View Images</summary>

---

**Admin panel**

![Admin Panel](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_home.png)
---

**Deleting several brands**

![Deleting several brands](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/admin_deleting_several_brands.png)
---

**Confirmation on brand deletion**

![Site owner recieves an email](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_deletion_brand_confirmation.png)
---

**Adding new category**

![Adding new category](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_add_category.png)
---

**Updating product name, brand and category**

![Updating product name and category](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_product_new_name_brand_category.png)
---

**Users order in admin**

![Users order in admin](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_order_before_edit.png)
---

**Users order details after editing**

![Users order details after editing](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_order_after_edit_1.png)
---

**Order line items after editing**

![Order line items after editing](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_order_after_edit_2.png)
---

</details>

- **Conclusion, User story 35 - tests passed**


---

### Testing of user story 36:

*As a site owner, I can add, edit or remove any product on the site*

**Performed tests**

- Adding a new product to the site

    - Admin user navigates to the Add Brand or Product menu item in the Account nav menu
    - User fills in the Add Product form
    - If the form is valid, user is taken to the new products Product Detail page

- Editing a product

    - Admin clicks the Edit button, either on the product cart in the Products page or at the top of the Product detail page
    - User is presented with the products current details in the product form and can edit it
    - User clicks on Update Product
    - If the form is valid, user is taken to the newly edited products Product Detail page

- Removing a product

    - Admin clicks the Delete button, either on the product cart in the Products page or at the top of the Product detail page
    - User has to confirm this in a modal dialog window
    - User clicks Delete Product and is notified via a toast that the product is removed

<details>
    <summary>View Add Product Images</summary>

---

**The Add Brand or Product Nav menu link**

![The Add Brand or Product Nav menu link](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/add_brand_product_nav_menu.png)
---

**The Add Brand or Product Nav Page**

![The Add Brand or Product Nav Page](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_add_brand_product.png)
---

**Fields in the Add Product form must be correctly filled**

![Fields in the Add Product form must be correctly filled](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/product_form_validation.png)
---

**Entering a lower intital price than the current one triggers an error modal**

![Lower price error modal](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/update_product_invalid_price.png)
---

**User can check box if product is new**

![User can check box if product is new](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/checkbox_new_product.png)
---

**User is taken to Product detail page of the new product which can be viewed in the products list**

![Users order in admin](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/tablet_add_product_new_added.png)
---

</details>

<details>
    <summary>View Edit Product Images</summary>

---

**The Product Edit button on the product card, Products page**

![The Product Edit button](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/product_edit_btn.png)
---

**The Edit Product page**

![The Edit Product page](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/edit_product_desktop.png)
---

**Setting the sale price**

![Fields in the Add Product form must be correctly filled](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/edit_product_setting_sale_price.png)
---

**Adding a new image to the product**

![Lower price error modal](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/edit_product_set_new_image.png)
---

**Updated product has a Save €! badge with correct amount saved and the new image**

![User can check box if product is new](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/edited_product_with_sale_badge_new_img.png)
---

</details>

<details>
    <summary>View Delete Product Image</summary>

---

**The user has clicked on the Delete button and gets this dialog window**

![The Add Brand or Product Nav menu link](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/delete_product_modal.png)
---
---

**Upon confirmation the product is deleted**

![The Add Brand or Product Nav menu link](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/product_deleted.png)
---

</details>


- **Conclusion, User story 36 - tests passed**


---


### Testing of user story 37:

*As a site owner, I can add, edit or remove any brand on the site*

**Performed tests**

- Adding a new brand to the site

    - Admin user navigates to the Add Brand or Product menu item in the Account nav menu
    - User fills in the Add Brand form
    - If the form is valid, user is taken to the Manage Brands page where the new brand is displayed among the others

- Editing a brand

    - Admin navigates to the Manage Brands page and click on the Edit button on the brand in question
    - User is presented with a modal window containing the brand form and the brands current details
    - User fills in the form and clicks on Update Brand
    - If the form is valid, Manage Brands page is updated with the brands new details

- Removing a brand

    - Admin clicks the Delete button on the brand in question on the Manage Brands page
    - User has to confirm this in a modal dialog window
    - User clicks Delete Product and is notified via a toast that the brand is deleted

<details>
    <summary>View Add Brand Images</summary>

---

**The simple Add New Brand form on the Add Product or Brand page**

![The add brand form](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/add_new_brand_form.png)
---

**Clicking on Select Image opens a window where users can upload an image**

![Select image](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/select_image_edit_add_brand_or_product.png)
---

**Clicking on Add Brand reloads the Manage Brands page, notifies the user and the brand is visible in the grid of brands (2 images)**

![New brand added](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/new_brand_added.png)
---

</details>

<details>
    <summary>View Edit Brand Images</summary>

---

**The brand Edit button on the brand card, Manage Brands page**

![The brand Edit button](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/edit_brand_btn.png)
---

**The Edit Brand modal window**

![The Edit Brand modal](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/edit_brand_form.png)
---

**The brand is updated and edit is reflected in the brand icon, Manage Brands page (2 images)**

![Brand is updated](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/brand_updated.png)
---

</details>

<details>
    <summary>View Delete Brand Images</summary>

---

**The Delete brand button, Manage Brands**

![The Delete brand button](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/brand_delete_btn.png)
---

**The Delete brand dialog modal window**

![The Delete brand modal](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/brand_delete_modal.png)
---

**Upon confirmation the brand is deleted**

![Brand is deleted](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/brand_deleted.png)
---

</details>


- **Conclusion, User story 37 - tests passed**


---


### Testing of user story 38:

*As a site owner, I can remove any products review on the site*

**Actions**

- Admin user navigates to the product detail page where the review in question is
- In the review box, a delete button is visible for each review for the product
- Admin user click the Delete Review button under the review in question
- After confirmation the review is deleted

<details>
    <summary>View Images</summary>

---

**For admins, the review box has a delete button for each review, independant of who posted it**

![Contact form is filled in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_review_box.png)
---

</details>

- **Conclusion, User story 38 - tests passed**


---

### Testing of user story 39:

*As a site owner, I can receive an email from a user that fills in the contact form, so that they can get in touch with me*

This user story is already covered at [Testing of user story 34](#testing-of-user-story-34) and passed

- **Conclusion, User story 39 - tests passed**


### Testing of user story 40 and 41:

*As a user, I can view a terms document via a link in the sites footer*

*As a user, I can view a privacy policy document via a link in the sites footer*

The footer as mentioned is almost always visible at the bottom of the page and contains links to both of these, so I put them here together. All the user has to do is click the link and a modal with either of these appears for the user to view.

<details>
    <summary>View Images</summary>

---

**The policy and terms links in the footer**

![Contact form is filled in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/policies_links_in_footer.png)
---

**The terms of use**

![Contact form is filled in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/terms_of_use.png)
---

**The privacy policy**

![Contact form is filled in](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/privacy_policy.png)
---

</details>

- **Conclusion, User story 40 and 41 - tests passed**


---


## Automated Testing


Some tests were performed (37), mostly for me to learn the practice of automated testing. Credits to pmeeny and his project [Love Rugby](https://github.com/pmeeny/CI-MS4-LoveRugby) for the main part of these.

Here are the results:

![Automated Testing part 1]()