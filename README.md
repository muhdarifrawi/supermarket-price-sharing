# Price Share
Price Share is a fictious platform where users can submit prices of items they may have came across or bought during their shopping trip. From there, other users can look for good deals that they might have missed out on. For ease of use, the platform adopts a minamilistic approach to design. 

## Getting Started

This application has been deployed to Heroku where you can find by clicking here. This application would not run proper as a github deployment. Also, I have yet to find a way to run the file locally after downloading from the repository. If you happen to know how, feel free to run it. 

## UI/UX

Users who potentially might use this often would be someone in their 30s or 40s. Here in Singapore, often times people above this age would lookout for great deals. They are known to be quick on their feet when it comes to getting great deals. 

So with that in mind, the navigation should be easy for them to understand and quick to jump from one page to the other. It shouldn't clutter either as it would make them confused and frustrated.

## Technologies

Coding Languages: HTML/CSS, JavaScript, Python

Framework: Flask

Database: MySQL with phpMyAdmin

## Wireframes

![Entity Relationship Diagram](https://github.com/muhdarifrawi/supermarket-price-sharing/blob/master/wireframes/Project%203%20ER%20Diagram.png)

![Logic Data Diagram](https://github.com/muhdarifrawi/supermarket-price-sharing/blob/master/wireframes/Project%203%20Logic%20Diagram.png)

## Features

Users would be greeted by an index page. It consists of a few things. A jumbotron with a "Contribute" button. A top Navbar with the Price Share logo, "Home" link, "Submit" link, "Prices" link and "Search" link. Two images each labeled "Submit a form" and "See prices". 

Clicking on the "Home" link would bring them back to the index page. CLicking on the "Submit" link, the Jumbotron's "Contribute" button or the image labelled "Submit a form" would all lead user to the forms page. There they would have to key in their preferred Username, the supermarket they went to, the location of the Supermarket, the address then followed by the brand, item name and price of the item. These fields are mandatory to fill. clicking submit will lead them to the "Thank You" page and from there they can either click on the "Submit form" or "See prices" button. "Submit form" would lead them to the forms page and "See prices" would lead them to the tables page.

From the index page, if the user chose to click on the "prices" link or the image labeled "See prices", they would be lead to the tables page. Once there they would see the entries made by them or other users. On the right most of the entry, there would be an edit and delete link. Clicking on edit would lead them to the edit page where they can revise the item name, cost, supermarket and their username. These fields are mandatory to be filled. If they are satisfied, they can press submit and the application would update their changes. They can click on cancel if they don't wish to update and there would be no changes made. Clicking on the delete link would lead them to the delete page where they can either press confirm where the entry would be removed completely or they can cancel the deletion. 

The search link would lead them to the search page where they would see a "Search by" dropdown list consisting of Items, Supermarket and User. They would have to select one option and key in the search term they wish to look up. It would then return the results in a table format similar to the prices page.

## Testing

###### The navbar:
- Clicking on each of the links should lead them to their respective pages. "Home" should lead users to the landing page. "Submit" leads them to the form submission page. "Prices" would lead them to the price table page. And "Search" leads them to the search page. Each of the links works as described. 

###### Home/landing page: 
- Users would be greeted with a jumbotron and two small images at the bottom of it. All images loads but the images loads slow. On the jumbotron iteself, there is a "Contribute" button. This button when clicked, leads users to the form submission page. This function is working as intended. 
- At the bottom left of the jumbotron, an image with the label "Submit form". When clicked, leads users to the form page. There are no issues with it. 
- At the bottom right of the jumbotron, an image with the label "See prices". When clicked, leads users to the table page. 

###### Form page: 
- Users would see a form with 7 input boxes. They are to key in their preferred Username, the supermarket they went, the location, address, brand of the item, the item name itself and finally the price. These input boxes are all mandatory to be filled and are checked by bootstrap's "required" field class. 
 - The input field for brand though has a javascript that autosuggests the brand names. These are codes borrowed from W3school and altered to suit the purpose of the application. More info on it can be found on the [acknowledgements section](https://github.com/muhdarifrawi/supermarket-price-sharing/blob/master/README.md#acknowledgements). This input field is made to ease the fetching of information from the database. However it is not perfect and more could be done. One issue with it that was found was that the autocomplete leaves out the apostrophes when user selects their choices. This causes confusion in the database. 
 
 Here is a short gif of it that explains better:
 ![Autocomplete Issue](https://github.com/muhdarifrawi/supermarket-price-sharing/blob/master/wireframes/videos/Autocomplete%20Issues.gif)
 
 ###### Prices page: 
 - Prices page shows the table of the database. 
 - Each line of entry has each own edit and delete links. 
 - Clicking on the edit would lead to the edit page where users can edit their entry. One of the issues that was found quite late into programming this was that the item names and supermarket names were not appearing in full. Other than that, the confirm and cancel buttons were working. 
 - The link to the deletion page was working. User is able to delete their entry from the front-end. However, at the back-end, the data was not completely erased. Only the itemcost table was cleared hence why the data was not appearing on the front-end. 
 
 
 
 ## Acknowledgements
 
 Raw Code can be found here:
  [js autocomplete by w3school](https://www.w3schools.com/howto/howto_js_autocomplete.asp). 
