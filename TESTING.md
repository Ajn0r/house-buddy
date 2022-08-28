# The House Buddy

## Validation

### Pep8 Python validation

pep8online.com was user to validate all python code.

<details><summary>Validation for the receipts_organizer app</summary>

- admin.py

![pep8admin](/documentation/images/validation/pep8-admin.png)

- views.py

![pep8views](/documentation/images/validation/pep8-views.png)

- urls.py

![pep8url](/documentation/images/validation/pep8-urls.png)

- models.py

![pep8models](/documentation/images/validation/pep8-models.png)

- forms.py

![pep8forms](/documentation/images/validation/pep8-forms.png)

- filters.py

![pep8filters](/documentation/images/validation/pep8-filters.png)

- tests.py

![pep8tests](/documentation/images/validation/pep8-tests.png)

</details>

<details><summary>Validation for the blog app</summary>

- admin.py

![pep8adminblog](/documentation/images/validation/pep8-adminblog.png)

- views.py

![pep8viewsblog](/documentation/images/validation/pep8-viewsblog.png)

- urls.py

![pep8urlblog](/documentation/images/validation/pep8-urlblog.png)

- models.py

![pep8modelsblog](/documentation/images/validation/pep8-modelsblog.png)

- forms.py

![pep8formsblog](/documentation/images/validation/pep8-formblog.png)

</details>

## Html validation

Html validation was carried out on all pages using [The Nu Html Checker](https://validator.w3.org/nu/)

The pages that required the user to be logged in have been validated by pasting in the source code for each page.

| Page | Status |
| --- | --- |
| index.html | Pass |
| contact.html | Pass |
| about.html | Warning |
| blog.html | Pass |
| blogpost_detail.html | Pass |
| mypage | Pass |
| category_page.html | Pass |
| category_detail.html | Pass |
| categories_confirm_delete.html | Pass |
| new_category.html | Pass |
| edit_category.html | Pass |
| new_entry.html | Pass |
| entries_page.html | Pass |
| edit_entry.html | Pass |
| entry_detail.html | Pass |
| base.html | Pass |

Both blog.html and the blogdetail page give errors of  "No p element in scope but a p end tag seen." however, if validated without the content in the blog post it is ok.

![blogvalidation](/documentation/images/validation/blog-validation.png)
![blogvalidation](/documentation/images/validation/blogpost-validation.png)

These issues were resolved by changing the p element surrounding to a div instead. 
I also added a class to keep the font family to Lato no matter which font was used in the admin panel. The validator now passes without any errors.

There is a warning on the about.html page about using h1 in both the header and on the page, this will be corrected in the next sprint.

![about-warning](/documentation/images/validation/contact-warning.png)

There was a warning on the contact page which was solved by removing 'required' from the select input in the form

![contact-warning-ok](/documentation/images/validation/contact-validation-ok.png)

## CSS Validation

CSS validation was carried out at W3C CSS Validation Service

One error was discovered at first, I had not set up text-shadow correctly, which was easily fixed by simply removing it, it had not worked so I wouldn't miss it in the design.

![css-error](/documentation/images/validation/css-error.png)

I ran the code again through the validator and it passed.

![css-fixed](/documentation/images/validation/css-valid.png)

## Javascript Validation

Javascript has been validated using [Beautify Tools Javascript validator](https://beautifytools.com/javascript-validator.php)

At first, a few semicolons were missing, but after adding those all Javascript was successfully validated.

![js-valid](/documentation/images/validation/js-valid.png)
![js-contact-valid](/documentation/images/validation/contact-js-valid.png)
![js-filter-valid](/documentation/images/validation/filter-js-valid.png)

## Lighthouse

Lighthouse testing was performed but did not score very well on mobile

![lighthouse-mobile](/documentation/images/testing/lighthouse-mobile.png)

However, the opportunities for performance improvement were related to things out of my control and knowledge at this point, but might be something to investigate in the future.

![lighthouse-error](/documentation/images/testing/lighthouse-error.png)

Lighthouse on desktop performed much better than on mobile, the home page however has a lower SEO score than other pages.

![lighthouse-desktop](/documentation/images/testing/lighthouse-desktop.png)

I could probably solve it by putting a button inside of the a link and the text inside of the button, however, I feel that it is a satisfactory result as it is.

![lighthouse-ceo](/documentation/images/testing/lighthouse-ceo.png)

## Testing

I have made one test_urls.py file in the receipt organizer app to test all URLs.

The rest of the project has been manually tested with the use of an excel sheet.

The project has also been tested on responsiveness on iPhone 12, Ipad, Macbook, PC, and also in Chrome Developer tools for more screen sizes and scenarios.

These are the manual tests that have been carried out.

- Navbar

![test-navbar](/documentation/images/testing/test-navbar.png)

- Footer

![test-footer](/documentation/images/testing/test-footer.png)

- Home

![test-home](/documentation/images/testing/test-home.png)

- About

![test-about](/documentation/images/testing/test-about.png)

- Conctact

![test-contact](/documentation/images/testing/test-contact.png)

- Blog

![test-blog](/documentation/images/testing/test-blog.png)

- My page

![test-mypage](/documentation/images/testing/test-mypage.png)

- Categories

![test-categories](/documentation/images/testing/test-categories-1.png)
![test-categories-cont](/documentation/images/testing/test-categories-2.png)

- Entries

![test-entry](/documentation/images/testing/test-entries.png)
![test-entry-cont](/documentation/images/testing/test-entries-2.png)

### Issues found during testing

1. The email field in the newsletter form in the footer was not required, so the user could simply click the subscribe button and it would appear as if they had successfully signed up for the newsletter. This was simply corrected by adding 'required' to the email input field.

2. There was no pagination on the category_detail.html page, this was simply adjusted by adding 'paginate_by = 6' to the CategoryDetails class in the views.py file

## Bugs

Being my first ‘real’ Django project I sure stumbled on a lot of things along the way, and I would probably do things differently the next time, but I guess that’s what learning is all about.
Here are some of the bugs I handled through the project, smaller bugs that were solved straight away are not on this list.

The first deployment failed, this was due to that I forgot to set the secret_key = os.environ.get link to the env.py file, and was quickly solved once discovered.

1. A bug that let other users delete, edit and view other users' categories and posts.

    While testing I found out that a user that was logged in could view, edit and delete another user's entry or category by entering the URL and pk. While the user could only see their categories and entries, they could input the URL and the pk for another user's entry and reach it that way.

    This was handled by adding test_func and UserPassesTestMixin to the views that were concerned.

2. On the blog page, the number of comments is displayed, this however displayed the total amount of comments on the post, even if they weren’t approved.
    I tried to reach only the comments that were approved but without luck, after some consideration and talking to my mentor I decided to make all comments approved by default instead, seeing as this also is more realistic to today's standard of comment fields.

    In the future, I would consider adding some functionality that catches 'bad words' and if any of those words are in the comment, it would be set to not approved, however, I'm not quite sure how so it will be for a future release.

3. With unique=True in the name field on the Categories model restricted users from having the same name on a category as another user.

    I wanted to prevent one user from having duplicate categories, but two different users must be able to both have categories with the name “garden” as an example.  

    I first used Django unique_together but read that Django recommended using “UniqueConstraint” instead since it comes with more functionality.

    The user could now not make duplicates, however, if the user tried it anyway Django would raise an IntegrityError, and it was not caught by form_valid.
    I imported IntegrityError from django.db and in the form valid function, I put a try/except statement that handles all IntegrityErrors as a solution.

    The code worked and solved the problem, however later when testing to add a new category with the same name that already existed, only with all lowercase letters, the category was successfully created and once again I had duplicates. The solution was to add a clean_name function to the NewCategoryForm and return the name with .lower()

    I have added the title tag to the template so the user will see their category's name capitalized for better visual display.

6. When creating a new entry, the user could choose from all categories in the database, with was not restricted to the specific user.
I wasn’t sure how to get the user inside forms.py, I found a solution on (link to webpage) which was to use get form kwargs in the view and pass the request to form. In the NewEntryForm I could then use the __init__ method to get the request and then reach the user.


### Unsolved bugs

1. The user can input something that is not an image and will be sent to a 500 error page.
I have tried to fix it several ways however it is still left unsolved. I have created a custom 500.html page that the user lands on where they are let aware that something went wrong and a button to go back.

2. The entries won't be paginated at the category_details page, I thought it was since I forgot to set paginate_by, but that won't work. I'm presuming it is because it is using the categories model so I will have to set the pagination somewhere else. This bug was discovered really late in the process so it is still not resolved. I did however instead set the max width and overflow to scroll as a quick fix. The code for the pagination is still on the template so it is ready to go once fixed. Entries on the entries page are still paginated as they are supposed to.
