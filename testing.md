# Testing 

Throughout the development of the project, code was regularly tested using Chrome developer tools, manual testing was performed and code was passed through validators like W3C for HTML, Jigsaw for CSS and Jshint for JS.

List of devices that the website was tested on for responsiveness through chrome developer tools:

- iPhone SE
- iPhone XR
- iPhone 12 Pro
- Pixel 5
- Samsung Galaxy S8
- Samsung Galaxy S20 Ultra
- Samsung Galaxy A51/71
- Samsung Galaxy A52/A53 5g

![Home Page](assets/images/manual_testing/mobile_responsive_homepage.png) ![All Recipes](assets/images/manual_testing/mobile_responsive_all_recipes.png) ![Profile Page](assets/images/manual_testing/mobile_responsive_profile.png)
![Log In](assets/images/manual_testing/mobile_responsive_log_in.png) ![Log Out](assets/images/manual_testing/mobile_responsive_log_out.png) ![Sign Up](assets/images/manual_testing/mobile_responsive_SIGN_UP.png)
![Post Recipe](assets/images/manual_testing/mobile_responsive_post_recipe_1.png) ![Post Recipe](assets/images/manual_testing/mobile_responsive_post_recipe_2.png) ![Recipe Details](assets/images/manual_testing/mobile_responsive_recipe_details_1.png)
![Recipe Details](assets/images/manual_testing/mobile_responsive_recipe_details_2.png)

## Manual Testing

### Sign Up / Log In / Log Out

| Type of Test | Steps |Expected Results | Results
|--------------|-------|------------------|-------
|**Create Account**| Visit https://pauls-kitchen.herokuapp.com/ | Opens the site | Working as intended
|| Click Sign Up button | Opens the Sign Up page | Working as intended 
|| Fill in username, email and password x 2 and click submit | Login page should open | Working as intended
|**Log In**| Log in with just details entered in sign up form | Home page should open | Working as intended
|| Home page should change to reflect a logged in user with | Log out button available | Working as intedned
|**Create account with wrong details** | Visit https://pauls-kitchen.herokuapp.com/ | Opens the site | Working as intended
|| Click Sign Up button | Opens the Sign Up page | Working as intended 
|| Fill in username, email, enter 2 passwords that dont match and click submit | Prompt user to enter matching passwords | Working as intended
|**Log Out** | Navigate to home page and click log out | Logout page should open and ask user are they sure | Working as intended
|| Click Log Out button | Home page should open and Login / Signup buttons available | Working as Intended

### Post a Recipe
| Type of Test | Steps | Expected Results | Results |
| -------------|-------|------------------|---------|
|**Post Recipe with Placeholder** | From Home Page Click Post Recipe button | Open add recipe page | Working as intended
|| Fill all fields with "This is a Manual Test" no image and click submit | Recipe should be posted with placeholder image | Working as intended
|**Post Recipe with Image**| From Home Page Click Post Recipe button | Open add recipe page | Working as intended
|| Fill all fields with "This is a Manual Test 2" click choose file select a image and click submit | Recipe should be posted image selected | Working as intended

### Delete / Edit a Recipe
| Type of Test | Steps | Expected Results | Results |
| -------------|-------|------------------|---------|
|**Edit Recipe**| From Home Page as a logged in user Click "Manual-Test-Account's Profile" Profile Button | Opens profile page for the logged in User | Working as intended
|| Select the Recipe to edit "Manual Test " | When recipe details page opens should be 3 options "Like" "Edit" "Delete" | Working as inteded
|| Click the "Edit" Button | The Edit Recipe form should open | Working as intended
|| Add to all fields "this is a edit" and submit | recipe list should open, a message displays "recipe updated successfully" | Workign as intended
|| Go back into "Manual Test - edit" detail page and update image and then click submit | recipe list should open, a message displays "recipe updated successfully" and image should change | FAIL image didnt change
|**Delete Recipe**| From Home Page as a logged in user Click "Manual-Test-Account's Profile" Profile Button | Opens profile page for the logged in User | Working as intended
|| Select the Recipe to delete "This is a manual Test 2 " | When recipe details page opens should be 3 options "Like" "Edit" "Delete" | Working as inteded
|| Click the "Delete" Button | The delete recipe page should open and user is asked are they sure they want to delete | Working as intended
|| Click the "Delete Button | recipe list should open, a message displays "recipe deleted successfully" | Workign as intended
|| Naviage back to "Manual-Test-Account's Profile" page "This is a manual Test 2 " should be deleted from the site | Working as intedned

