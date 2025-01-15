# Windows HP templates route: C:\Users\HP\PycharmProjects\polytopia_python\app\templates
# Windows truncated templates route: C:\PycharmProjects\polytopia_python\app\templates
# relative templates route: polytopia_python\app\templates
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# add Index page, Privacy, Dashboard, About, Settings, HallOfFame and ThroneRoom routes! I have the content for them, you just make the routes and the navigation!

# Route for the homepage
@app.route("/")
def home():
    return (
        """
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="">
    <link rel="icon" href="{{ url_for('static', filename='img/chat_icon.jpg') }}">
    <title>Flask Chatbot Application</title>
</head>
<body>
{% extends "base.html" %}

{% block content %}
<header>Flask Chatbot Application</header>

<h1>Word in Context decision maker model</h1><p>The server is running at 127.0.0.1:5000</p>
<p>This is the Index page. Explore other sections using the navigation above.</p>
{% endblock %}
@{
	ViewData["Title"] = "Home Page";
}
<main id="chat-list">
    <button class="collapse-btn" onclick="toggleSidebar()">☰</button>
    <div class="chat-list-container">
        <h2 style="align-self: flex-start">Your chats will appear here</h2>
    </div>

    <div class="chat-container">
        <div class="message">Hello! How can I assist you today?</div>
        <!-- More messages will be dynamically added here -->
    </div>

    <div class="input-container">
        <form action="#" method="post">
            <label>
                <input type="text" placeholder="What would you like to ask?" style="width: 90%;"/>
            </label>
            <label for="submit">
            <button type="submit" name="submit" id="submit">Send
            </button>
            </label>
                <img src="../static/images/chat-icon.jpg" alt="Send" height="64px">
        </form>
    </div>
</main>
<footer style="text-align: center;">
    <section style="width: 80%; background-color: black; margin: auto; padding: 20px; border: 0;">
        <h2>Contact us:</h2>
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin-bottom: 10px;"><a href="mailto:meowuwuka@calculus.hu">meowuwuka@calculus.hu</a></li>
            <li style="margin-bottom: 10px;"><a href="https://www.facebook.com/meowuwuka">facebook.com/meowuwuka</a>
            </li>
            <li style="margin-bottom: 10px;"><a href="https://www.linkedin.com/in/meowuwuka">linkedin.com/meowuwuka</a>
            </li>
            <li style="margin-bottom: 10px;"><a href="https://www.meowuwuka.com">meowuwuka.com</a></li>
        </ul>
        <p>&copy; 2024 TryHard33. All rights reserved.</p>
    </section>
</footer>
<div class="text-center">
	<form action="/chat" method="post">
		<label for="my-chats" class="toggle">
			<input type="submit" name="my-chats" value="My chats" />
			<span class="toggle-btn">

			</span>

		</label>
	</form>

</div>
<style>

        body {
            font-family: Arial, sans-serif;
            background-color: #343541;
            color: #ffffff;
            margin: 0;
            padding: 0;
            flex-direction: column;
            height: 100vh;
        }

        header {
            background-color: #444654;
            padding: 20px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            border-bottom: 1px solid #282b30;
        }

        .chat-container {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }

        .input-container {
            background-color: #40414f;
            padding: 10px;
            display: flex;
            border-top: 1px solid #282b30;
        }

        .input-container input[type="text"] {
            flex: 1;
            padding: 10px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            outline: none;
            margin-right: 10px;
            width: 100%; /*Ensure that the text input is long enough to be visible on all screen sizes*/
        }

        .input-container button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #19c37d;
            border: none;
            border-radius: 5px;
            color: white;
            cursor: pointer;
        }

        .input-container button:hover {
            background-color: #13a369;
        }

        .message {
            background-color: #444654;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            max-width: 60%;
            word-wrap: break-word;
        }

        .user-message {
            align-self: flex-end;
            background-color: #1a7f65;
        }

        .chat-list-container {
        {#    width: 250px;#}{#    height: 100%;#}{#    background-color: #444654;#}{#    padding: 20px;#}{#    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.2);#}{#    display: flex;#}{#    flex-direction: column;#}{#    align-items: flex-start;#} flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: flex-start;
            width: 100%;
        }

        .chat-list-container h2 {
            color: #ffffff;
            font-size: 22px;
            margin-bottom: 20px;
        }

        .chat-list-container a {
            color: #ffffff;
            text-decoration: none;
            margin-bottom: 15px;
            font-size: 18px;
        }

        .chat-list-container a:hover {
            color: #19c37d;
        }

    </style>
    <script>
    function toggleSidebar() {
        const sidebar = document.getElementById('sidebar');
        sidebar.classList.toggle('collapsed');
    }
</script>
</body>
</html>
    """
            )

@app.route("/chat")
def chat():
    return ""

# Route for the Privacy page
@app.route("/privacy")
def privacy():
    return
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% extends "base.html" %}

{% block content %}
<h1>Privacy Policy</h1>
<p>This is the Privacy page content.</p>
{% endblock %}

</body>
</html>
"""

# Route for the Dashboard page
# TODO Fix error Template file 'dashboard. html' not found
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Route for the About page
@app.route("/about")
def about():
    return render_template("about.html")

# Route for the Settings page
@app.route("/settings")
def settings():
    return render_template("settings.html")




if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
