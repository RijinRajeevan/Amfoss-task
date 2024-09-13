
# Documentation for Micro Blog
## Overview
The **Microblog** project is a simple web application built with Flask, designed to simulate a microblogging platform, similar to Twitter. It provides basic features such as user registration, posting messages, following/unfollowing other users, and displaying posts in a timeline. The application includes functionality for user authentication, pagination, and profile management.
## Features 
- User registration and login/logout system
- Creating, editing, and viewing posts
- Following and unfollowing other users
- Displays not only the user's posts but also the posts from users they are following
- Paginated display of posts on the timeline
-  If a post is in another language, a blue "Translate" button appears, and clicking it translates the post
- Displays the last time a user was active on their profile page
- User profile management
- Password reset functionality
- It has the ablity for  users to send private messages to other users
- We can export our posts
## Code Documentation
#### 1. microblog/app/__init__.py
Initializes the Flask application, configures settings, and sets up extensions.

- `def create_app()` :
Sets up necessary settings and configurations for the app.Initializes tools and libraries like SQLAlchemy for the database, Migrate for database changes, and Flask-Login for user sessions.Connects different parts of the application (called blueprints) to the main app.

#### 2. microblog/app/models.py
Defines data models for the application using SQLAlchemy, representing database tables.

- `User` :
Represents a user in the app, including attributes for managing user details and relationships (ex. like the followers).

- `Post` :
Represents a post created by a user, including attributes for post content and relationships with users.
#### 3. microblog/app/main/routes.py
Defines the web pages or endpoints for the main section of the application. This file handles the routing, which determines what content is shown when users visit different URLs. 

- `/` and `/index`:
Displays posts from users the current user is following and allows posting new content.

- `/explore` :
Shows all posts in the system, allowing users to discover new content.

- `/user/<username>` :
Displays a specific user's profile and their posts.

- `/edit_profile` :
Allows users to update their profile information.

#### 4. microblog/app/main/forms.py
Defines and manages forms for user input using Flask-WTF.

- `EditProfileForm` :
For updating the user’s profile information.

- `PostForm` :
Used for creating and editing posts.

- `SearchForm` :
Used for search functionality in the application.

- `MessageForm` :
Ensures the message is not empty and does not exceed 140 characters.

#### 4. microblog/app/templates
Contains HTML templates that render the web pages.

- `base.html` :
The base layout used for other templates

- `index.html` :
Renders the homepage and user timeline.

- `messages.html` :
Displays the user’s messages and allows for new message interactions.

- `edit_profile.html` :
Allows users to edit their profile information.

- `user_popup.html` :
Shows a popup view of a user’s profile.

#### 5. microblog/app/api/errors.py
Provides custom error pages for handling HTTP errors.

- `error_response(status_code, message=None)`
Creates a standardized error response. It includes the HTTP status code description and an optional custom message.

- `bad_request(message)` :
A helper function to create a 400 Bad Request error response with a custom message.

#### 6. microblog/app/auth/email.py
Manages email functionalities such as sending password reset instructions.

- `send_password_reset_email(user)` :
Sends a password reset email to the specified user.


## Implementation Details 
#### Post Creation :
Posts are created through the PostForm in index.html. The form data is processed in the index view in main/routes.py, which adds a new Post instance to the database.
   
#### Post Listing :
Posts are displayed in index.html by querying the Post model in the index view. The view retrieves posts from users the current user is following and passes them to the template for rendering.

#### Post Exploration :
Posts are explored through the explore view in main/routes.py, which fetches all posts and lists them in index.html for exploration.

#### User Profile :
User profiles are shown in user.html by querying the User model in the user view. The view retrieves the user’s posts and displays them along with user information.

#### Profile Editing :
Users can edit their profiles,i have implemented it by edit_profile.html. The edit_profile view handles form submissions and updates user details in the database.

#### Message Handling :
Messages are managed using the MessageForm in messages.html. The form data is processed in the messages view, which handles sending and displaying messages between users.

#### Error Handling :
Errors are managed using custom error responses in errors.py. The handle_exception function provides structured error messages for HTTP exceptions.

## Usage
#### 1. Creating a Post :
Navigate to the home page. Use the form at the top of the page to write and submit your post.
#### 2. Viewing Posts :
On the home page, we can see posts from users we follow. You can also explore posts from all users by navigating to /explore.
#### 3. Updating Your Profile :
Go to the profile editing page (/edit your profile). Update your username or "About me" section and save the changes.
#### 4. Following/Unfollowing Users :
On any user’s profile page (/user/<username>), use the provided buttons to follow or unfollow that user.
#### 5. Handling Messages :
Access your messages through the messages.html page. You can send and receive messages there.
#### 6. Error Handling :
If an error occurs, you’ll see an error message formatted by the application, providing details about the issue.
#### 7. Localization :
The application detects your preferred language and displays content accordingly. You can manually translate posts using the translate option if available.
#### 8. Exporting Posts :
To export your posts, use the export feature available in the settings or profile page. This allows you to download your posts and other relevant information in a structured format.



