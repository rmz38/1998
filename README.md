# 1998
# Cornell CS Wiki
## 1998 final project

##### Explore tech gig easier on campus

![Image description](1234.png)

##### Description

Cornell Wiki enables non CS and entry level CS studentto search for related resources
that they are curious about Cornell.

##### Important features

Search and Display - get spercific classes, faculty and research on campus;

It has a general search page, a filter page and a favorite page.

General search: Search anything by keyword
Filter system: Search courses by credits, requirements, etc.
Favorite: Add anything interested

##### Purpose and features

A list of how your app addresses each of the requirements (iOS / Backend)

iOS

The iOS portion of the project must contain the following components that have learned in class:
AutoLayout using NSLayoutConstraint or SnapKit
At least one UICollectionView or UITableView

UI CollectionView used for filtering courses

Some form of navigation (UINavigationController or UITabBarController) to navigate between screens

UITabBarController used for switching between the three pages.

Integration with an API - this API must provide some meaningful value to your app. For example, if you’re creating a music app, you could use the Apple Music API. Most of you will integrate with an API written by students in the backend course.

API for searching the course.

##### Backend

The Backend fulfills our iOS client's needs by servicing GET requests for information, which can provide all classes, all research belonging to a class, and all faculty teaching a class. It can also return specific research by id and specific faculty by id, allowing all faculty and research to be displayed in the app.

The backend is delpoyed through Docker Compose, and can be accessed through to the front end.The original plan is using the backend from Cornell Class Roster API, due to the limit of the time, the data API did not get connected, but could be delpoyed in the future. 


