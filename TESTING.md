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
| blog.html | Error |
| blogpost_detail.html | Error |
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

## Bugs

1. With unique=True in the name field on the Categories model restricted users from having the same name on a category as another user.

    I wanted to prevent one user from having duplicate categories, but two different users must be able to both have categories with the name “garden” as an example.  

    I first used Django unique_together but read that Django recommended using “UniqueConstraint” instead since it comes with more functionality.

    The user could now not make duplicates, however, if the user tried it anyway Django would raise an IntegrityError, and it was not caught by form_valid.
    I imported IntegrityError from django.db and in the form valid function, I put a try/except statement that handles all IntegrityErrors as a solution.

    The code worked and solved the problem, however later when testing to add a new category with the same name that already existed, only with all lowercase letters, the category was successfully created and once again I had duplicates. The solution was to add a clean_name function to the NewCategoryForm and return the name with .lower()

    I have added the title tag to the template so the user will see their category's name capitalized for better visual display.

2. The email input didn’t have a required tag in the newsletter form so the user could just press the subscribe button and get the feedback that they had subscribed without actually entering an email address.  

3. When creating a new entry, the user could choose from all categories in the database, with was not restricted to the specific user.
I wasn’t sure how to get the user inside forms.py, I found a solution on (link to webpage) which was to use get form kwargs in the view and pass the request to form. In the NewEntryForm I could then use the __init__ method to get the request and then reach the user.