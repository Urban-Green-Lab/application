
# Test Plan: Urban Green Lab Gameventify Project

Thursday, October 29, 2020 at 10:09 AM
Authored by: Summer Perkey and Ankaj Goel

## INTRODUCTION

- This application is used to create quizzes that can be administered at events or on the internet.
- There is a backend admin site as well as a user application for game play, which also includes a leaderboard.
- This application will be a web based application that can be used on desktop or mobile web browsers. This is not a freestanding mobile application.
- This application will be used by both adults and children. Demographics will be captured for users over 18 years old. Only Username will be required for those under 18 years old.

### TOOLS

- Developers will be committing work to the team GitHub repository. Once pull requests are completed these will be ready for QA testing.
- Backend API testing will be completed using PostMan calls and Frontend UI will be available via direct URLs for testing.

### TIMESCALE

Full development and testing to be completed within the timeframe of the Hack for the Community event. Due to time constraints the following items may not be fully tested:

- Full Application functionality on physical mobile device
- Full Application functionality on desktop browser

### OUT OF SCOPE

Mobile Application

### ASSUMPTIONS

- All users have internet access
- All users have web browsers
- The majority of users will be on mobile devices
- All users will be able to read and comprehend the English language
- All users will receive questions from the event set regardless of age 
- Only users of the age of 18 will be required to complete registration

### RISKS

- Given the responsive nature of web page, different screen sizes and resolutions may have UI look distorted. QA team will try to cover as many resolutions as possible in given time limit.
- Limited testing of desktop version on all browsers and/or physical devices
- Due to time limit, there might be few open bugs which might get deferred and would need to be addressed by support team (post H4TC)

## TEST CASES/SCENARIOS

### Front-End Project

#### Splash Screen

- Confirm URL directs user to the correct event
- Confirm Screen has correct branding 
- Confirm [Play the Game] button functionality - advances user based upon age range set for event
- Confirm [How to Play] button functionality - triggers How to Play modal
- Confirm How to Play modal content
  
#### AGE RANGE

- All Age Groups
- Confirm [Play the Game] button advances user to the User Info Screen

#### User Info Screen

- Confirm the following data fields are present:
  - First Name (no character requirements)
  - Last Name (no character requirements)
  - Email (@ requirement)
  - Zip Code (5 numeric characters only)
- Confirm all data fields are marked and function as required
- Confirm [Get ready] button functionality - advances user to Countdown

#### Under 18 years old Age Groups

- Confirm [Play the Game] button advances user to the Countdown
- Confirm that UserInfo page does not display following
  - email address field
  - First Name
  - Last Name
- Confirm that UserInfo page asks if user want to create a username so it can be displayed in Leaderboard
- Confirm that if username is selected, it cannot be blank

#### Countdown

- Confirm each number of the countdown is presented in the correct order
- Confirm [Let’s play] button functionality - advances user to 1st Question in the event
- Confirm that [Let’s play] button is disabled till the counter is running.

#### Question Component

- Confirm question number is showing in correct order and updating as user progresses
- Confirm question content
- Confirm answer content
- Confirm question timer
- Confirm answer selection highlighted
- Confirm correct answer path
- Correct answer highlighted
- Points awarded message
- Confirm user advanced to the next question following buffer time of X seconds
- Confirm incorrect answer path
- Incorrect answer highlighted
- Correct answer highlighted
- No points awarded message
- Confirm user advanced to the next question following buffer time of X seconds
- After answering the final question in the set, confirm user advanced to Score/Results screen following buffer time of X seconds

#### Score/Results Screen

- Confirm content for results message
- Confirm score displaying correctly
- Confirm [View leaderboard] button functionality - advances user to Leaderboard page

#### Leaderboard

- Confirm displays score correctly
- Confirm content [Add your initials to the leaderboard]
- Confirm Initials field
- With header [Add three letters]
  - Confirm field accepts 3 characters
  - Confirm [Add my score] button functionality - advances user to leaderboard list
  - Confirm leaderboard list in correct order, i.e. as we more quizzes are answered, the leaderboard is updated
- Confirm list showing all elements:
- Place - in descending order
- Initials
- Score
- Confirm user can scroll through list
- Confirm [Exit] button functionality - returns user to the splash page

### Logos

- Confirm branding is correctly implemented on all screens

### Error Handling 

- Confirm 400 and 500 errors trigger an error messages consistent with application branding
- Confirm that for a non 200 ok response returned by API, application redirects to error page. 
- Confirm that the error page has some link to redirect user to the home page, i.e. exit out of that workflow and allow it to start over.

#### Functional Flows

- Check the application when in child mode
- Check the application flow when in adult mode

### Back-End Project

#### Database

- Confirm demographic information entered on home page is captured
- Confirm score/leaderboard  is captured

#### API

- Confirm CRUD API endpoints with PostMan calls
- Confirm that API endpoints have Authorization
- If a special character is passed in a GET or POST body, API should be able to encode that and handle it.

### Security

- Back-End development team to conduct necessary Security testing.
