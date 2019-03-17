import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from myuser import MyGPU
from edit import Edit
from view import View
from update import Update
from query import Query
from compare import Compare

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        url = ''
        url_string = ''
        welcome = 'Welcome back'
        myuser=None
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'LOGOUT'
            myuser_key = ndb.Key('MyGPU',user.user_id())
            myuser = myuser_key.get()
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'Login'
        result=MyGPU.query().fetch()
        template_values = {'url' : url,'url_string' : url_string,'user' : user,'welcome':welcome,'myuser':myuser,'result':result}
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))
    def post(self):
        self.response.headers['Content-Type']='text/html'
        if self.request.get('button')=='Create':
            user=users.get_current_user()
            name=self.request.get('users_name')
            name1=name.upper()
            name=name1
            myuser_key=ndb.Key('MyGPU',name)
            myuser=myuser_key.get()
            if myuser==None:
                myuser=MyGPU(id=name)
                myuser.put()
                myuser_key=ndb.Key('MyGPU',name)
                myuser=myuser_key.get()
                myuser.name=name
                myuser.manufacturer=self.request.get('users_manufacturer')
                myuser.date=self.request.get('users_date')
                myuser.put()
                self.redirect('/')
            else:
                self.redirect('/un')
        if self.request.get('button')=='Query':
            self.redirect('/query')
        if self.request.get('button')=='Result':
            self.redirect('/query')
        if self.request.get('button')=='Compare':
            self.redirect('/compare')




class Username(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        self.response.write("Username is already taken<br/>")
        self.response.write('<a href="/"> HomeScreen </a><br/>')
        self.response.out.write('</html></body>')


class Finalcompare(webapp2.RequestHandler):
    def get(self,id,id1):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        my=id
        my1=id1
        if user:
                myuser_key=ndb.Key('MyGPU',my)
                myuser=myuser_key.get()
                myuser_key1=ndb.Key('MyGPU',my1)
                myuser1=myuser_key1.get()
        else:
                url = users.create_login_url(self.request.uri)
                url_string = 'login'
        template_values = {'myuser':myuser,'myuser1':myuser1}
        template = JINJA_ENVIRONMENT.get_template('finalcompare.html')
        self.response.write(template.render(template_values))


class Sorr(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        self.response.write("<u><h1><center>BOTH OPTION CANNOT BE SAME</center></h1><br/></u>")
        self.response.write('<center><h2><a href="/compare"> TRY AGAIN </a><br/></h2></center>')
        self.response.write('<center><h2><a href="/"> HomeScreen </a><br/></h2></center>')
        self.response.write('<hr/>')
        self.response.out.write('</html></body>')




app = webapp2.WSGIApplication([('/', MainPage),('/view/(.*)',View),('/update/(.*)',Update),('/un',Username),('/query',Query),('/compare',Compare),('/finalcompare/(.*)/(.*)',Finalcompare),('/sorry',Sorr)], debug=True)
