# The House Buddy

## Validation

### Pep8 Python validation

pep8online.com was user to validate all python code.

#### Validation for the receipts_organizer app

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

#### Validation for the blog app

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

## Lighthouse

Lighthouse testing was performed but did not score very well on mobile

![lighthouse-mobile](/documentation/images/testing/lighthouse-mobile.png)

However, the opportunities for performance improvement were related to things out of my control and knowledge at this point, but might be something to investigate in the future.

![lighthouse-error](/documentation/images/testing/lighthouse-error.png)

Lighthouse on desktop performed much better than on mobile, the home page however has a lower SEO score than other pages.

![lighthouse-desktop](/documentation/images/testing/lighthouse-desktop.png)

I could probably solve it by putting a button inside of the a link and the text inside of the button, however, I feel that it is a satisfactory result as it is.

![lighthouse-ceo](/documentation/images/testing/lighthouse-ceo.png)
