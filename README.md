<h1>twitter_unfollower</h1>
Python script using selenium. Logs into twitter and starts unfollowing all accounts you follow.
<br>Made to make the unfollow task faster.
The script logs in, pushes the first unfollow button, confirms the popup, reloads site. Rinse/repeat.
You can costumize how many unfollows to do.
<br>
Use it only for cleaning up your account.<br>
After 180 unfollows got kicked by twitter. Not sure for how long. (Back in after 10 minutes)
<br>
Clean up:<br><br>

![Before](https://i.imgur.com/8p051HB.png)

![After](https://i.imgur.com/t2UQG8y.png)

Use at your own risk!
<br>
<h2>Usage</h2>
Download the project
<br><pre>
pip install pipenv<br>
</pre>
or<br>
<pre>
pip3 install pipenv
pipenv shell
pipenv install
</pre>
There is also the chromedriver in the folder. And the script is set up to use it. But you can use your own. Just change the code. If you are new search - "chromedriver for selenium".<br> 
Version 83
<br>
<h2>Run it</h2>
<pre>
pipenv run python main.py
</pre>
<br>
<h3>Issues</h3>
Doesn't run in background.<br>
My code uses secret.py file with my login details. It is not shared. Just replace 
<pre>
secret.PASS
secret.USER
secret.MY_URL
</pre>
with your info to log in.
There are comments in the code file. Just follow the instructions.
