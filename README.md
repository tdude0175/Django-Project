# Monthly project 2: A Django Wiki web application

Create an a Wikipedia Light web application to support multiple Wiki Post Authors.

### Design Requirements:
* You MUST produce a written design *prior* to starting to code your solution. This design doesn't have to be a book, but should at least note needed endpoints and basic sketches on how you plan to use CSS Grid for your various screens.
* You MUST demonstrate that you have stood up all your endpoints, routes, views, and templates with stubbed out dummy data *prior* to adding specific logic.

## Functional Requirements (Total of 20 points)

### Aesthetics (10 pts)
Use HTML, CSS, templating, and any CSS resources neccessary to make your site aesthetically pleasing. NOTE: Primary layout should rely on CSS grid!

#### Consistency (3 pts)
- 3pts: Background, text format, and color usage are carefully chosen to produce a consistent screen layout for all your pages.
- 2pts: Background, text format, and color usage are somewhat consistent with little inappropriate variation.
- 1pt: Background, text format, and color usage are randomly chosen with few consistent elements throughout

#### Navigational/Structural Format (4 pts)
- 4pts: Content is presented in a clear manner that is easy to follow. Readers can get around your website with ease. There are no blind links, and a navigation bar is provided per requirements below.
- 3pts: Content is presented in a clear manner that is easy to follow. Navigation is difficult. Not intuitive.
- 2pts: Content is somewhat confusing and difficult to follow. Site is somewhat difficult to navigate. Too much textual information.
- 1pt: Content is confusing and difficult to follow. Site is difficult to navigate. Not intuitive. Large images that take long to load.

#### Simplicity and Color Scheme (3 pts)
- 3pts: Content is simple and to the point. Design is easy to understand in many ways color is appropriately used to produce an atmosphere that expresses the character of the Web site. 
- 2pts: Web page is somewhat busy. People reading it will have difficulty finding what they want quickly. Excessive use of graphic elements. Color is used somewhat appropriately to produce an atmosphere that expresses the character of the Web site.
- 1pt: Web page is too busy. People reading it cannot find what they want quickly. Excessive use of graphic elements

### Functionality (10 pts)

#### Base Requirements (5 pts):

* The layout should be similar to the example images provided.

* The project should use CSS Grid for the main layout. Other elments may be mixed in as you see fit. 

* The User should be able to do a keyword search that will return a list of Wiki entries where the entered keywords are found in the entry's title and/or text.

* All pages should provide a Navagation Bar that allows a user to go 'Home', 'Add a New Entry', or 'Your Entries'. 'Add a new Entry' and list 'Your Entries' should only be available if the User is signed in. The main 'index' page should list all current Wiki entries from all Authors along with their main image (if present)

* All Users should be able to click the Title of an individual entry to see the full post. If the post has an image, it should display. Any 'Related Information' items for the post should be displayed in a sidebar at the right of the page. If a displayed entry is also owned by the current signed in User, you should offer them options to 'Edit and/or 'Delete' the entry.

#### Model Details (5 pts):
SUCCESSFUL CREATION OF REQUIRED MODELS AND ASSOCIATED KEYS MANDATORY FOR ANY POINTS
* Each Wiki entry should support a required 'Post Title', 'Post Text', 'created date/time', 'last updated date/time', along with an *optional* 'Post Image'. *NOTE:* The image should be stored in a model instance (i.e. no external URLs)

* Each Wiki entry should also *optionally* support 0 to n 'Related Information' items each of which represent related information. Each post line item should also support a required 'Item Title', 'Item Text', 'created date/time', 'last updated date/time', along with an *optional* 'Item Image'. *NOTE:* The image should be stored in a model instance (i.e. no external URLs)

* Authors and all Wiki Entries and related items can be administered from your web app, this includes a signup page for new Authors (5 pts)

* Your application depends on the built-in Django Admin for some portion of your database maintenance (3 pts)

* You application depends on the built-in Django Admin for all  of your database maintenance (1 pts)

### RESOURCES:
* This project will require the use of imagefields in your model. See the documentation on how to use them: https://docs.djangoproject.com/en/2.1/topics/files/

* This project will require the use of the Django database search capabilities. See the documentation for more information: https://docs.djangoproject.com/en/2.1/topics/db/queries/


### CHALLENGES:
* Implement pagination so that only a certain number of Wiki Posts are displayed on the main page/search results, and the user can 'page' through the entries. 

* Add support for entering Wiki posts using the 'Markdown' syntax to support rich text formatting and other advanced formatting features.



