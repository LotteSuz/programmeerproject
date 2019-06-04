# Design

## Sketches
![alt text][overview]

[overview]: https://github.com/LotteSuz/programmeerproject/blob/master/images/overview.png "Overview Sketch"

## Frameworks
The django eventtools package will be used to handle the calendar function needed for the timetables at the gym schedule & personal schedule page. Documentation of this package: https://github.com/gregplaysguitar/django-eventtools

## Models

### 1 | Users
<pre>
username          | CharField
email             | EmailField
first name        | CharField
last name         | CharField
staff status      | BooleanField
subscription      | CharField
</pre>

### 2 | Timetable
<pre>
name              | CharField
instructor        | CharField
datetime          | DateTimeField
duration          | IntegerField
max participants  | IntegerField
</pre>

### 3 | Personal Schedule
<pre>
username          | CharField
lesson            | ManyToManyField (timetable)
</pre>

### 4 | Stock
<pre>
name              | CharField
color             | CharField
price             | DecimalField
description       | CharField
amount            | IntegerField
</pre>

### 5 | Cart
<pre>
username      | CharField
item          | ManyToManyField (webshop)
</pre>
