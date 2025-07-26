# Changelog

## [July 2025]
- Learning about Django and initial project setup.
- Added a gallery view that displays a random image on each page load using [picsum.photos](https://picsum.photos).
- Passed a random number from the Django view to the template to ensure a new image is shown each time.
- Refactored views.py gallery function to use Django's render shortcut, which loads the template, passes the context, and returns the HTTP Response in one step (Cleaner and more idiomatic code)
