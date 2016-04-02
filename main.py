#Author = Anna Scheppele


import webapp2
import os
import logging
import jinja2
from google.appengine.api import mail

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #saving the path/page name as a variable
        url = self.request.path
        logging.info(url)
        #open the page with the url or open home page if that fails
        try:
            template = JINJA_ENVIRONMENT.get_template('templates' + url)
            self.response.write(template.render())
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())

        
#class for the login page
class FormHandler(webapp2.RequestHandler):
    #get method for when the page is first loaded
    def get(self):
        url = self.request.path
        try:
            template = JINJA_ENVIRONMENT.get_template('templates' + url)
            self.response.write(template.render())
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())

    def post(self):
        #post method for when the form is submitted
        url = self.request.path
        #saving the username and password as variables
        email = self.request.get("email1")
        pw = self.request.get("pw1")
        #dictionary to hold email and password data
        login_data = {"test@test.com":"testpass"}
        #if they are trying to log in
        if  (url =="/login.html"):
            #if email and password are correct, login
            if (email in login_data) and (login_data[email] == pw):
                logging.info("successful login")
                template = JINJA_ENVIRONMENT.get_template('templates/loggedin.html')
                self.response.write(template.render())
            #if password is incorrect
            elif (email in login_data) and (login_data[email] != pw):
                template = JINJA_ENVIRONMENT.get_template('templates/login.html')
                self.response.write(template.render({"fail": "Incorrect password, try again."}))
            #if email is not found
            elif (email not in login_data):
                template = JINJA_ENVIRONMENT.get_template('templates/login.html')
                self.response.write(template.render({"fail": "Incorrect email, try again."}))
        #if none of above, they are signing up
        else:
            #save the email and password in the dictionary
            login_data[email] = pw
            logging.info("saving email " + email + " and password " + pw)

            #sending an email confirming signing up to the user
            sender_email = "annascheppele@appname.appspotmail.com"
            subject = "Thank you for signing up on Anna Scheppele's Portfolio!"
            body = """Thank you for signing up and making an account! 
            There is no extra functionality for creating an account on my website, but it allows me to practice sending emails!"""
            mail.send_mail(sender_email, email, subject, body)
            #load the logged in page
            template = JINJA_ENVIRONMENT.get_template('templates/loggedin.html')
            self.response.write(template.render())


#creates the instances for webapp2
#all pages, except the login page(uses FormHandler), will use the MainHandler
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/work.html', MainHandler),
    ('/aboutme.html', MainHandler),
    ('/form.html', FormHandler),
    ('/login.html', FormHandler),
    ('/loggedin.html', FormHandler)
], debug=True)
