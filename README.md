# The House Buddy

For my fourth project with Code Institue, I have created a website to store and organize receipts and other documents.
The website was created to store mainly receipts regarding properties, however, the user can create their own customized categories to fit their needs.

![amiresonsive-image](/documentation/images/amiresponsive.png)

For the live website, please click [here](https://the-house-buddy.herokuapp.com/)

- [The House Buddy](#the-house-buddy)
  * [User Experience](#user-experience)
    + [Who would the user be?](#who-would-the-user-be)
    + [Why would a user want this?](#why-would-a-user-want-this)
    + [What value will it add?](#what-value-will-it-add)
    + [What is already out there](#what-is-already-out-there)
  * [User goal](#user-goal)
    + [User stories](#user-stories)
    + [User stories fulfilment](#user-stories-fulfilment)
  * [Structure](#structure)
    + [Database models](#database-models)
    + [Site structure](#site-structure)
  * [Features](#features)
    + [Existing features](#existing-features)
      - [Home](#home)
      - [About](#about)
      - [Contact](#contact)
      - [The blog page](#the-blog-page)
      - [Blogpost detail](#blogpost-detail)
      - [The ‘My Page’](#the-my-page)
      - [Categories](#categories)
      - [Entries](#entries)
      - [Footer](#footer)
      - [Custom 403, 404 and 500 pages](#custom-403-404-and-500-pages)
    + [Features I would like to implement in the future](#features-i-would-like-to-implement-in-the-future)
  * [Wireframes](#wireframes)
  * [Colors and fonts](#colors-and-fonts)
    + [Colors](#colors)
    + [Fonts](#fonts)
  * [Images](#images)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Creating the repository](#creating-the-repository)
    + [Creating the Django project and apps](#creating-the-django-project-and-apps)
      - [Installing all libraries needed to start](#installing-all-libraries-needed-to-start)
      - [Create a Heroku app](#create-a-heroku-app)
      - [Attaching the database](#attaching-the-database)
      - [Set up the settings.py file with necessary folders and files](#set-up-the-settingspy-file-with-necessary-folders-and-files)
    + [Final deployment](#final-deployment)
  * [Technologies and resources used](#technologies-and-resources-used)
  * [Credits](#credits)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## User Experience

---

### Who would the user be?

---
The user could be anybody wanting to keep track and store receipts or other property-related documents.

The user could also be any of the 6 million people living in Sweden owning a property, or any other country that has the same tax rules as Sweden.

### Why would a user want this?

---
The main purpose of the app is to make it easier for the user to keep track of all the receipts, saving them all in one place. The user can sort them into different categories that they have created themselves to fit their need.

The site is especially useful for property owners in Sweden.

#### **Why?**

In Sweden, homeowners must pay a tax on the profit if they sell their property, which is at 22% today.
However, the tax can be reduced by the amount spent on home improvements, the cost of materials mainly, but also all other sorts of improvements that increase the value of the property, such as flowers and other small items.
It’s up to the homeowner to save and keep track of all the receipts, which can be a hassle, especially since it can add up to quite a few receipts of small sums, that in the end can result in a considerable grand total.

Another perspective is the real estate agent side of it, they are the ones who must put all the receipts together and send them to the tax office.  
More times than often they will be handed a bag of receipts from the homeowners, and then have to do the time-consuming task of sorting, adding and putting it all together, a workload that they could do without. Being able to retrieve all the receipts digitally from the start would save them a ton of time and work, maybe also making it possible to lower the commission as a bonus for the homeowners.

### What value will it add?

---
For all users it will add value in the sense that they will have all their receipts and information in one place, making it easier to find them if needed for warranty or other inquiries.

Moreover, for the Swedish homeowners, it will add value in the sense that they can save money on the profit tax, in a hassle-free way.

### What is already out there

---
Looking through forums on the subject I found that people still use maps and folders to store receipts manually, they found it difficult to use an online cloud service, this will make it easy for the user to snap a photo of the receipts and upload it to elective category. House Buddy is designed so that even the not-so-technical person should be able to use this website.

## User goal

---
**As a first-time user I would like to:**

- Easily find out the purpose of House Buddy
- Be able to navigate easily throughout the site
- Be able to read the blog without signing in
- Be able to contact the site owner and or blogger
- Be able to register for an account to use all functions

**As a registered user I would like to:**

- Be able to sign in to my account
- Get an overview of my categories and entries
- Easily manage my categories and entries
- Interact with a blogpost
- Be able to logout from my account

**As a site owner I would like to:**

- Restrict access to non-logged-in users
- Be able to control users' comments on the blog, making sure they are not inappropriate.
- Write blog posts

### User stories

---
I have used Github Issues to create user stories and to manage the project in an agile way.

![github-project](/documentation/images/github-projectboard.png)

These are the ones that have been implemented:

<details>
<summary>These have the label `must have`</summary>

1. Account registration
    - As a **site user** I can **register for an account** so that **I can benefit from all the logged-in user functions of the site, such as creating, viewing, editing, and deleting entries and/or categories.**

2. Manage categories
    - As a **logged-in site user** I can **create, view, edit and delete categories from my page** so that **I can manage my categories and organize my posts.**

3. Manage entries
    - As a **logged-in site user** I can **create, view, edit and delete entries on my page** so that **I can manage my entries and keep track of important receipts/information.**

4. View categories
    - As a **logged-in site user** I can **view all of my categories** so that **I can get a clear overview of all my different categories and easily find the one im looking for.**

5. Blog: View blogposts
    - As a **site user** I can **view a list of blog posts** so that **I can select which one I would like to read**

6. Blog: Choose a blog post to read
    - As a **site user** I can **click on the blog post I would like to read** so that **I can see the full post and all of the comments.**

7. Site navigation
    - As a **site user** I can **navigate the site using the navbar** so that **I can easily find the information/content I was looking for.**

8. Blog: Manage blog posts
    - As a **site owner** I can **create, view, edit and delete posts from the admin page** so that **I can manage my blog and its content.**

</details>

<details><summary>These user stories have the label `should have`</summary>

9. About the website
    - As a **site user** I can **read about the House Buddy website and the benefits of using it on an about page** so that **I can get to know more about the website and how I could get the most out of using it, also get inspired to create an account if I haven't already got it.**

10. Contact the site owner
    - As a **site user** I can **get in contact with the site owner** so that **I can ask questions, ask for help with my account or give them feedback**

11. Blog: Leave a comment on a post
    - As a **logged-in user** I can **leave a comment on a post** so that **I can let the author know how I feel about it, and interact with other users.**

12. Blog: Create drafts
    - As a **site owner** I can **create draft posts** so that **I can finish writing the blog post later**

13. Blog: Approve comments
    - As a **site owner** I can **approve or delete comments** so that **I easily can control that it won't be any offensive or hateful comments posted.**

14. Blog: View comments
    - As a **site user or site owner** I can **view comments in a blog post** so that **I can read the comments and see what others think about the post.**

15. Blog: Like or unlike posts
    - As a **logged-in site user** I can **like or unlike a post** so that **I can interact with the content**

16. Blog: View likes
    - As a **site user or site owner** I can **view the number of likes on each blog post** so that **I can see which is the most popular and if it's an appreciated blog post.**

</details>

<details><summary>These user stories have the label `could have`</summary>

17. Sort entries
    - As a **logged-in site user** I can **sort my entries by category, amount or date added** so that **I can easily find or sort my entries and get a good overview of them.**

18. Search for entries
    - As a **logged-in site user** I can **search for an entry** so that **I can easily find what I was looking for**

19. Sign up for a newsletter
    - As a **site user** I can **sign up for a newsletter** so that **I can receive interesting news from the House Buddy website and its owner.**

</details>

<details><summary>These user stories have the label of `won't have` and will not be implemented in this release</summary>

Blog: sort posts by category or date

- As a **site user** I can **sort blog posts by category or published date** so that **I can find a blog post in a certain category or the newest/oldest one.**

Blog: Like comments

- As a **logged-in site user** I can **like other people's comments** so that **I can interact with them.**

Blog: Manage blogpost frontend

- As a **site owner** I can **create, view, edit and delete blog posts from my logged in site (not /admin)**   so that **I can create and edit blogpost quick and easy**

These are now closed but can be opened again for future sprints.

</details>

The project board can be found [here](https://github.com/users/Ajn0r/projects/4/views/1)

---

### User stories fulfilment

| Nr | User story fulfilled |
| --- | --- |
| 1 | The user can register for an account by clicking on the sign-up button, either on the navbar under the user icon or on the home page, there is a button on the hero and one on the first card under the hero. There is also a quick link to sign up under benefits both on the about page and in the footer. |
| 2 | A signed-in user can view the total amount of categories they have on their 'my page' page, where they can also see up to 4 of their categories. They can choose to view or edit, or go to all categories where they will be able to delete a category as well. If they click on the view button on 'my page' they will see all entries in that category, and if they are on the category page, they can click on the name for the same result. |
| 3 | A signed-in user can view 4 of their latest entries on 'my page', where they have the option to view or edit the entry. There is a link to all entries that takes them to the entries page that shows all the entries by that user. To delete an entry the user needs to view it, and then can choose to edit or delete the item. |
| 4 | This is almost identical to user story 2, the user can view all categories if they go to the 'categories' page. If the user has many categories they will be paginated. |
| 5 | The user can go to the blog page, where a list of blog posts will be displayed, if there are more than 4 blog posts they will be paginated. |
| 6 | The user can read the full content of the blog post if they click on it, the whole card is a link to the specific post so it's easy even on smaller screens. Once clicked the user will be redirected to the blog post detail page, where they also can view all comments at the bottom. |
| 7 | The navbar is the same on all the pages, so it will be easily navigated, there are also some links in the footer to help the user to navigate. |
| 8 | The site owner can manage blog posts from the admin page. |
| 9 | The user can read about House Buddy on the about page, where there is both information about the blog and the site. The user is presented with the benefits of using house buddy and then a button to sign up. |
| 10 | The user can get in touch with the house buddy team by filling in the form on the contact page. The form is connected with emailJs to send an email to a Gmail made for House buddy. |
| 11 | A logged-in user can leave a comment on a blog post if they scroll down past the post. |
| 12 | The site owner can choose to create a draft on the admin site, there is a filter that only displays blog posts with the status of 'published' |
| 13 | The site owner can control all the comments from the admin site. |
| 14 | At the bottom of the blog detail page, all approved comments will be displayed. |
| 15 | The logged-in user can like a blog post by clicking on the heart at the top of the blog detail page. If the user wants to unlike the post they simply have to click again. the heart will be filled if liked and only contoured if not making it easy for the user to see if they have liked the post or not. |
| 16 | The number of likes on each post is shown on the blog page, at the top right corner of each post there is a heart with the number of likes next to it. |
| 17 | The logged-in user can sort entries by amount or date added on the entires page if they open the filter function by clicking on the filter button.  To filter entries by category the user has to go to the category page, and then click on the category they would like to view entries in. |
| 18 | The user can search for entries by title with the filter function, it will show results that contain what has been searched for, so it doesn't need to be exact. |
| 19 | In the footer there is a section where the user can sign up for a newsletter, however, the form is not connected to anything, but with the magic of JavaScript, it will make it look like the user has subscribed if they enter their email and press subscribe. |

[Back to top](#the-house-buddy)

## Structure

### Database models

![model](/documentation/images/models.png)

### Site structure

The website has been structured to be easily navigated and user-friendly. Users that are not signed in will be displayed slight different content than logged-in users, inviting them to sign up. Logged-in users also get access to 'my page' 'categories' and 'entries' pages.

There are 4 main pages and then 3 more for signed-in users
In total without the authorisation pages, there are 16 Html pages, one CSS, and one javascript file.

I have made two apps, one that handles the receipt organizing functionality and one that serves the blog and comment functions.
The homepage, about and contact URLs are in the main project 'house buddy' folder.

## Features

### Existing features

#### Home

The first page the user lands on is the 'Home' page, there is a large background image of houses, with a large jumbotron with text to give the user a quick idea of what house buddy is with a button that takes the user to the about page.

![home-signedin](/documentation/images/home-hero.png)

If the user is not signed in there will also be a button to sign up.

![home-notsignedin](/documentation/images/home-notsi.png)

Further down there are 3 cards, the first changes depending on if the user is signed in or not, and the other two stay the same.

![home-cards](/documentation/images/home-cards.png)

The user is redirected to 'My page' if they log in instead of Home.

#### About

The about page contains information on what House buddy can offer.
The landing of the about page is a background of bricks with the text “We are House Buddy” vertically on the whole page and a downward pointer that bounces.

If the user clicks the bouncer they will be directed down to the about content.

![aboutpage-hero](/documentation/images/about-page.png)

The first part covers the fundamental idea of House buddy, and also a piece of short information about the blog and who runs it. It’s a made-up woman called “Kiela”.

![about-text](/documentation/images/about-text.png)

Further down on the page there are 4 icons and short benefits descriptions as to why the user should use House buddy.

![benefits](/documentation/images/benefits.png)

There is a collapsible part that has the heading “Do you own a property in Sweden?

![aboutpage-sweden](/documentation/images/swe-benefit-col.png)

If the user clicks that then the information on how to save money on tax if they sell their property, and how using house buddy can make life easier for them

![openedsweden-benefits](/documentation/images/swe-benefit.png)

#### Contact

The contact page consists of a short text encouraging the user to get in touch and suggesting what the user could contact House Buddy about.

![contact-page](/documentation/images/contactform.png)

On large screens, the form is on the right of the text, and on medium and smaller it is below the text.

The user has to input their name, and email, choose from a list of subjects to why they want to get in touch, and then the message. All fields are required.

The form is sent to a house buddy email with emailJs, so the contact form is fully functional. Once sent the user will be displayed a modal with a success message.

![contactformsent](/documentation/images/contact-sent.png)

#### The blog page

The blog page greets the user with an image with the text “The house buddy blog” on top.

![blogpage](/documentation/images/blogpage.png)

Under the image, there are four cards each showing a blog post.

The card has the category on top, followed by the title, date published, and then the first 17 words of the post, encouraging the user to read more.

![blogcard](/documentation/images/blogcard.png)

On the top right corner, there is an icon for comments with the number of comments and a heart with the number of likes each post has.

When there are more than four posts the pagination will appear.

At the bottom of the page, there is an 'about' box where the user can read about Kiela, the girl who writes all the blog posts. There is also a link to get in touch with her that takes the user to the contact page.

![blog-about](/documentation/images/blog-about.png)

#### Blogpost detail

The blog post detail page is where the user can read the full blog post, it’s also where they can like and comment on the post.

The first thing that the user sees is the “heading” which is the title of the post, followed by the published date and what category the post is in. On large and medium screens the like button shaped like a heart is at the right corner, it will stack under the heading on smaller screens.

![blogpost-detail](/documentation/images/blogpost.png)

A horizontal line separates the heading and the content and image.  
On smaller screens, the image will appear on top and the content of the post under. On medium and larger screens the text will wrap around the image for a better experience.

Once the post is finished the comments will be displayed, with a comment form where logged-in users can submit a comment.

![comments](/documentation/images/comments-signedin.png)

If the user is not signed in they will not be able to leave a comment, instead they are asked to login or sign up

![comment-ifnot-signedin](/documentation/images/comments-not.png)

#### The ‘My Page’

The user has their page where they are greeted with ‘Welcome username’ and it also shows the last login date.

![mypagestart](/documentation/images/mypage-welcome.png)

On smaller screens, the number of categories and entries is displayed under the welcome phrase, and all others it is to the right.

The user is then presented with up to 4 of their categories, a button for adding a new category, and a button to go to all categories, the same is displayed for entries under the category row.

![mypage-categories-entries](/documentation/images/mypage-end-full.png)

If the user hasn't got any categories or entries yet there will be a text instead encouraging the user to get started.

![mypage-categories-entries-empty](/documentation/images/mypage-end.png)

#### Categories

The category page is a listview that displays all the user's categories, the page starts with a button to take the user back to ‘my page’ and one to add a new category.

![categories-page](/documentation/images/categories-list.png)

If the user doesn’t have any categories there will be a text saying ‘It looks like you don't have any categories yet, add one to get started to encourage the user to add a category.

To create a new category the user has to enter a name for the category and then press save.

![new-category](/documentation/images/new-category.png)

Once the user has created some categories they will be displayed as cards, The category name will be displayed first, which also is a link to view entries in that category.

There are two buttons, one for editing and one for deleting the category.

To edit the category, the user can choose a new name and press update, or just choose to go back.

![edit-category](/documentation/images/edit-category.png)

If the user chooses to delete the category they will be redirected to a delete confirmation page, to make sure they don’t accidentally remove a category.

![delete-category](/documentation/images/delete-category.png)

#### Entries

There are two ways to view entries, one is by clicking on ‘view all entries’ on my page or ‘entries’ on the navbar, this will display all entries and also provides a search/filter function.

![all-entries](/documentation/images/all-entries.png)

The user can choose to filter or search on any word or letter that the title contains, by amount or date of purchase

![filter-option](/documentation/images/filter-options.png)

![filter](/documentation/images/filter-result.png)

If the user wants to view only entries in a certain category, they will have to click either on ‘view’ on the category on 'my page', or the category name on the category page.

#### Footer

The footer consists of 4 different columns that stack on top of each other on small devices.

![footer-large](/documentation/images/footer-lg.png)

The first has the heading House Buddy and then displays a short description of the website, followed by a text that lets the user know that the site is for educational purposes.

The second column consists of the same links as in the header, home, about, contact and blog.  
If a user has many entries and is at the bottom it makes it easier for them to navigate than to scroll back up to the top.

The third column has different content depending on if the user is logged in or not.
If the user is not logged in it will display two of the benefits of using house buddy. Below those, there is a link to the about page that invites the user to learn more about the benefits.  
The last object is a link to sign up.

If the user is signed in there will be four links, one for categories, one for adding a new category, a third for entries and the last for adding a new entry.

The fourth and last column is a suggestion to sign up for a newsletter.
If the user would like they can submit their email and get a newsletter every two weeks. The form doesn’t go anywhere at this time, but I have used JavaScript to make it visible to the user that they have successfully signed up.

![footer](/documentation/images/footer-medium.png)

#### Custom 403, 404 and 500 pages

I have made very basic 403.html, 404.html and 500.html pages that the user will land on instead of the default ones if something goes wrong.

### Features I would like to implement in the future

- When the user clicks on “add a new entry” while in a specific category, the category field should already be populated. In this release, the user has to choose from the list of their categories.

- Refine the filter function - I would like to take the filter function even better, it has been implemented in the most simple way to get the basic filter/search function in place.

- I would also like to add a filter function to the blog so the user chose to filter by categories, most popular post, published date and number of comments.

- For the next release, I would also like to style the 403, 404 and 500.html pages a bit better, they are very basic at this point.

- Some of the pages are taking some time to load, so for the next release I would like to add a spinner when the page is loading so the user doesn’t have to guess what is happening

- I would like to add a feature that allows the user to add up the total amount of one or all categories, to get a clear overview of how much was spent on each.

[Back to top](#the-house-buddy)

## Wireframes

Wireframes were made very early in the project, and the finished product is not 100% accurate to the initial wireframes.

I ended up not using the logo since I felt it looked better in plain text with the Lora font.

- Homepage

![wiref-home](/documentation/images/home-lg.png)

![wf-home-md](/documentation/images/home-mb.png)

- About

![wf-about](/documentation/images/about-lg.png)

- Contact

![wf-contact](/documentation/images/wf-contact.png)

- Entries and Categories

![wf-categories](/documentation/images/wf-categories.png)

![wf-category](/documentation/images/wf-category-mb.png)

![wf-entries](/documentation/images/wf-entry-mb.png)

## Colors and fonts

### Colors

The colours have been found using Adobe Color & Coolors.

The blue/teal colours are used for buttons, links and some icons, and the light grey and green-grey colour is used for the background on the page.

The orange colour is used on some links when hovered such as the down one on the about page.

![colors](/documentation/images/housebuddy-colors.png)

### Fonts

Fonts that have been used if from google fonts.

For all types of headings, I have used 'Lora'

![lora](/documentation/images/lora.png)

For all other text on the page 'Lato' has been used.

![lato](/documentation/images/lato.png)

## Images

All images used for the site have been found on [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/), however, some of the images for the blog in the readme are my own that I have used only for testing.

## Testing

All tests and validations can be found [here](/TESTING.md)

## Deployment

I have followed the Code institute 'I think therefore I blog' Django Deployment Instruction to set up and deploy my project.

### Creating the repository

I have used the Code Institute Gitpod Full Template for this project.
By clicking on 'use this template' I created the repository on GitHub under my username.

### Creating the Django project and apps

#### Installing all libraries needed to start

Django and gunicorn

`pip3 install 'django<4' gunicorn`

Supporting database libraries

`pip3 install dj_database_url psycopg2`

Cloudinary libraries to manage static files

`pip3 install django-cloudinary-storage`

Create a file for requirements

`pip3 freeze --local > requirements.txt`

Create a project: `django-admin startproject house_buddy`

Create my two apps `python3 manage.py startapp receipts_organizer` and `python3 manage.py startapp blog`

Add my apps to the list of `installed apps` in the settings.py file in `house_buddy`

Migrate changes with `python3 manage.py migrate`

Test that the server works locally with `python3 manage.py runserver`

#### Create a Heroku app

1. Logged into my account on Heroku  

2. From Heroku Dashboard clicked on 'New' and 'Create new app'

3. Gave the project the name of 'the-house-buddy' which was approved. I set the region to Europe and created the app.

4. In the resources tab, under the section 'add-ons', I searched for 'Heroku Postgres' and selected that package for the database.

5. In the settings tab under 'Config Vars', I added the keys that I needed to start the development, which was SECRET_KEY, DATABASE_URL and CLOUDINARY_URL

6. I also added PORT with the value of 8000 and DISABLE_COLLECTSTATIC with the value of 1 still in the config vars section.

#### Attaching the database

1. In gitpod, I created an env.py file and make sure it was added to the .gitignore file.

2. In the env.py I imported os library `import os`, set environment variables and added my secret key

`os.environ["DATABASE_URL"] = "Heroku DATABASE_URL Link"`

`os.environ["SECRET_KEY"] = "thisisnotmyrealsecretkey"`

also added my Cloudinary API key with `os.environ["CLOUDINARY_URL"] = "cloudinary://************************"`

#### Set up the settings.py file with necessary folders and files

1. To connect the environment variables and also import messages I added this code.

```
from pathlib import Path
import os
import dj_database_url
from django.contrib.messages import constants as messages

if os.path.isfile("env.py"):

import env
```

2. Added all necessary apps inside of `INSTALLED_APPS`

3. Replaced the default DATABASES with
`DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}` To connect with my database.

4. For all my static files I added this code to connect it to Cloudinary

```
MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


STATIC_URL = '/static/'

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

5. Setup templates with `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')` and added `TEMPLATES_DIR` within the TEMPLATES array in 'DIRS': key.

6. Added my Heroku hostname to ALLOWED_HOSTS array.

7. Finally added a Procfile with the code `web: gunicorn house_buddy.wsgi`

8. Push to GitHub for deployment with

`git add .`

`git commit -"first try deployment commit"`

`git push`

9. In Heroku, I deployed the project manually with the GibHub deployment method, and choose the house_buddy repository.

In the first deployment, I forgot to set up my secret key variable in the settings.py file, so I corrected it by adding `SECRET_KEY = os.environ.get('SECRET_KEY')`  and deployed once more now successfully.

### Final deployment

For the final deployment, I changed  DEBUG to False and added `X_FRAME_OPTIONS = 'SAMEORIGIN'` in the settings.py file.

Then on Heroku, I removed the `DISABLE_COLLECTSTATIC` var under Config Vars.

Finally deployed it manually and made sure it was successfully deployed.

## Technologies and resources used

- Programming languages used: Python 3.8, Java Script, HTML5 and CSS3

- Gitpod - Used to create/edit the code of the project

- Git for version control

- Github - Used to create the repository, for version control and agile project managing

- Heroku - Used to deploy and host the project

- Django - Used in the development of this project

The following packages has been installed:

```
asgiref==3.5.2
cloudinary==1.29.0
dj-database-url==1.0.0
dj3-cloudinary-storage==0.0.6
Django==3.2.15
django-allauth==0.51.0
django-crispy-forms==1.14.0
django-filter==22.1
django-summernote==0.8.20.0
gunicorn==20.1.0
oauthlib==3.2.0
psycopg2==2.9.3
PyJWT==2.4.0
pylint-django==2.5.3
pylint-plugin-utils==0.7
python3-openid==3.2.0
pytz==2022.1
requests-oauthlib==1.3.1
sqlparse==0.4.2
```

- Bootstrap - Used to style the project

- PostgreSQL - Used as the database for this project through Heroku

- Cloudinary - Used to upload images and cloud hosting service

- Balsamiq - Used to create the wireframes

- Adobe Color - User for choice of colours

- Coolors - Used for the palette used in the README

- Google Fonts - Used for font selection

- Pexels and Unsplash for images

- Font Awesome - Used for the icons

- Favicon.io - Used to implement the favicon on the website

- Grammarly for writing all texts, hopefully, correct

- GitHub Wiki TOC generator for table of content in readme

- DevTools - Chrome - to assist in the development of the project

- Lighthouse (Chrome Devtools) Used to performance test

- PEP8online - Used to test/validate Python code

- [Beautify Tools](https://beautifytools.com/javascript-validator.php) for validating the Javascript

- W3C CSS Validation Service for validating the CSS file

- [The Nu Html Checker](https://validator.w3.org/nu/) - Used to validate Html code

- [Dbdiagram.io](https://dbdiagram.io/home) for making the Database model diagram

- EmailJs for sending emails from the contact form to thehousebuddyapps Gmail

## Credits

- For setting up the Django project I have used the Code institute “Django Deployment Instruction”

- For the blog app, I have used the Code Institute “I think therefore I blog” walkthrough as a base, and changed it slightly to fit my project

- Daryl Howai_Alumni solution on slack for images not uploading to Cloudinary

- [The Dumbfounds youtube](https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2) video for URL testing

- [Cryce Truly youtube](https://www.youtube.com/c/CryceTruly) for adding custom error handling pages

- [Very Academy youtube](https://www.youtube.com/c/veryacademy) for learning more about Django Class-based Views.

- [Dennis Ivys youtube](https://www.youtube.com/c/DennisIvy/featured) for inspiration and to learn more about Django

- [For setting the class of active in the template](https://stackoverflow.com/questions/9793576/how-to-render-menu-with-one-active-item-with-dry )

- I have used and relied on the official docs for Django, Bootstrap, Allauth, Django filters and EmailJs when creating this project.

- I have used w3Scool and stack overflow for troubleshooting when in need.

- These have been particularly helpful and also credited in the code.

    * [for displaying foreignkey values](https://stackoverflow.com/questions/71692499/django-foreign-key-display-values-in-detail-view)

    * [for passing user object into forms.py](https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c)

- Thanks to my mentor Spencer Barriball for guiding and supporting me

[Back to top](#the-house-buddy)