#Author = Anna Scheppele


import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #saving the path/page name as a variable
        url = self.request.path
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
        logging.info("opening login page")
        template = JINJA_ENVIRONMENT.get_template('templates/form.html')
        self.response.write(template.render({'title': 'Login'}))

    def post(self):
        #post method for when the form is submitted
        #saving the username and password as variables
        name = self.request.get("name")
        pw = self.request.get("pw")
        #if username and pass are correct, show login.html
        if (name == "Colleen") and (pw == "pass"):
            logging.info("successful login")
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({'title': 'Logged in'}))
        #if username and pass are incorrect, reload the form and show a fail message    
        else:
            logging.info("bad username: " + name + ", bad pass: " + pw)
            template = JINJA_ENVIRONMENT.get_template('templates/form.html')
            self.response.write(template.render({'title': 'Login'}))


#creates the instances for webapp2
#all pages, except the login page(uses FormHandler), will use the MainHandler
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/family.html', MainHandler),
    ('/dogs.html', MainHandler),
    ('/form.html', FormHandler),
    ('/login.html', FormHandler)
], debug=True)
