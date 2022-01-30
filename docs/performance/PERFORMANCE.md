# Performance

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

![Test results of lighthouse, Home](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_home_dt.png)
---
</details>

<details>
    <summary>View test results of mobile page</summary>

---

![Test results of lighthouse, Home](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/screenshots/lighthouse_home_mb.png)
---
</details>

