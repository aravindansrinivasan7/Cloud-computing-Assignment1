import webapp2
import cgi, cgitb
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from myuser import MyGPU
from edit import Edit
from view import View
from update import Update

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class Compare(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        self.response.out.write('<h1><center>PLEASE CHOOSE TWO GPU DATASTORE:</center></h1>')
        result=MyGPU.query().fetch()
        s=None
        form = cgi.FieldStorage()
        self.response.write('<form method="get" action="/compare">')
        self.response.write('<center><h2><select name = "dropdown">')
        for i in result:
            self.response.write('<option value = "%s">%s</option>'%(i.name,i.name))
        self.response.write('</select></h2>')
        self.response.write('<select name = "dropdown1">')
        for i in result:
            self.response.write('<option value = "%s">%s</option>'%(i.name,i.name))
        self.response.write('</select><br/><br/>')
        self.response.out.write('<input type="submit" value="Compare" name="button"/>')
        self.response.out.write('</form></center>')
        if form.getvalue('dropdown'):
            s=form.getvalue('dropdown')
            t=form.getvalue('dropdown1')
        else:
            s="hello"
        if self.request.get('button')=='Compare':
            s=form.getvalue('dropdown')
            t=form.getvalue('dropdown1')
            if s==t:
                self.redirect('/sorry')
            else:
                self.redirect('/finalcompare/%s/%s'%(s,t))
        self.response.write("<h2><center><a href='/'> Homescreen </a><br/></center></h2>")
        self.response.write('<hr/>')
