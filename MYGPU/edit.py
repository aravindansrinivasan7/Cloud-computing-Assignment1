import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
from myuser import MyGPU

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class Edit(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        user=users.get_current_user()
        myuser_key=ndb.Key('MyGPU',user.user_id())
        myuser=myuser_key.get()
        template_values={'myuser':myuser}
        template=JINJA_ENVIRONMENT.get_template('edit.html')
        self.response.write(template.render(template_values))
    def post(self):
        self.response.headers['Content-Type']='text/html'
        if self.request.get('button')=='Update':
            user=users.get_current_user()
            name=self.request.get('users_name')
            myuser_key=ndb.Key('MyGPU',name)
            myuser=myuser_key.get()
            if myuser==None:
                myuser=MyGPU(id=name)
                myuser.put()
            myuser_key=ndb.Key('MyGPU',name)
            myuser=myuser_key.get()
            myuser.name=self.request.get('users_name')
            myuser.manufacturer=self.request.get('users_manufacturer')
            myuser.date=self.request.get('users_date')
            myuser.put()
            self.redirect('/')
        elif self.request.get('button')=='Cancel':
            # If the user hits the Cancel button we will simply redirect back to / as the user does not wish to update any data
            self.redirect('/') #redirecting
