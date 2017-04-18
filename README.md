basic.py
========
-> Basic flask app
-> HTTP GET requests
-> Function url_for


A basic flask application with four routes:

  1.      /                       index()
  2.      /user/<username>        show_user_profile(username)
  3.      /number/<int:n>         number(n)
  4.      /url_for_index          url_for_index()


Each of these routes are delivered through HTTP GET requests.

The url_for function converts a function and its arguments into a URL.









template.py
===========
- Function render_template
- Two routes to one function
- Variable substituion within templates


A flask application that displays its HTML by rendering a template (templates/hello.jinja2).




form.py
=======
- Function request
- HTTP Post request
- HTML Form

Information is retrieved from a web server using GET.  Information is sent to a web server using POST.
A GET request can be used to encode information in the URL, e.g. htttp://www.mysite.com/john
An HTML Form is the most common way for a web client to generate a POST request.

   <form action="call this URL on submit" method="POST">
     <input type="text" name="username"/>
     <button type="submit">Press Me</button>
   </form>


The first call /login is a GET request and causes login.jinga to be served.

The next call to /login occurs when the user presses "Press Me" and is a POST request.
This request.form is populated and "User <username> logged in" is served.a

The challenge is successfully logging in leaves the user at /login



post.py
=======
- Functions redirect, flash

The GET request /login works exactly as it did before.  That is, it renders a form (with a POST action).
The POST request is different.  It re-directs the request to a different URL but maintains the header.

The other new feature used here is the flash() function.  The flash() function stores a string (message)
in a list (messages) that can be accessed from the template (using get_flashed_message).




inherit.py
==========
