import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from myuser import MyGPU
from edit import Edit

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)


class View(webapp2.RequestHandler):
    def get(self,id):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        my=id
        if user:
            myuser_key=ndb.Key('MyGPU',my)
            myuser=myuser_key.get()
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'
        template_values = {'myuser':myuser,'my':my}
        template = JINJA_ENVIRONMENT.get_template('view.html')
        self.response.write(template.render(template_values))
    def post(self):
        self.response.headers['Content-Type']='text/html'
        if self.request.get('button')=='Cancel':
            # If the user hits the Cancel button we will simply redirect back to / as the user does not wish to update any data
            self.redirect('/') #redirecting
