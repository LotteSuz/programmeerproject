# Project Proposal

## Problem
YourGym is a cool new gym which offers free weights training and group lessons. They need a web application to recruit members, keep track of the group lessons schedule and sell branding.

## Solution
A django written web application will enable people to subcsribe to YourGym, browse the timetable, enroll for classes and shop products. The gym personnel can monitor members, class subscriptions and webshop orders.

### Index Page
![alt text][yg1]

[yg1]: https://github.com/LotteSuz/programmeerproject/blob/master/images/YourGym1.png "Index Page"

### Timetable
![alt text][yg2]

[yg2]: https://github.com/LotteSuz/programmeerproject/blob/master/images/YourGym2.png "Timetable"

### Webshop
![alt text][yg3]

[yg3]: https://github.com/LotteSuz/programmeerproject/blob/master/images/YourGym3.png "Webshop"

## Prerequisites
__• Data sources__ No data sources will be used for this project.

__• External components__ For this project Django 2.2 will be used. This web framework is free and open-source.

__• Other Apps__ A comparable web application is that of Vondelgym (http://www.vondelgym.nl). This web application allows customers to subscribe to the gym, check out the schedule and enroll for classes. Navigation through this app is intuitive and the design modern, which are important aspects for the YourGym app as well. The webshop, though not promimently placed in the design, is organized and modern as well. The Vondelgym application is very extensive, which makes a bit overwhelming even though there is clear navigation options. The YourGym app will be less extensive, which will make the options more clear. Furthermore, the YourGym timetable will be organized based on starting times, not on type of classes, and can both be displayed as a daily- and weekly schedule as opposed to the merely weekly schedule of Vondelgym.

__• Limitations__ Technical difficulties during this project can arise in granting members with different types of subscriptions, different kinds of possibilities. A way to overcome this could be adding a code to every member, representing their type of subscription and checking this code in different aspects of the application. Another difficult aspect is keeping track of the stock of the webshop items. It should be well taken care of that the stock decreases after an order, furthermore it should possible to change the stock manually.

## Features
__• Subscriptions__ The index page contains the 2 different kinds of subscriptions available, where members can select the preferred program and are redirected to registration.

__• Register__ Users are able to register for 2 different kinds of subscriptions.

__• Members__ Personnel can browse the memberbase, and for each member see their subscription and classes they are currently enrolled for.

__• Login/Logout__ Members can login to get access to the timetable and their shoppingcart, and logout.

__• Webshop__ The webshop is available to members as well as visitors who can order with a guest account. Personnel can edit the amount of stock available for purchase.

__• Timetable__ Personnel can add classes to the schedule, which can be viewed by all members.

__• (Un)Subscribe for classes__ Members with a subscription for group lessons can enroll for classes, and unsubscribe if needed. Members with a non-group subscription can view the timetable, but not enroll for classes.

