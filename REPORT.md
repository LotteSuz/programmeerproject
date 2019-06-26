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
Important changes in the 
• personell cant check who enrolled for classes
• cant order with guest account
• cant unsubscribe
• non group subscr cant see the timetable
