# Final Report

This webapplication was created as a final project for the minor in programming at the University of Amsterdam. YourGym is a fictional gym, and its web application's core functionalities are for future members to subscribe and for members to enroll for group lessons and to order items from the webshop. Personnel is granted some extra features, such as uploading new items to the webshop and monitoring current memberships.

![alt text][index]

[index]: https://github.com/LotteSuz/programmeerproject/blob/master/images/readme_index.png "Index page"

## Technical Design
### Models
To discriminate between members with different types of subscriptions, I created a custom user model. This allows for expanding upon the standard Django user model, so now users have their type of subscription and access to group-lessons as extra attributes.

To keep track of the shopping carts, I made use of a custom made many-to-many model ‘CartItem’. This model keeps track of which items from the ‘Stock’ model are currently in any user’s ‘Cart’. Upon ordering, all items are moved from the user cart to the ‘Order’ model.

The ‘Event’ and ‘Participant’ models are center in the calendar function. These models keep track of all group-lessons that are available for members, and of which member enrolled for which lesson.

### Views
The view functions can be divided into three categories: User authentication, Webshop and Calendar. Important aspects of each category's main functions will be discussed in more detail.

An important aspect of the register function, is the discrimination between different types of subscriptions future members can register for. The subscription type is requested through a POST-method and processed into a new user object together with the other validated information from the registration form.

For the webshop there is the option for personnel to add new items, which is done through submission of a DocumentForm. This form is validated and added to the Stock model. The cart view handles ao requests from users to add items to their cart, here some important checks are put in place. First, whereas all users can visit the webshop only YourGym members can order items. An alert will be activated if a visitor tries to add something to their cart. Further, items will only be added to a cart if there is sufficient stock. Upon ordering the items from the cart, the Order function instantiates a mollie payment. In case of a succesful payment the order will be finalized, otherwise the items will remain in the cart for the user to try payment again.

Last, the (Your)Events functions play a central role in rendering the calendars. These functions get the appropriate event objects from the database, turn them into a list of dictionaries of the objects' needed attributes, and returns a JSON response to display the events in the calendars. Group lessons for which a member wants to enroll, are added to the YourEvent model through the enroll function.


## Development
Important changes in the features of this webapplication largely include changes to the calendar functionality, furthermore the webshop underwent some adjustments as well.

### Calendar
The first diversion from the original proposal regarding the calendar, is that members who have a subscription without access to grouplessons can not view the schedule at all. Originally, I planned on discriminating between subscriptions only after members requested to enroll for a class, however I decided to deny them access to the schedule at all. Designwise I thought this would make more sense because someone who chooses to subscribe for a non-group lessons programme, has no benefit in having access to the schedule at all. 

Members with access to the grouplessons can enroll for classes, but in constrast to the original proposal can not unsubscribe for grouplessons they enrolled for. This was a time-related decision; implementing this feature would be largely alike implementing the option to enroll for classes, therefore I chose to focus on other more distinct features of the web application.

Lastly for the calendar, it is not possible for personnel to check which members are enrolled for certain grouplessons. This decision was mainly due to changing to a different framework for the calendar function during the project, which costed a lot of time. This feature was the final one I planned for the calendar function and because I had spend so much time to this already, compared to other even so important aspects of the web application, I decided to not implement this after all. Others I discussed this with agreed that it would have been nice to add this feature to the calendar, but they also recognized the improvement to the other calendar functions which resulted from choosing a different calendar framework, which let me to conclude that this is a reasonable tradeoff to make.

### Webshop 
For the webshop there is an adjustment in functionality for users who are not a member of YourGym. Though they can visit the webshop, they will be prompted to login or register as soon as they try to add an item to their shopping cart. This decision was largely based on time-constraints, but also because I came across some other more interesting features to add to the webshop. I discussed this with others who agreed that the other functions, which will be discussed next, were to be prioritized over the current one.

One of the extra features for the webshop, is the generation of a payment through the services of Mollie, which is a legitimate payment handler which can be used in testmode, as I did for the current project. When placing an order, the user is redirected to the mollie interface where they can indicate the status of their payment. If the payment succeeds, their order will be finalized, otherwise they have the option to return to their shoppingcart and try again. Someone else suggested using mollie and already while implementing I myself and others who gave feedback were very enthusiastic about this feature, because it is very real and instantly makes the webshop look like a real one.

Lastly, personnel can add new items to the website through a form on the website. Though this would also be possible through the django user admin, I wanted to gain some experience in using DocumentForms and uploading images to a website. Furthermore, it is more user friendly for the user to do this via the website since this interface can be adjusted and users are redirected to the webshop after adding a new item, which makes the process outcome instantly visible. Unfortunately, I did not have time to enable this for all information personnel might want to update, such as grouplessons for the calendar which still need to be added through the admin. Ideally I would implement this functionality for all models (where needed) and include an option to remove or adjust objects.
