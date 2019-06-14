# Process

## Day 1
Today I wrote the project proposal. I decided customers who aren't a member of the gym can use the webshop, and personnel can overview not only orders and the schedule but also the type of subscription members have. Furthermore, I chose not to develop a chat for members and their coach at the gym, because this would be too extensive for the time available for this project.

## Day 2
Today I worked on the design of my webapp, sketched the association between different parts of the application and set up the models' structure. For the prototype I decided to focus on the django eventtools framework and on the difference in user types (personnel, guests, members without group lessons, members with group lessons) and the consequences this type has on the functionality and interface of the webapp.

## Day 3
Today I set up the project, created all necessary html pages and linked them to eachother. I asked feedback about the feature where non-members can order from the shop as well, and both Lars and Nils adviced me to register guests with name and emailadress only, instead of a regular member account. I then worked on the index page and scss.

## Day 4
During the standup we discussed possible problems/bottlenecks for the coming weeks of development. Nils and Lars agreed that the calendar function could be difficult to implement, which I why I will begin working on this today. Furthemore, the option to shop as a guest could be timecostly as well, therefore this is the first thing on my to do list for next week.

## Day 5
For todays meeting we sat down with our tech assistent and gave a short tour through our app so far. Marijn suggested to use a different framework for the calendar function, which I spend the rest of the day on. I decided to go with the fullcalendar.io framework because this calendar had more different views (day/week/month) and mainly relies on javascript instead of python, which makes it easier to adjust. Marijn agreed that the calendar and extending the user model are aspects that need priority next week.

## Day 6
Today I continued working on the calendar, which turned out to be a timecostly part of this project. I had trouble implementing switching views and adding events, therefore I decided to leave this for now and ask help from Marijn tomorrow. I started working on the webshop & cart functions, and focused on the models I need for this.

## Day 7
With help of Marijn the calendar view can be switched now (between day, week and month). For the webshop and subscriptions functionality, the user model needed to be customized which was had far-reaching effects. From this experience and the django documentation I used for this I learned that this step is best done at the beginning of a new project, which I will take with me for future works. During out standup, we discussed which styleguide we would adhere to.

## Day 8
Today I finished the registration, and worked on the webshop which still has some bugs. With our stand-up team we further discussed the styleguide, which I processed in STYLE.md.

## Day 9
During our team meeting Marijn gave me feedback for my model structure for the webshop. I decided to create my own manytomany model, and began restoring the webshop functionality using these models.
