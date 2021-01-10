## frontend-app-logistration
This is a micro-frontend application responsible for the login, registration and password reset functionality. End modified for Tutor Open edX.
This is an example plugin for to implement a micro-frontend application to Tutor Open edX. This example little bit different than this repository https://github.com/overhangio/tutor-gradebook but it works. Please test it before using in production !

#### Cloning and configuring Frontend-app-logistration

Step 1: Fork this repository https://github.com/edx/frontend-app-logistration to your GitHub account

Step 2: Clon the repo to your local PC or server, than make a new branch for your customizations.
`$ git branch <YourBranchName>`


`$ git clone -b solo https://github.com/murat-polat/frontend-app-logistration `

Than edit
`https://github.com/murat-polat/frontend-app-logistration/blob/murat/.env.development` file with your environment values, push back to GitHub.


### Installation:

If using virtualenv: (optional)

`$ python3 -m venv ~/tutor`

`$ source ~/tutor/bin/activate`

 Cloning and installing plugin

`$ https://github.com/murat-polat/tutor-applogistration `

`$ pip3 install -e tutor-applogistration`

`$ tutor plugins list`

`$ tutor plugins enable applogistration`

Building new Docker services for Tutor

`$ tutor images build applogistration`

`$ tutor local quickstart `

visit http://yourdomain.com:1999/login.

## Development
Start Devstack
To use this application devstack must be running.

## Start devstack
Start the development server
In this project, install requirements and start the development server by running:

`npm install`

`npm start` # The server will run on port 1999
Once the dev server is up visit http://localhost:1999/login.


![](src/login.png)


## Configuration and Deployment
This MFE is configured via node environment variables supplied at build time. See the .env file for the list of required environment variables. Example build syntax with a single environment variable:

`NODE_ENV=development ACCESS_TOKEN_COOKIE_NAME='edx-jwt-cookie-header-payload' npm run build`

For more information see the document: Micro-frontend applications in Open edX.

![](src/register.png)

### Django Admin site redirection(login and register pages)
By default Open edX login page is " LMS_HOST/login ". But on Logistration  is " LMS_HOST:1999/login ". So we must redirect **login** and **register** pages to the new login pages . There are different ways available for redirections. But the most easiest way, to do that on the Django Admin side.

To add new site go to the http://yourdomain.com/admin/sites/site/ and add new site for Logistration service: (LMS_HOST:1999)

![](src/add_new_site.png)

After adding new page go to the http://yourdomain.com/admin/redirects/redirect/ and add new redirection for **login** page
