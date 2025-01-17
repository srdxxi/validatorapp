##Validator App

The Validator App uses [Alloy](https://www.alloy.com/) to provide a quick decision on U.S.-based credit applications by analyzing a candidate's risk based on the following personal information:

- First Name
- Last Name
- Address 
- City
- Two-letter U.S. State code
- Zip Code
- Social Security Number
- Email Address
- Date of birth (YYYY-MM-DD format)

Alloy evaluates the candidate and provides one of the following responses:

- **Approved** the candidate's application has been approved. 
- **Denied** the candidate's application has been denied.
- **Manual Review** the candidate's application needs further review and has been sent to [the *Review Queue* in Alloy](https://help.alloy.com/hc/en-us/articles/4405650462363-Manual-Review-Individual-Evaluations).

###Technical details

The app is built using [Flask](https://flask.palletsprojects.com/en/stable/) for the backend and [Vue.js](https://vuejs.org/) for the frontend. It leverages the `/evaluations` endpoint of [Alloy's API](https://developer.alloy.com/public/reference/post_evaluations) to evaluate the candidate's application based on the provided input. 

To run the Fradulator locally, you will need create an API token and have it accesible via the `ALLOY_KEY` envar. See [Alloy API Authentication Guide](https://developer.alloy.com/public/docs/authentication-guide) for more information on authentication to the API.)

###Future enhancements

- Submitting multiple applicants at once
- Reviewing past submissions
- More robust error handling