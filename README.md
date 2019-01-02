# Wagtail Freelancer

[![Build Status](https://travis-ci.org/AccordBox/wagtail-freelancer.svg?branch=master)](https://travis-ci.org/AccordBox/wagtail-freelancer)

This project is a combination of [startbootstrap-freelancer](https://github.com/BlackrockDigital/startbootstrap-freelancer) and [Wagtail CMS](https://github.com/wagtail/wagtail), you can use Wagtail StreamField feature to quickly edit the content of the page.

I build this project to help people better understand how StreamField of Wagtail works.

You can find more useful resources of Wagtail in my [Wagtail Tutorial Series](https://blog.michaelyin.info/wagtail-tutorials/)

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
```

### How to use it

### Edit portfolio using StreamField

[![Alt text](https://img.youtube.com/vi/_YMm6sah1F8/0.jpg)](https://www.youtube.com/watch?v=_YMm6sah1F8)

### Edit contact form using Wagtail Form

[![Alt text](https://img.youtube.com/vi/c_ItEbb_Zhw/0.jpg)](https://www.youtube.com/watch?v=c_ItEbb_Zhw)

### Screenshot

![](https://blog.michaelyin.info/upload/images/wagtail_freelancer_page_screenshot.original.png)
