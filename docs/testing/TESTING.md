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
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_checkout.png)

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

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_checkout.png)

</details>

- **Conclusion: tests passed**


---

**The Add Brand or Product Page**

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
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_checkout.png)

</details>

- **Conclusion: tests passed**


---

**The Edit Product Page**

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
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_checkout.png)

</details>

- **Conclusion: tests passed**


---

**The Manage Brands Page**

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
    <summary>View Image</summary>

![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_checkout.png)

</details>

- **Conclusion: tests passed**

