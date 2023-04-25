# eleks-intern-pnu-video-access
## It's one of the task, provided by the company Eleks for an internship (8 semester).
### Task
Videos Access Point

Estimate - 120 hours

Develop a web service and database that provides information about various types of videos.

The database contains the following mandatory information about the video clip:
• Title.

• Brief description.

• Genre (jokes, cartoons, news, sports, etc.).

• The user who provided information about the video clip.

• Links to videos (eg youtube links).

• Download date.

The database also contains information about users:

• First name.

• Password.

The web service provides the following options if the user has the correct Username and Password (required
organize user authorization):

• Get 100 latest downloaded video records.

• Get the 100 most recent downloads of a specific genre.

• Get video records for a certain period of time.

• Get a record of a specific video clip.

• Upload new video information. At the same time, the recorded data must
meet the requirements: name cannot be empty, link must be a valid URL
address

## Solution
A WEB application, “Videos Access Point” was developed using the Django framework. After running the empty project and making sure everything was working fine, work on authorization started - namely registration and login. To log in, you need to enter a username and password, for registration, the list is a little longer. This information will be stored in the database (MySQL), according to the requirements of the task, the password will also be automatically hashed. You can view it by going to the Django admin panel (http://127.0.0.1:8000/admin).
By entering the correct username and password, the user gets access to a table with a database that contains all the necessary information (specified in the task). For a specific recording of a video clip, you can change the data, delete them, etc. When creating a new record, the name of the logged-in user is immediately entered in the input field, and the date of creation is automatically pulled. All fields must be filled in, the address is checked for validity (512 characters is enough for a YouTube link).
A full-fledged CRM system has been created, which provides the ability to manage users (CRUD operations) and video records.
### Project Structure:
```
├───src                                 <- Code
|
├───main.py                             <- For console tests
|
├───.gitignore                          <- Ignore files
|
├───README.md
|
└───requirements.txt
```

### An example of a completed task:

### Run code in Windows:
```
cd src
py manage.py runserver
```