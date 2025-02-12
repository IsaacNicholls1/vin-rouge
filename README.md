
# Vin - Rouge

This Website was built by Isaac Nicholls for Code Institute Final project for the 16 week Bootcamp - Full Stack Development for the AI Augmented Developer. The brief for the project was a full interactive website, with bpth front and back end server, using the Django/Python framework. Full CRUD functionality was required. After some research and brainstorming/mindmapping I had idea of a wine review website, specifically for French wines. This is something that interests me, and after living in France for 10 years it is something i have a passion and knowledge for. This helped to design the site, and create user stories and my project board.   

👩🏻‍💻 Here is an example of this website and its homepage ![Am I Responsive](static/images/responsivehome.png)

Link to deployed and finished site: https://github.com/IsaacNicholls1/vin-rouge

---

## CONTENTS

* [Project](#project-goals)

* [Planning](#planning)
  * [Wireframes](#wireframes)
  * [Agile](#agile)
* [Features](#features)


* [Ux-Ui](#ux/ui)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Fonts](#fonts)
  * [Logo](#logo)

* [Testing](#testing)
  * [Acessibility](#accessibility)
  * [Responsivity](#responsivity)
  * [Device Testing](#device-testing)
  * [Testing Breakdown](#testing-breakdown)
  * [Testing User Stories](#testing-user-stories)

* [Known Bugs](#known-bugs)
  * [Deployment](#deployment)

* [Sources](#sources)

  * [Future features](#future-features)
  * [Acknowledgments](#acknowledgments)

- - - -
# Project Goals #
## 1. User goals

- The users goal is to discover and explore detailed reviews of various French wines.

- The users goal is to being able to navigate the website quickly and efficently to our content.

- The users goal is to Share personal wine reviews and ratings to help other users make informed choices.

- The users goal is to Connect with other wine enthusiasts to discuss and share recommendations. 
    
## 2. Site Owner Goals
- The site owner goal is to ensure a smooth and seamless user experience by maintaining a robust and responsive website.

- The site owner goal is curate and moderate user-generated content to maintain high-quality and reliable reviews.

- The site owner goal is to analyse user data and feedback to continuously improve site features and functionality.

----


# Planning

## Wireframes

 - Wireframes were created with Balsamiq to create clear, visual layouts of the site's design. It helped in identifying potential issues and refining the user interface early on, ensuring a more seamless user experience.
 - The wireframes were developed at the start of the project and then worked on as I went through, to tweak the changes I made to the design and feel of the site

![wfhome](/static//images/wireframehome.png)
![wfwines](/static/images/wireframewine.png)
![wfabout](/static/images/wireframeabout.png)
![wfcontact](/static/images/wireframecontact.png)
![wfwdetail](/static/images/wireframewd.png)


## Agile 
- Agile methodology is "a set of methods and practices where solutions evolve through collaboration between self-organising, cross-functional teams"
- A project board was set-up to keep track of user stories. Each user story was assigned a 'MoSCoW' prioritisation (must have, should have, could have, won't have) tag. 

## GitHub project planning
- I used a GitHub project board to assist me in planning and carrying out tasks related to my user stories. This approach allowed me to enter all user stories into the project board, where they could be easily assigned and labeled. The GitHub project board provided a clear overview of the tasks, helping me to prioritize, organize, and track progress efficiently, ensuring that all user stories were addressed systematically and effectively. 

The board can be found [here](https://github.com/users/IsaacNicholls1/projects/12).

## MOSCOW Prioritisation 

- In order to effectively utilise the MoSCoW prioritization method, I ensured that my project issues board in GitHub was actively used. This provided a comprehensive overview of the issues related to my user stories, allowing me to categorize and track them efficiently. The GitHub issues board enabled me to organise tasks, monitor progress, and verify completion, ensuring that I addressed our Must-Haves, Should-Haves, Could-Haves, and Won't-Haves systematically and effectively.

![moscow](/static/images/MOSCOW.png)

- - - -

# Features #


### Background Javascript
- I added a modal to the site so that when users first enter the site, they get a pop down modal to ask if they are over 18 or not. I felt this was important to my site as it protects minors and adheres to laws and respolsibilities. This was performed using Javascript. 

- ![Home Page screenshot](static/images/modal18.png)

## Intro page and CTA button
- The homepage is the main landing page of the website, which provides some info on the site, a nice welcoming feel and a cta button to take you through to the next stage of the site, the wines.  
- ![Home Page screenshot](static/images/homepage.png)

### Registering
- In the header, if you are not already logged in, you can press the 'Register' button which will take you to the registration page.
- ![Register screenshot](static/images/signup.png)

### Logging in
- In the header, if you are not already logged in, you can press the 'Login' button which will take you to the log-in page.
- ![Log-in page screenshot](static/images/signin.png)
- ![Log-in page screenshot](static/images/signinsuccess.png)

### Logging out
- In the header, if you are logged in, you can press the 'Logout' button which will take you to the log-out page.
- ![Log-out page screenshot](static/images/signout.png)

### The admin panel
- Accessible only by the superuser, the admin panel is where the Wine review Site owner can create reviews and approve user-submitted reviews.
- User reviews are sorted based on approval status, with unapproved reviews displayed at the top for easy identification by the superuser.
- - ![Admin panel screenshot](static/images/admin.png)

## Wine Page
This is the page where I want users to navigate to, they can see all the posts about wines, the different wines and sort them into categories. They can nagivate to their favourite wines and leave reviews and comments. 
- ![Wines screenshot](static/images/winespage.png)

### User review/comment
- At the bottom of each Wine review, there is the opportunity for users to leave their own comments and ratings on that location. Users simply type their comment in the text box, select their rating and then press submit and it will be added with a "This comment is awaiting approval" message. A message box will also pop up at the top of the page to provide feedback to the user. 
- ![User review screenshot](static/images/comments.png)
- ![Feedback screenshot](static/images/leavecomcinfirm.png)

### Editing a user review
- If you want to edit your own comment, you can press the edit button which will open the edit page in a new tab. You can then edit your review and it will be updated. 
- - - ![Edit screenshot](static/images/editcomment.png)
- - - ![Edit confirmation screenshot](static/images/editconfirm.png)

### Deleting a user review
- If you want to delete your own review, you can press the delete button which will delete your comment and a confirmation message will pop-up.
- - ![Delete screenshot](static/images/deletecomment.png)
- - ![Delete confirmation screenshot](static/images/deletecommentconfirm.png)

## About Page
This page features some information to the user about the site, and a short form where users can register and receive a newsletter from the site admin. 

## Conatct Page
This page is there so that users have the opportunity to send in their own wine review, which is recieved into the admin panel, can be moderated and uploaded by the admin/superuser. 

## Header and Footer
The header and footer have been kept the same throughout the site - styled simply with the same font from Font awesome and the spacing and colours all the same. 

## Database
- I used Code Institute's PostgreSQL database.

### Database planning
- I used an Entity Relationship Diagram to plan my database.
- ![ERD diagram](/static/images/dbdiagram.png)

### How to create a database
1. Navigate to [PostgreSQL](https://dbs.ci-dbs.net/) from Code Institute.
2. Enter your student email address in the input field provided.
3. Click Submit.
4. Wait while the database is created.
5. Check your email.
6. You now have a URL you can use to connect your app to your database.

<hr>
<p><a href="#contents">🍷Back To Top🍷</a></p>

- - - -

# UX/UI #

   ## Purpose and Intended Audience

   -The purpose of Vin Rouge is to create a comprehensive and user-friendly wine review platform. This site is designed to help users discover, review, and share their experiences with various French wines, leveraging Django and Python for robust backend support and smooth user interactions.

   - Intended Audience: Vin Rouge is intended for wine enthusiasts, connoisseurs, and casual drinkers who appreciate French wines. The platform aims to serve both seasoned wine experts looking for detailed reviews and newcomers seeking recommendations and insights into the world of French wines.
 
  
 ## User Stories
  - User Story: As a registered user, I can log in to my account, so that I can access personalized features and leave reviews.
  - User Story: As a logged-in user, I can leave reviews on different wines, so that I can share my opinions and experiences with others.
  - User Story: As a logged-in user, I can comment on wine reviews, so that I can engage in discussions with other users.
  - User Story: As a user who has previously left a review, I can edit/delete my comments.
  - User Story: As a superuser, I can access the admin panel, so that I can manage the website's content and user activities.
  - User Story: As a superuser, I can validate or reject user comments, so that I can ensure all reviews meet community guidelines.
  - User Story: As a superuser, I can add posts to the website, so that I can share important updates and information with users.
  - User Story: As a superuser, I can manage user accounts, so that I can handle user-related issues and enforce website policies.
  - User Story: As a website visitor, I can sign up for the newsletter, so that I receive updates and information about new reviews and content.
  - User Story: As a website visitor, I can access the website on a mobile or smaller screen device, so that I have a seamless and user-friendly experience regardless of the device I'm using.
  - User Story: As a website visitor, I can search for wines, so that I can quickly find reviews and information on specific wines.
  - User Story: As a registered user, I can add wines to my favourites list, so that I can easily access my preferred wines later.
  - User Story: As a new visitor, I can register for an account, so that I can access personalised features and leave reviews.
  - User Story: As a site admin, I want to implement an age confirmation feature to ensure compliance with legal drinking age regulations and protect underage visitors.
  
<hr>
<p><a href="#contents">Back To Top</a></p>

- - - -

 ## Design
 
 ##  Colour Scheme

 - I selected a palette that balances elegance and approachability, reflecting the sophistication of French wines and the inviting nature of Vin Rouge. Pastel green offers a fresh, soothing backdrop that complements the rich, deep hues of wine colors like merlot and burgundy. Light gray adds a modern, clean touch, ensuring the overall design is sleek and visually appealing, enhancing the user's experience while exploring wine reviews.

 **Coolers**
![Colours](/static/images/coolers.png)
 
 ##  Fonts
 -  I chose Libre Baskerville as my font, as it was a common font used on other wine sites, and also used on many wine bottles. It also has good readability. 

 ![Font](/static/images/font.png)
 
    
<hr>
<p><a href="#contents">🍷Back To Top🍷</a></p>

- - - -


# Testing #

## Manual testing
- Manual testing was carried out on the local and deployed sites.

![manualtesting](/static/images/manualtesting1.png)
![manualtesting](/static/images/manualtesting2.png)

## HTML Validation
- Initial HTML Validation was performed using the W3C Mark up service and the results can be found in this document. 
- There were two small errors with stray tags, and a span class not closed properly which were dealt with. 

![html1](/static/images/html1.png)
![html2](/static/images/html2.png)
![html3](/static/images/html3.png)
![html4](/static/images/html4.png)
![html5](/static/images/html5.png)

  
## CSS Validation
- W3C CSS style sheet validation link 
![Css1](static/images/cssvalid.png)

## JS Validation
![JS](static/images/jsvalid1.png) 
![JS](static/images/jsvalid2.png) 
![JS](static/images/jsvalid3.png)

### Python validation
[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the python files I created or edited myself.
- Flake8 was used during production, which meant no errors were present wheh it came to testing at the end, this was a brilliant tool to use during productionb and sped the process up, whilst adhering constantly to PEP8 standards. 

![Python](static/images/blogadminpy.png)
![Python](static/images/blogformspy.png)
![Python](static/images/blogmodelspy.png)
![Python](static/images/blogurlspy.png)
![Python](static/images/blogviewspy.png)
![Python](static/images/aboutadminpy.png)
![Python](static/images/aboutformspy.png)
![Python](static/images/aboutmodelspy.png)
![Python](static/images/abouturlspy.png)
![Python](static/images/aboutviewspy.png)


## Accessibility / Lighthouse
 - I tested the page with lighthouse and the accessibility and performance scores are shown below
![lighthouse scores home](/static/images/lighthousehome1.png)
- I resized the image after this test, and used tiny.pg to reduce the size which gave me a better score and allowed the page to load quicker. 
![lighthouse scores home2](/static/images/lighthousehome2.png)
![lighthouse scores wines](/static/images/lighthousewines.png)
- The wines and winde detail pages scored low in the best practices, this seemed to be due to the cloudinary files not producing https files. This is something to edit and work on for the project. 
![lighthouse scores winesdetail](/static/images/lighthousewinedetail.png)
![lighthouse scores about](/static/images/lighthouseabout.png)
![lighthouse scores contact](/static/images/lighthousecontact.png)
 

## Responsivity
- I tested the site's responsiveness using multiple devices, including desktops, tablets, and smartphones, to ensure a consistent user experience. By leveraging browser DevTools, I was able to simulate various screen sizes and resolutions, identifying and resolving potential layout issues. Additionally, I conducted real-world testing on physical devices to validate the site's functionality and appearance across different platforms.


![Am I Responsive home](/static/images/responsivehome.png)
![Am I Responsive wines](/static/images/responsivewines.png)
![Am I Responsive about](/static/images/responsivewd.png)
![Am I Responsive about](/static/images/responsivecontact.png)
![Am I Responsive about](/static/images/responsiveabout1.png)

## Device Testing

I tested the site with the following devices:

- Android Google Pixel 8
- Desktop
- Chrome Developer Tools (Simulating for all available device options)
  
## Browser Testing

Testing has been done on the following browsers:

- Chrome (& Developer tools)
- Safari
 
  <hr>
<p><a href="#contents">Back To Top</a></p>\


## Testing user stories

I tested my site vs the user stories: 

1. 
User Story:
![User story1](/static/images/userstory1done.png)

--

2. 
User Story:
![User story2](/static/images/userstory2done.png)

--

3.
User Story: Please see future implementations

--

4.
User Story:
![User story4](/static/images/userstory4done.png)

--

5. 
User Story:
![User story5](/static/images/userstory5done.png)

--

6.
User Story:
![User story6](/static/images/userstory6done.png)

--

7.
User Story:
![User story7](/static/images/userstory7done.png)


--

8.
User Story:
![User story8](/static/images/userstory8done.png)


--

9.

User Story:
![User story9](/static/images/userstory9done.png)

--

10.
User Story:
![User story10](/static/images/userstory10done.png)

--

11.
User Story: Please see future implementations

12.
User Story: Please see future implementations

13.
User Story:
![User story14](/static/images/userstory13done.png)


<hr>
<p><a href="#contents">Back To Top</a></p>
--

## Known Bugs


### Bugs/Issues during production

- Admin panel bugs, throughout the project I encountered many bugs from the admin panel connectiong to my code, which often thre up errors which were often Integrity errors, these I had to assess, work my way through and solve at the time. Usually i used co-pilot to solve these errors, and although many of them took some time to fix I was always able to get through and solve them myself. 

- Comments not working - My comments section was not working for a while, which was due to my models not linking up correctly with the views.py and urls.py. To fix this again i used co-lpilot to assist me, and also spoke to my Coding coach Roo who was able to point me in a direction of where to look and useful documentation to use. 

### Poor Font for User

- I felt that the font had to be just right for the website feel and the user, and after some testing I found the perfect one which was not my first option. I tested a few and eventually settled on one which was correct in style and feel for my site. 

### Responsiveness

- Responsiveness issues were encountered with the header, with the dropdown menu changing when changed to a smaller device. This was dealt with at the time.


## During development and testing, these are the current bugs:

### Images  

- Some of the images are still too large - generating a lower lighthouse score than I would have liked, with more time I would have liked to edit these to make sure everything was as high as I could make it, therefore giving a better user experience all round. 

### Unknown code fixes in lighthouse

- I have identified some errors and warnings in Lighthouse that could enhance the score. To address these, I will conduct thorough research before future projects to understand and resolve the issues. This proactive approach will help ensure my site meets high performance standards.
- Images could have been resized, which would have helped the performace score in lighthouse, with more time i would have edited these using tiny.pg to update the score. 

<hr>
<p><a href="#contents">Back To Top</a></p>


- - - -


# Deployment #

The site was deployed to Heroku. The steps to deploy are as follows:
 - Install the gunicorn python package and create a file called 'Procfile' in the repo's root directory
 - In the Procfile write 'web: gunicorn vin-rouge.wsgi'
 - In settings.py add ".herokuapp.com" to the ALLOWED_HOSTS list
 - In settings.py add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS list, git add, commit and push to github

Navigate to the Heroku dashboard
 - Create a new Heroku app
 - Give it a name and select the region 'Europe'
Navigate to settings tab and scroll down to Config Vars
 - Click 'Reveal Config Vars'
 - Add the following keys:
         key = DATABASE_URL | value = (my secret database url)
         key = SECRET_KEY | value = (my secret key)
Navigate to Deploy tab
 - Connect to GitHub and select the repo 'vin-rouge'
 - Scroll down to 'Manual deploy' and select the 'main' branch
 - Click 'Deploy Branch'

Security Measures:
Sensitive data is stored in environment variables.
DEBUG mode is disabled in the production environment to enhance security.




 ### Cloning
- To clone a GitHub repository:
1. On GitHub.com, navigate to the repository you want to clone.
2. Click the "Code" button (found above the list of files).
3. Copy the URL for the repository.
4. Open Git Bash or your chosen terminal.
5. Navigate to the directory where you want to clone the repository.
6. Type: git clone - github repository
7. Press Enter to create your local clone.

<hr>
<p><a href="#contents">Back To Top</a></p>

- - - -

# Sources #

### Languages Used

- Languages used
- HTML5

- CSS

- JavaScript

- Python
   - asgiref==3.8.1
   - cloudinary==1.41.0
   - dj-database-url==0.5.0
   - gunicorn==20.1.0
   - oauthlib==3.2.2
   - psycopg==3.2.1
   - PyJWT==2.9.0
   - python3-openid==3.2.0
   - requests-oauthlib==2.0.0
   - sqlparse==0.5.1
   - urllib3==1.26.19
   - whitenoise==5.3.0

- Django

   - summernote==0.8.20.0
   - allauth==0.57.2
   - crispy-forms==2.3

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
   - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/specimen/Libre+Baskerville?selection.family=Monoton|Orbitron:wght@400..900|VT323&query=libre+bas)
3. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
4. [jQuery:](https://jquery.com/)
   - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
5. [Contrast Finder](https://app.contrast-finder.org/?lang=en)
        - Contrast Finder was used to check the contrast between text colour and background image
6. [Tiny.PNG](https://tinypng.com/)
        - Tiny.PNG was used to compress images
7. [W3 Schools](https://www.w3schools.com/)
        - used to look up syntax for HTML and CSS
8. [Co-Pilot] (https://copilot.microsoft.com/)
   - Used extensively for help with coide, script and de bugging processes. An invaluable tool.  
9. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the wireframes during the design process.
10. [Git](https://git-scm.com/)
        - Git was used for version control
11. [GitHub:](https://github.com/IsaacNicholls1/vin-rouge)
   - GitHub is used to store the projects code after being pushed from Git.
12. [W3 Jigsaw](https://jigsaw.w3.org/css-validator/)
        - used to validate the CSS
13. [JSHint](https://jshint.com/)
        - used to validate the JavaScript
14. [W3C HTML validator](https://validator.w3.org/)
        - used to validate the HTML
15. [Python Enhancement Proposals](https://peps.python.org/pep-0008/)
        - for advice on PEP8 compliance
16. [Django framework](https://www.djangoproject.com/)
17. [Heroku](https://dashboard.heroku.com/apps) - for deployment. 
18. [Pexels](https://www.pexels.com/)
        - for copyright free images


## Media and Content
  
 - The following photos were used in the content: (https://github.com/IsaacNicholls1/vin-rouge/tree/main/static/images)
- Font awesome was used to add icons for UX purposes auch as social media icons. 
- Balsamiq was used to create the wireframes during the design process, as this was the second time of using the tool it took a bit of getting used to and developing these. We tweaked them as i went along and made slight changes to the actual site. 

## Code
- The HTML & CSS uses Bootstrap Version 5.3: https://getbootstrap.com/docs/5.3/getting-started/introduction/ 
- I used other coding tools and resources such as snippets of code from our previous CI projects to guide and aid when we needed reminding about the correct way to use the code. 
- The CI walkthrough project 'I think therefore I blog' was used to refer back to to give help during the process. When stuck or needing some advice my first check was with my walkthrough project and the documentation on the LMS learning portal of previous lessons. 
- Co-pilot in VS code was a very valuable tool in helping to develop code for my project, but also is the fixing, testing and troubleshooting of my code.
- For reference i looked at a couple of example projects which were provided to me by our tutor, these projects were : 
- https://github.com/alexcurnow96/Task-Nest-Project  - Readme advice. 
- https://github.com/elamont174/ey-up-me-pup  - for code examples and Readme advice. 
- Pexels was used to get some photos, alongside photostock and google images and others were produced by AI generators.  


# Use of AI #

## Co-Pilot

- Throughout this project, I extensively utilised Copilot to enhance development and streamline testing. As this was my first experience with AI tools on such a scale, I found Copilot to be an invaluable collaborator throughout the entire process.
- Using Copilot throughout this project has been invaluable in several ways. Copilot has provided detailed, step-by-step guidance, which has been crucial in resolving technical issues related to Django migrations and database schema.
- It has also offered design feedback, helping to ensure that the review form on the wine detail page is both user-friendly and visually appealing.


## Code Creation & other uses

- By utilising question-and-answer prompts and multi-step instructions, I was able to generate a good initial draft for my test cases. I could then refine these to better match the project's requirements. 

- The iterative back-and-forth with Copilot felt like having a knowledgeable pair programmer by my side. This collaboration made me more thoughtful about how I structured my prompts, as clearer questions led to better answers.

- Throughout the project's development, Copilot also served as an invaluable debugging and problem-solving tool. Whether I encountered specific error messages or stumbled upon unexpected issues, Copilot provided insightful suggestions that greatly expedited the troubleshooting process. Its ability to offer solutions, based on context, helped me overcome roadblocks efficiently, saving me both time and effort.

- Copilot significantly contributed to the development of my site's front end by providing efficient code suggestions and auto-completions, which streamlined the implementation of interactive features and responsive design elements.

- Copilot's ability to generate ideas and offer alternative solutions has fostered continuous improvement, making the development process more efficient and effective. Overall, Copilot's support has significantly contributed to the project's success by enhancing both the technical and user experience aspects.
- I found it very useful overall and saved me a great deal of time, however I found when using it, it needed a close eye kept on it as it sometimes adds in extra closing tags and code that is sometimes not needed. 

- Co-pilot helped in the testing and de-bugging of my code, when running through validators it was very helpful as any small code issues were picked up on straight away and i could deal with them quickly and efficiantly because of this tool. 



- - - -

# Future features #

 ## Search Facility ##

- Something I would have liked to add to my site to improve functionaloty and user experience, which i ran out of time for was adding in a serach bar, to quickly access any part of the site that the user required. I did all the research for this using co-pilot, so I have the documentation of how to implement it, unfortunately i didnt get the chance to add this into my site. 
- User Story 11: Searching Wines
   ![User story11](/static/images/userstory11.png)

 ## Filters Menu ## 
- I would have liked to implement a Filters menu on my wine page, I feel this would have added great functionality to my site and better UX. Providing users with the option to filter their wines by region, grape variety and rating. Again all the research was done using co-pilot, but unfortunately I wasn't able to implement it on my site. However I plan to add this to my portfolio site. 

 ## Profile Page and Favourite Wines ##
- In relation to my user story 12, I would like in the future to add a user Profile Page which the user can access, populate with their personal data and also to be able to choose favourite wines which they can 'like' and they will get added to their profile. This would provide my site users a great space to store their favourite wines, allowing for the greater UX and also a better experience overall on the site. 
 - User Story 12:
   ![User story12](/static/images/userstory12.png)

 ## Ratings system ## 
- I currently have a ratings system available for each review and users can give their own rating out of 5 in the comments, however i would like to develop this further in the future to add in functionality that would tally up each wines ratings and give an average score for that wine. This would allow users to see which wines have scored highest when they are looking and searching for their favourite ones.  

## Region Model ##

- My original thought was to include a region model, to make it easier for users to differentiate between wines and sort by region. This is something i would implement in the future. 

## Comment on Reviews ##
- In accordance with User Story 3, in the future I would like to implement the ability for users to comment on other peoples reviews, so that discussions can be had, but comments should be moderated. This was originally planned as a separate model, which is the way I would like to impolement it in the future. 
- User Story 3:
   ![User story3](/static/images/userstory3.png)

## Community wine review page ##
- I would as like a future feature to implement my contact page into a community review page, where users can leave their personal wine reviews and it can be a community hub. 

## Newsletter sign -up email ##
- Currently users can leave their name and email in order to get a newsletter from the site, which is a spotlight on a particular region. In the future implementations, instead of this being sent as user feedback and a link to click, I would like to set up a system where the user will automatically recieve the newsletter to their inbox, and therefore be signed up to our mailing list. 

###  Acknowledgments
- I would like to thank Emma at CI for her help, encouragement and support and for keeping me on track!
- I would like to thank Roo and Spencer for all the help they gave us, dealing with tricky problems which we managed to work through, this included the migration to VS code at the start of the project, and also to Roo for the various calls and advice on models, urls and Django framework, always there to help!  
- I would like to thanks Code Institute for all the help, courses/teaching and valuable learning they have given us throughout the whole course. 

<hr>
<p><a href="#contents">Back To Top</a></p>

- - - -
