# Wagtail Freelancer

This project shows you how to build landing page (portfolio) using StreamField, FormBuilder of Wagtail.

## Live demo

The live demo is [Wagtail landing page](https://wagtail-landing-page.herokuapp.com/)

The admin page of this live demo is [Wagtail admin](https://wagtail-landing-page.herokuapp.com/admin) , you can use `admin:admin` to login and publish articles as you like.

**The database and media files would be reset after a while, so do not be surprised if your article is gone.**

Setup (with Vagrant)
--------------------

We recommend running Wagtail in a virtual machine using Vagrant, to ensure that the correct dependencies are in place.

### Dependencies
 - [VirtualBox](https://www.virtualbox.org/)
 - [Vagrant 1.1+](http://www.vagrantup.com)

### Installation

Run the following commands:

```bash
git clone [the url you copied above]
cd wagtail-freelancer
vagrant up
vagrant ssh

# then, within the SSH session:

./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8000

# Please visit http://127.0.0.1:8000/admin to enter the Wagtail admin to edit the page

### Screenshot

![](https://blog.michaelyin.info/upload/images/wagtail_freelancer_page_screenshot.original.png)
