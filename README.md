
# The Arcade

This Website was built by Isaac Nicholls, Paul Abrahams and Rogerio Soares for Code Institute Hackathon #1. The brief for the site was a fairly open scope, with the main point being an interactive site using Javascript at its core. After some research and brainstorming wehad the idea of an arcade game simulator, where the user could feel as if they were at an arcade playing the games they used to enjoy. This helped to tailor the User stories and styling.   

👩🏻‍💻 Here is an example of this website and its homepage ![Am I Responsive](/assets/images/rdme-image/responsive.png)

Link to deployed and finished site: https://github.com/IsaacNicholls1/TheAiTeam

---

## CONTENTS

* [Project](#project-goals)

* [Planning](#planning)
* [Teamwork](#hackathon-teamwork)

* [Features](#features)


* [Ux-Ui](#ux/ui)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Fonts](#fonts)
  * [Wireframes](#wireframes)
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

- The users goal is to access a gaming website where they can play their favourite games. 

- The users goal is to being able to navigate the website quickly and efficently to our content.

- The users goal is to use our site to get to and play the games they are looking for.

- The users goal is to have a fun experience playing games that they like, and also having the nostalgic feel of an old arcade gaming machine. 
    
## 2. Site Owner Goals
- The site owner goal is to provide an easily accesible website so that the user can easily get to the games they would like to play. 

- The site owner goal is to make a fun interactive website, so that the user feels immersed in the nostalgic experience. 

- - - -

## Project Structure

```
/C:/GitHub/TheAiTeam/
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   └── profile/
│   │       ├── avatar1.png
│   │       └── avatar2.png
│   └── js/
│       └── main.js
├── includes/
│   ├── navbar.html
│   └── footer.html
├── index.html
├── about.html
├── contact.html
├── games.html
├── snake.html
├── space-invaders.html
└── pac-man.html
```

# Planning #

- We used a resource called Trello, which was a good way to keep a handle on team projects. We could create cards on our workspace that we had, which could then be assigned to people and tasks could be managed and carried out. Below are two examples of the board in use. 
![Trello1](/assets/images/rdme-image/trello1.png)
![Trello2](/assets/images/rdme-image/trello2.png)
![Trello3](/assets/images/rdme-image/trello3.png)

## GitHub project planning
- We also used the github project board to enter in all our user stories, which could then be assigned and labelled. 

![githubproject](/assets/images/rdme-image/projectboard.png)

## MOSCOW Prioritisation 

- In order to utilise the MOSCOW prioritisation method, we made sure to utilise the project issues board in Github - which gave a very good overview of the issues we had with our user stories and allowed us to organise these and check they had been done as we went along. 

![moscow](/assets/images/rdme-image/moscow.png)

- - - -

# Hackathon Teamwork #

- We had to work as a team during this project, as we had not worked in a hackathon before. This threw up different problems for us, for example we had to spend a long time learning the process of git and github branches on the first day so that we could work effectively together. We overcame this together and after that it all ran smoothly. 

- We also had to make sure we were speaking all the time, so that no ones work was wiped over. To do this we used google chats, which was a very effective tool for keeping up to date with one another quickly. 
- We also utilised google meet to set up progress meeetings and update of progress.


- - - -

# Features #

## Main Page
### Background Javascript
The main page features javascript style background which gives the idea of flying through space, this has the feel of an arcade game of the time, and then includes a bootstrap5 responsive grid system with the game cards. 
### Cards
Below there are 4 cards with images in, which will take the user to the game pages. 
To do this the user hovers over the game card which contains a coin slot. The coin will then appear as the user hovers over the button, providing a fun and interactive experience. 

### JS Coin
Once the user has clicked the buttonn to navigate to the games pages and entered their coin into the slot, a JS styled coin drops down from the top, giving another interactive experience before the user reaches their goal of the game page.  

## About Page
This page features some information to the user about the site, the developers and a cta button at the bottom to return users to the main page in ordere to play our games. 

## Games Pages
These are the pages on our site where we wish the user to go - therefore there is a CTA buttonon the homepage to get to these. They are the pages where users will find and play the games they like.

## Contact page
This page is a simple contact form page with a header and the chance to get in contact with our site via a contact form. Some information to users is provided above the form, and everything is styled in the same styling as the rest of the site. 

## Privacy Policy and t&c's
These are essential pages to have, to outline the legal terms and conditions and privacy policy and are styled the same as the rest of the site. 

## Header and Footer
The header and footer have been kept the same throughout the site - styled simply with the same font from Font awesome and the spacing and colours all the same. 

## Usage

### Including the Navbar

This `JavaScript` code snippet defines a function called `loadNavbar` that is responsible for loading the `navbar` content from an external HTML file (`navbar.html`) and inserting it into an element on the current page.

``` javascript
function loadNavbar() {
    fetch('includes/navbar.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('navbar-placeholder').innerHTML = data;
            setActiveNavLink();
        });
}
```

### Setting the Active Link

The following function sets the active link in the navigation menu based on the current page.

``` javascript
function setActiveNavLink() {
    const path = window.location.pathname;
    const page = path.split("/").pop();

    const navLinks = {
        'index.html': 'nav-home',
        'about.html': 'nav-about',
        'games.html': 'nav-games',
        'contact.html': 'nav-contact'
    };

    const activeLinkId = navLinks[page];
    if (activeLinkId) {
        const activeLink = document.getElementById(activeLinkId);
        activeLink.classList.add('active');
        activeLink.setAttribute('aria-current', 'page');
    }
}
```

The loadNavbar(); function call is used to dynamically load the navbar content from an external HTML file and insert it into the current page.

```javascript
loadNavbar();
```

The following HTML snippet is used to include a placeholder for the footer content in your web pages:

```html
<footer>
  <div id="footer-placeholder"></div>
</footer>
```


<hr>
<p><a href="#contents">Back To Top</a></p>

- - - -

# UX/UI #

   ## Target Audience
   
  - Anyone looking for a fun gaming experience with retro games
  - People wishing to feel some nostalgia with games they may have played before.
  - Users looking to spend some time playing retro games, and looking for an immersive gaming experience.  
  
 ## User Stories
  - User Story: As a user, I want to visit a retro gaming website and play games so that I can enjoy classic arcade games online.
  - User Story: As a user, I want to easily navigate to the games so that I can quickly find and start playing my favorite retro games.
  - User Story: As a user, I want the website to have the feel of an arcade game, providing nostalgia so that I can relive the classic arcade experience.
  - User Story: As a user, I want a contact/feedback form on the website so that I can share my thoughts and ask questions.
  - User Story: As a user, I want to access an about page so that I can learn more about the games and the website.
  - User Story: As a user, I want to have an easily accessible footer so that I can quickly find important information and links.
  - User Story: As a user, I want clear instructions on how to play the game so that I can understand the game mechanics and enjoy playing.
  - User Story: As a user, I want the website to be responsive and mobile-friendly so that I can access it on my smartphone or tablet.
  - User Story: As a user, I want the website to have an engaging visual design so that it is visually appealing and enjoyable to use.
  - User Story: As a developer, I want a detailed README file so that I can understand the project setup, usage, and contribution guidelines.

  
<hr>
<p><a href="#contents">Back To Top</a></p>
- - - -

 ## Design
 
 ##  Colour Scheme

 - The colour scheme for our site was inspired by the look and feel of an old arcade machine, with simple black and white background and font, with some other colors inspired by the graphics and images. 
 - Inspired by https://coolors.co/16084a-141414-eef0f2-ffa90a-c270b0

 **Coolers**
![Colours](/assets/images/rdme-image/coolercolorscheme.png)
 
 ##  Fonts
 - The font that we used was PressStart2p - We wanted to focus on what the font would have looked like on the old style arcade machine, quite pixelated and therefore we recreated that.  

 ![Font](/assets/images/rdme-image/googlefont.png)
 
 ## Wireframes

 - These wireframes have been created using Balsamiq to define the key feature layout to guide the user experience design. 
 Utilising the Bootstrap framework and available components allows for the construction of a page that feels familiar for ease of navigation whilst also allowing for well structured content and a responsive design.
 The wireframes were developed at the start of the project and then worked on as we went through, to tweak the changed we made to the design and feel of the site
 - They differ slightly to the exact look of the site as we decided we had to use different images and styles to the wire frame ideas. 
    
  - Home Page Wireframe

  **Home Page Wireframe**
![Home Wireframe](/assets/images/rdme-image/wireframe/HomePage.png)

 **About Page Wireframe**
![About Wireframe](/assets/images/rdme-image/wireframe/AboutPage.png)

**Space Invaders Game Page Wireframe**
![SI Wireframe](/assets/images/rdme-image/wireframe/siwireframe.png)

**Snake Game Page Wireframe**
![Snake Wireframe](/assets/images/rdme-image/wireframe/Snakegamepage.png)

**Pac-man Game Page Wireframe**
![Pacman Wireframe](/assets/images/rdme-image/wireframe/pacmangamepage.png)
  
**Contact Page Wireframe**
![Contact Wireframe](/assets/images/rdme-image/wireframe/ContactFormPage.png)

<hr>
<p><a href="#contents">Back To Top</a></p>

- - - -


# Testing #

## HTML Validation
- Initial HTML Validation was performed using the W3C Mark up service and the results can be found in this document. 
- Any issues were dealt with at the time. 

![html1](/assets/images/rdme-image/htmlvalidator.png)
![html2](/assets/images/rdme-image/htmlvalidator2.png)
![html3](/assets/images/rdme-image/htmlvalidator3.png)
![html4](/assets/images/rdme-image/html4.png)
![html5](/assets/images/rdme-image/html5.png)
![html6](/assets/images/rdme-image/html6.png)
  
## CSS Validation
- W3C CSS style sheet validation link 
![Css1](/assets/images/rdme-image/cssvalidator.png)


## JS Validation
- Initial validation
![JS](/assets/images/rdme-image/jsvalidation.png)
- The test showed that the only warnings showing up were due top the bootstrap style insert on line 2.  

 
## Accessibility
 - We tested the page with lighthouse and the accessibility and performance scores are shown below
![lighthouse scores](/assets/images/rdme-image/lighthouse1.png)
![lighthouse scores](/assets/images/rdme-image/lighthouse2.png)
![lighthouse scores](/assets/images/rdme-image/lighthouse3.png)
 

## Responsivity
- We tested the website with DevTools so that it worked across all different device sizes, including mobile and tablet. This is very important as it must be functional across all types of devices. The games must work on all devices and be compatible.

- We checked the site was responsive across all devices. Originally we had a problem with ...

![Am I Responsive home](/assets/images/rdme-image/responsive.png)
![Am I Responsive about](/assets/images/rdme-image/responsiveabout.png)
![Am I Responsive contact](/assets/images/rdme-image/responsivecontact.png)

## Device Testing

We tested the site with the following devices:

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

We tested our site vs the user stories: 

1. 
User Story:
![User story](/assets/images/rdme-image/userstories/userstory1done.png)

--

2. 
User Story:
![User story](/assets/images/rdme-image/userstories/userstory2done.png)

--

3.
User Story:
![User story](/assets/images/rdme-image/userstories/userstory3done.png)

--

4.
User Story:
![User story](/assets/images/rdme-image/userstories/userstory4done.png)

--

5. 
User Story:
![User story](/assets/images/rdme-image/userstories/userstory5done.png)

--

6.
User Story:
![User story](/assets/images/rdme-image/userstories/userstory6done.png)

--

7.
User Story: please see future featues

--

8.
User Story: please see future featues

--

9.

User Story:
![User story](/assets/images/rdme-image/userstories/userstory9done.png)

--

10.
User Story:
![User story](/assets/images/rdme-image/userstories/userstory10done.png)

--

11.
User Story:
![User story](/assets/images/rdme-image/userstories/userstory11done.png)


<hr>
<p><a href="#contents">Back To Top</a></p>
--

## Known Bugs

## During development, I found these bugs and fixed them:

### Nav bar dropdown shifting to the right hand side on smaller devices

- On smaller devices, in the connect.html and index.html pages the navbar burger logo to indicate the nav bar would switch sides and throw everything on there out of line.
- To fix this issue, we checked the code in the other pages and texted them where it worked fine. The issue was due to the logo which we had in the first pages. we copied across the code, resized the logo and this worked.
- Other bugs we encountered where that pages took us to different links, which we fixed by including then correct page link and making sure this worked on the deployed version of the site.  

### Other issue/bug

- Out footer text was not wanting to line up and be the same as the rest on the font for the pages. This had to be fixed and debugged. 

### Poor Font for User

- We felt that the font had to be just right for the website feel and the user, and after some testing we found the perfect one which was not our first option.  

### Other bugs

- We felt that the font had to be just right for the website feel and the user, and after some testing we found the perfect one which was not our first option. 



## During development and testing, these are the current bugs:

### Images  

- Some of the images are still too large - generating a lower lighthouse score than we would have liked. 

### Unknown code fixes in lighthouse

- There are some errors/warnings in lighthouse which would improve the score. We will research these before the next project and make sure to find out how to fix them. 

### Responsiveness

- Responsiveness issues were encountered with the games pages - we would have liked to implement and test these further but ran out of time. 
- With more time this could have been tested further, the games were responsive but not all the way and with every device. We would have liked to test and implement these better, for enhanced UX. 

### Responsiveness

- There were also other smaller bugs and developments we would have liked to have made - if we had more time things such as the text, titles, spacing and alignment were things that were flagged up to change and edit. 

<hr>
<p><a href="#contents">Back To Top</a></p>


- - - -


# Deployment #

How I deployed this site : 

- In the GitHub repository, I navigated to the Settings tab, then chose Pages from the left hand menu 
- From the source section drop-down menu, selected main branch
- Once the main branch had been selected, the page was automatically refreshed with a detailed ribbon display to indicate the successful deployment
- Any changes pushed to the main branch take effect on the live project

- The live link is here: https://github.com/IsaacNicholls1/TheAiTeam

- I used an agile methodology by using early deployment, I made sure the project was deployed after the first few pages were created. This ensured that I could see every change on a live site, which greatly aided the coding and development process.
![Site Example](/assets/images/rdme-image/earlydeployment.png)

<hr>
<p><a href="#contents">Back To Top</a></p>

- - - -

# Sources #

### Languages Used

- HTML5
- Css
- Javascript

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
   - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/specimen/Press+Start+2P?selection.family=Monoton|Orbitron:wght@400..900|Press+Start+2P|VT323)
   - Google fonts were used to import the PressStart2p font into the style.css file which is used on all pages throughout the project.
3. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
4. [jQuery:](https://jquery.com/)
   - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
5. [Git](https://git-scm.com/)
   - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
7. [GitHub:](https://github.com/IsaacNicholls1/TheAiTeam)
   - GitHub is used to store the projects code after being pushed from Git.
8. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
   - Photoshop was used for resizing images and editing photos for the website.
9. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the wireframes during the design process.

## Media
 - The images that were used throughout the project were mostly developed by Paul using photoshop, and images from different sources.  
 - The following photos were used in the content: (https://github.com/IsaacNicholls1/TheAiTeam/tree/main/assets/images)
 - Some images were edited with Photoshop - this was to reduce their size and get them the correct shape, therefore providing a better UX when visiting the site.


## Content
- Font awesome was used to add icons for UX purposes auch as social media icons. 
- Balsamiq was used to create the wireframes during the design process, as this was the second time of using the tool it took a bit of getting used to and developing these. We tweaked them as i went along and made slight changes to the actual site. 

## Code
- The HTML & CSS uses Bootstrap Version 5.3: https://getbootstrap.com/docs/5.3/getting-started/introduction/ 
- I used other coding tools and resources such as snippets of code from our previous CI projects to guide and aid when we needed reminding about the correct way to use the code.
- The following sites were used for examples of code for the games, and the stars hero image. 
- SITES/GitHub pages used here : 
- https://codepen.io/adelciotto/pen/WNzRYy
- https://www.geeksforgeeks.org/create-a-snake-game-using-html-css-and-javascript/
- https://codepen.io/hellokatili/pen/xwKRmo
- https://codepen.io/bts/pen/BygMzB
- Pexels was used to get some photos, alongside photostock and google images. 

## Use of AI

- We utilised AI in this project in the form of CoPilot. This helped to create basic HTML structures and to edit parts of code that needed it, to structure and help keep styling the same. I found it very useful overall and saved me a great deal of time, however I found when using, it needed a close eye kept on it as it sometimes adds in extra closing tags and code that is sometimes not needed. 
- It was used in the creating of some of the Javascript sections, and also to create content for the privacy policy and Terms and Conditions sections. 

# Other issues #

- Another issue faced was within Github - where we had a merge conflict at one point. 
- ![github conflict](/assets/images/rdme-image/mergeconflict.png)
- This meant that the Project lead needed to go into github and find the problem. Then to research how to solve the problem in Github as this was a new issue. The site that was very useful for this was https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github
- This helped to explain the merge conflicts and how to resolve the issue, which was then implemented and the issue fixed.  

# Future features #
- If we had more time, we would have liked to add in an additional feature for the games, which would have been able to show  the score of the player in relation to the top and highest scores of others as a leaderboard, for each game. 
-  We had a nice javascript image to use for the hero of each page which gave the effect of flying through space, we would have really liked to use this image/design but ran out of time to implement it. 
- One extra thing would have been to add in a search bar at the top in the navbar as this would provide a better UX, giving the user the ability to find what they need from anywhere in the site. 
- We would have liked to improve our lighthouse scores, and get them all up into the 90's 
- A future feature that we wished to add was the option of adding an easter egg for users to find within the games, or somewhere on each page. If clicked and found this could then increase he score, or give a hint to the user of how to win the game. We did not have time to implement this. 
- We would have liked to develop our testing table further, as all aspects of the site were tested but documentation in the readme could have been more thorough for this, again we ran out of time. 
- We wanted to provide a description of how to play each game with text that pops up in a modal. 
![Text Game](/assets/images/rdme-image/futuretext.png)
- We wished to add a coin slot to our graphics, and had the idea of using javascript to make a coin appear when you hovered over, and it fall into the slot when you clicked. We did some testing of this and did get it to a working stage but it did not make it into the end product unfortunately, but with more time it would have. 

- Future features that we would have liked to implement from our user stories
   User Story:
   ![User story](/assets/images/rdme-image/userstories/userstory13.png)
   User Story:
   ![User story](/assets/images/rdme-image/userstories/userstory7.png)


###  Acknowledgments
- We would like to thank Emma at CI for her help and encouragement. 
- We would like to thank Roo, Mark and Spencer for all the help they gave us, dealing with tricky problems which we managed to work through!

<hr>
<p><a href="#contents">Back To Top</a></p>

- - - -
