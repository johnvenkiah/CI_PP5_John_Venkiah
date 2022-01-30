# Performance

## Table of Contents

- [Performance](#performance)
  * [Overview](#overview)
  * [Home](#home)
  * [Products](#products)
  * [Product Detail](#product-detail)
  * [Cart](#cart)
  * [Checkout](#checkout)
  * [Order Confirmation/History](#order-confirmation-history)
  * [Contact](#contact)
  * [![Test results of lighthouse, Contact, desktop]
  * [My StepUp](#my-stepup)
  * [Add Product or Brand](#add-product-or-brand)
  * [Manage Brands](#manage-brands)
  * [Edit Product](#edit-product)
  * [Sign Up](#sign-up)
  * [Sign In](#sign-in)
  * [Sign Out](#sign-out)
  * [Change Password](#change-password)
  * [Reset Password](#reset-password)
  * [Reset Password Link Sent](#reset-password-link-sent)
  * [Reset Password Set](#reset-password-set)
  * [Reset Password Done](#reset-password-done)
  * [Delete Account](#delete-account)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Overview

Performance was tested using the DevTools Lighhouse feature in the Chrome web browser. Performance was overall good on desktop and not too great on mobile. This was, according to the tests due to two things mainly:

- The usage of PNG and JPEG files, newer and lighter formats were suggested by Lighhouse that I had not heard of earlier and I will do more research on web image file types for future projects.

- The second thing was the loading of static files, Javascript and CSS, before the rest of the page has loaded. This is something that I normally would add to the bottom of a page, but two factors played in here, making me stick with the way things are at the moment:

* Bootstrap and JQuery need to be loaded after one another in the right order
* The HTML and Django template structure makes it more difficult to have an overview of which files are loaded first, and, I decided not to move things around this time around.


**Here are the test results**

## Home

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Home, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_home_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Home mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_home_mob.png)
---
</details>


## Products

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Products, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_products_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Products, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_products_mob.png)
---
</details>


## Product Detail

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Product Detail, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_product_detail_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Product Detail, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_product_detail_mob.png)
---
</details>


## Cart

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Cart, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_cart_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Cart, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_cart_mob.png)
---
</details>


## Checkout

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Checkout, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_checkout_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Checkout, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_checkout_mob.png)
---
</details>


## Order Confirmation/History

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Order Confirmation, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_order_conf_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Order Confirmation, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_order_conf_mob.png)
---
</details>


## Contact

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Contact, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_contact_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Contact, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_contact_mob.png)
---
</details>


## My StepUp

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, My StepUp, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_my_stepup_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, My StepUp, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_my_stepup_mob.png)
---
</details>


## Add Product or Brand

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Add Product or Brand, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_add_pro_br_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Add Product or Brand, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_add_pro_br_mb.png)
---
</details>


## Manage Brands

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Manage Brands, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_manage_brands_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Manage Brands, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_manage_brands_mob.png)
---
</details>


## Edit Product

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Edit Product, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_edit_product_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Edit Product, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_edit_product_mob.png)
---
</details>


## Sign Up

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Sign Up, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_signup_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Sign Up, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_signup_mob.png)
---
</details>


## Sign In

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Sign In, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_signin_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Sign In, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_signin_mob.png)
---
</details>


## Sign Out

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Sign Out, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_signout_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Sign Out, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_signout_mob.png)
---
</details>


## Change Password

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Change Password, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_change_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Change Password, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_change_mb.png)
---
</details>


## Reset Password

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Reset Password, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_reset_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Reset Password, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_reset_mob.png)
---
</details>


## Reset Password Link Sent

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Reset Password Link Sent, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_reset_link_sent_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Reset Password Link Sent, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_reset_link_sent_mob.png)
---
</details>


## Reset Password Set

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Reset Password Set, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_reset_change_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Reset Password Set, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_reset_change_mob.png)
---
</details>


## Reset Password Done

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Reset Password Done, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_reset_done_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Reset Password Done, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_password_reset_done_mob.png)
---
</details>


## Delete Account

<details>
    <summary>View test results of desktop page</summary>

---

![Test results of lighthouse, Delete Account, desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_delete_account_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Delete Account, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_delete_account_mb.png)
---
</details>

