# Special Olympics Ontario By IamJim

### Description
---------------------------------------
Our client (Special Olympics Ontario) would like a way to keep track of their user (athlete) and events data in order 
to utilize these data for event-planning. Unfortunately, the application that they have is not only limited in search 
function, but also inconvenient to use. Their current application only allows user to look up one single competition at 
a time. This may be frustrating to the user if they want to compare results from different competitions. Additionally, 
the search result shows the competition data in table, which may be difficult to comprehend if one is not familiar with 
using the application. We hope to create a more user-friendly application with graphics that can display the results in 
a more comprehensible way, so that the staff and athletes of Special Olympics Ontario may organize and view their data 
in an all-encompassing/holistic way.


Our product/application hopes to solve this problem for our client by:

1) Allowing them to query the required data across both/all databases using a single query or interface.
2) Allowing them to query the required data across multiple competitions and display the respective results.
3) Display the queried data in an intuitive and user friendly format, especially for people with learning disabilities. 
4) Provide relevant data visualizations that give a graphical representation of the queried data making it easier to 
understand.  

### Basic/Key Features
- Our application supports the viewing of athlete and team profile pages, as well as dedicated sports pages. Once an athlete/team is found, or a sports page is reached either by using the search functionality, navigation, or directly entering the URL, the user is redirected to the respective athlete, team or sports page. The page displays the relevant data such as basic infromation. Furthermore, it displays detailed relevant statistics and even contains graphs and plots to give a visual representation of data.  

- Our application supports a basic search functionality which is limited to athletes and teams. It allows a user a to search for either teams or athletes based on a string entered in the search box. The entered string is matched with the athlete or team names and the appropriate teams/athletes are displayed in list format. The user can then select the athlete or team he/she was searching for it is valid and found.

### Searchable Athletes and Teams
Searchable Athletes:
- April Andrews
- Harry Holmes
- Lisa Lowe
- Oliver Owens
- Paula Parker
- Russell Reed
- Sam Sanders
- Sharon Smith
- Tess Trojan
- Walter Wood

Searchable Teams:
- Mississauga
- Toronto

### Instructions/User Guide
Our product is an web application deployed to web using Heroku for cloud hosting. Thus it is publicly available for access and testing. In order to access or test the web app one simply needs to visit the URL: http://www.csc301-soo.tk:5000/. When visiting the URL, the user will be redirected to the home/landing page of our web application. On the home page, the user will have access to the navigation bar on the left hand side of the screen (on desktop) and the main contents of the home page on the right. 

- In order to view an athlete profile, the user must know which athlete he/she is looking for by name. The user can then use the search functionality to find the athlete. In order to find an athlete, the user must select the link to the search functionality page from the navigation bar on the left. This will redirect the user to the search page where he/she can select "Athlete" as the search option, enter the name of player he/she is searching for and press the search button. The user will then be shown a list of atheletes matching the search term and he/she can select the desired athlete. Once selected, the user will be redirected to a dedicated athlete page where he/she will be able to see all the data pertaining to the athlete - everything including basic information, detailed statistics as well as interactive plots and graphs. 

- In order to view a team profile, the user must know which team he/she is looking for by name. The user can then use the search functionality to find the team. In order to find a team, the user must select the link to the search functionality page from the navigation bar on the left. This will redirect the user to the search page where he/she can select "Team" as the search option, enter the name of team he/she is searching for and press the search button. The user will then be shown a list of teams matching the search term and he/she can select the desired team. Once selected, the user will be redirected to a dedicated team page where he/she will be able to see all the data pertaining to the team - everything including basic information, detailed statistics as well as interactive plots and graphs. 

- Unlike the athlete and team pages, in order to view a team page, the user does not have to use the search functionality to find and view the page. Instead, for the sports page, the user simply needs to select/click on the "Sports" link from the navigation bar on the left. This will redirec the user to a intermediary sports page which has a listing of all the sports by category - summer and winter. The user will visually be able to see the available sports - and select the one he/she is searching for. Once selected, the user will be redirected to a dedicated sports page where he/she will be able to see all the data pertaining to the sports - everything including basic information, detailed statistics as well as interactive plots and graphs. 
