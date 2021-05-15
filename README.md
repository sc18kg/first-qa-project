### Movie Review Website
 ## Contents
* [Objective](#objective)
* [Requirements](#Requirements)
* [Approach](#Approach)
* [Risk Assesment](#Risk-Assesment)
* [Architecture](#Architecture)
* [CI Pipeline](#CI-Pipeline)
* [Project Tracking](#Project-Tracking)
* [Continuous Intergration](#Continuous-intergration)
* [Testing](#Testing)
* [Final Application - Front End](#Final-Application---Front-End)
* [Future Improvements](#Future-Improvements)



## Objective
To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

## Requirements
## are as follows:

**A Trello board** (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.  
**A relational database** used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.  
**Clear Documentation** from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
**A functional CRUD application created in Python**, following best
practices and design principles, that meets the requirements set on
your Kanban Board  
**Fully designed test suites** for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.  
**A functioning front-end website and integrated API's**, using Flask.  
Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.  

## Approach
I have created an application which adheres to the objective.
**Create:** You are able to create Films and Reviews.  
**Read:** You are able to view existing films and reviews that are input onto the application.  
**Update:** You are able to upade the existing films on the application and also the reviews.  
**Delete:** You are able to delete both your own reviews and also the films entered in the application.  

## Risk Assesment

Prior to building the application I had completed a risk assesment for all the items which I deemed as
a risk for the project  
Upon reflection I have included a few more items which I have discovered from using various tools building the application
Here is an updated version where I have highlighted the rows which I added later down the line.
![Risk Assesment](https://i.imgur.com/rmNs94Y.png)
[Link to my Risk Assesment](https://docs.google.com/spreadsheets/d/139uNft5K6sNDZgaGhPrtIWHvzJF40PCcAND5tNtLiuY/edit#gid=0)

## Architecture

Initially I came up with an architecture which I believed would be fit for purpose for the application
I build an ERD diagram to show the two databases which I am using and also the relationship between them. I have a 
one and only one to many relationship between the databases. This is due to a film can have many reviews however each review is only
linked with the one specific film.
![oldERD](https://i.imgur.com/tOijCxW.png)  
Again during the building stage I realised I had not covered everything I would like or need to include in my application so
I created a new one to reflect the changes I had made which was to just feature more fields but kept the relationship the same.  
![newERD](https://i.imgur.com/bvU1Yih.jpg)

## CI Pipeline
CI is short for Continuous Intergration and is a software development practice. Its a runnable specification of the steps that any developer would need to
produce a new version of a software product which is autoamated once set-up. Please find below the image which I have created which covers each the deveolpment
and deploying of my application. I have chosen the best fit services for my application for efficent and rapid deveopment and testing.
![CIPipeline](https://i.imgur.com/zFJJngX.jpg)

## Project Tracking

As a DevOps engineerm, the idea is to create the application or software following the best methology and this is using an Agile method
I have created a Trello board which features all the tasks which I had to complete in order to produce the application that meets the set requirements.
I have used MoSCoW techique (Must Have, Should Have, Could Have, Won't Have this time) to prioritisation the tasks for my application I have colour coded the
user stories, use cases and tasks to show this, green being a must, yellow a should, orange a could and red being wont. I also used story points to estimate
the effort for each task.
![Trello](https://i.imgur.com/CJStl34.png)
[Link to my Trello](https://trello.com/b/Sc9YjKgM/qa-project)

From the story points I created a burn-down chart which helps visualise the effort for a spreint and show the remaining effort this needs to be as close to the
ideal burn-out to ensure a steady work flow and reduce heavy loads at certain times in the application.
(Insert Burnout)

## Continuous Intergration

I have used CI as its usually paired alongside agile software development which is the method for this project. The main focus of the CI is to automate the testing process, from using a webhook I have enabled the tests which I have written to be performed every time an update is pushed to the git repository as Jenkins fetches this information and runs both the intergration and unit tests. Below I have insert the instructions that are used to input for the Jenkins to run:  
# Jenkins Build Script
```
sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip chromium-browser wget unzip -y

version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium-browser --version | grep -oP 'Chromium \K\d+'))
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

export DATABASE_URI=mysql+pymysql://root:jasper123@10.92.224.3/project_db
export SECRET_KEY=qwertyuioplkjhgfdsazxcvbnm

python3 -m pytest --cov=application --disable-warnings
```

## Testing
# Unit Tests
for the unit tests, this works by testing against each function I have and using assertions checks that the function is returning the correct or expected results
As you can see from the image below, I have reached 100% coverage meaning every function has been tested.  

# Intergration Tests
For the intergration tests, I used selenium which is a driver used to simulate user input. For my application, I tested adding a new film to the database
I had selenium enter data and and clicking buttons using their xPath which was then checked for the correct input. As you can see from the tests I have passed
all 18, this number is refering to both the Unit and Intergration tests.
![unit](https://i.imgur.com/L4cj1me.png)

## Final Application Front-End
# Home
# Film list 
# Add Review
# Add Film
# Count
