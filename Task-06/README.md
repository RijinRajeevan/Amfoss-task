
# Open Docs
The **Microblog** repository (https://github.com/miguelgrinberg/microblog.git) is a simple website, like a mini version of Twitter, built using Flask. It lets users sign up, post messages, follow others, and see posts on a timeline.

## Micro Blog
### Overview
**Microblog** is a small website made with Flask, similar to Twitter. It allows users to create an account, write short posts, and follow other users. Users can see their posts and the posts of people they follow in a timeline. The app also has features like user profiles, pagination to show posts in parts, and error handling. 
## Features
- User registration and login system
- Post creation and editing
- Follow and unfollow other users
- View posts from followed users in a timeline
- Paginated display of posts
- User profile pages with posts
- Password reset functionality
## Setup Instructions
1. **Clone the Repository:**
```bash
git clone https://github.com/miguelgrinberg/microblog.git
cd microblog
```
2. **Setting and Creating a Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Install Dependencies:**
```bash
pip install -r requirements/dev.txt
```
4. **Set Up Environment Variables:**
```bash
export FLASK_APP=microblog.py
```
5. **Deploy the ApplicationL:**
```bash
flask deploy
```
6. **Run the Application:**
```bash
flask run
```

## Usage
- **Sign Up and Login**

  Create a new account by clicking on the Sign Up link and filling in your details.
  After registering, log in using your username and password.

- **Create a Post**

  Once logged in, you can create a new post by typing your message into the text   box on the homepage and clicking Post.
  Your posts will appear on your profile page and the timeline.

- **Follow and Unfollow Users**

  Visit another user's profile by clicking on their username.
  You can follow or unfollow the user by clicking the Follow or Unfollow button on   their profile page.

- **View Timeline**

  The homepage shows your timeline, which includes posts from users you follow.
  Posts are displayed in reverse chronological order and can be navigated using pagination.

- **Edit Profile**

  You can edit your profile by clicking on your username in the navigation bar and  choosing the Edit Profile option.

- **Password Reset**

  If you forget your password, you can use the Forgot Password link on the login    page to request a password reset via email.

- **Log Out**

  To log out, click the Logout link in the navigation bar.
## Contribution Guidelines

- Reporting Issues: Please report any issues or bugs using the GitHub Issues tab.
- Submitting Pull Requests: Fork the repository, make your changes, and submit a pull request with a description of your changes.



