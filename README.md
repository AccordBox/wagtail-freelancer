# Wagtail Freelancer

This project shows you how to build landing page (portfolio) using StreamField, FormBuilder of Wagtail.

* [How to build a landing page using Wagtail CMS](https://www.accordbox.com/blog/how-build-landing-page-using-wagtail-cms/)

* [How to build contact page in Wagtail](https://www.accordbox.com/blog/how-build-form-page-wagtail/)

## Live demo

The live demo is [Wagtail landing page](https://wagtail-landing-page.herokuapp.com/)

The admin page of this live demo is [Wagtail admin](https://wagtail-landing-page.herokuapp.com/admin) , you can use `admin:admin` to login and publish articles as you like.

**The database and media files would be reset after a while, so do not be surprised if your article is gone.**

## Run it in local env

```bash
git clone [the url you copied above]
cd wagtail-freelancer

# setup virtualenv
pip install -r requirements.txt

./manage.py runserver
# http://127.0.0.1:8000/blog
# username: admin  password: admin
```

### Screenshot

![](https://blog.michaelyin.info/upload/images/wagtail_freelancer_page_screenshot.original.png)
