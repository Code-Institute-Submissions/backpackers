# Backpackers

Stream Three Project: Data Centric Development - Code Institute.

The project Backpackers was built using the Flask Microframework,this is an application that helps you to find tourist spots in ireland. You can also share an experience
from a spot. 

### Demo

A live demo can be found [here](https://app-backpackers.herokuapp.com/).

### Technologies

+ Flask Microframework (Python)
+ MongoDB (NoSQL Database)
+ Materialize
+ JavaScript
+ jQuery
+ HTML
+ CSS


### UX

I have greate interest in travelling and site seeing, the idea about this project came from this interest. 

The project basically have 3 pages, Home page, Add a spot and find a spot. There is also About which is a model. And all these three are displayed in nav bar. This project use MongoDB for data storage. Also the stylings are done with Materialize.

The Home page contains a search bar which is a select drop-down list with options to select a county name and a button. by selecting a county and pressing the button you can find spots from that county.
The spots are displayed as card reveal, that is it displayed more details when you click on it. the card contain an image of the spot, its name, place name, county, an edit button in which displays an edit page in which we can edit the details about the spot.The edit option is available only in Desktop and tablet, in mobile the edit button will not be displayed. You can change an existing image and add another. On clicking the card 
more details about the spot can be viewed, activities that can be done in this spot will be shown.

In Add a spot page you can add a spot, with its name, place name, county, you can give a discription about the spot, things to do in the spot can be added, you can add an image and also rate the spot as per your experience.
All the fields in this page are required to add a spot, when you add a spot you will get an email from the application thanking you.

In Find a spot page you can search a spot by spot name, place name, by county and also by things to do. 



Only Admin can delete a spot. No delete option is allowed in frontend.

### Features

+ MongoDB is used to store all the data about the spots.
+ This application displays all the spot details as cards.
+ The application has an effective searching options.
+ The application is responsive in all screen size.
+ The application sents emails to those who added a spot thanking them.

#### Features Left to Implement

+ The application must enable to add more images and should show a gallary for all spots.
+ The application must spot all the tourist location in a map, Also it should allow to locate it when the spot is added.

### Testing

All the testing for this application was done manually. 

#### Links

All the links included in the website have been tested and they are all working.

#### Effects

Hover effects on icons, links and cards have been tested and they all have a hover effect working as expected.

#### Responsive 

The website have been tested in different viewports and it is responsve.

#### Data Base

MongoDB is used to store data, I had tested that the data is been storage in the expected collection and this is working.
 
 + The spot can be successfully added.
 + The spot can be successfully updated.
 + we can also search for spots.
 
#### Email

The feature has been tested and it is sending the email correctly.


##### Known Issues

The email sending shows google authentication errors sometimes when adding, even though I have turn on less secure access. But spot will be added.

### Deployment 

The Backpackers application is deployed using Heroku and GitHub.


### Credits

##### Media 

All images and contents have been obtained through different searches through [Google](www.google.com) and [Wikipedia](https://en.wikipedia.org/wiki/English_Wikipedia).


