import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from myuser import MyGPU
from edit import Edit
from view import View
from update import Update

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),extensions=['jinja2.ext.autoescape'],autoescape=True)

class Query(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        self.response.write('<u><h1><center>FINDING THE EXACT GPU NAME:</center></h1></u>')
        self.response.out.write('<form method="get" action="/query">')
        self.response.out.write('<table border="1">')
        self.response.out.write('<tr><th>GPU FEATURES</th><th>INFORMATION</th></tr>')
        self.response.out.write('<tr><td>geometryShader:</td><td><input type="checkbox" name="users_geometryShader" /></td></tr>')
        self.response.out.write('<tr><td>tesselationShader:</td><td><input type="checkbox" name="users_tesselationShader" /></td></tr>')
        self.response.out.write('<tr><td>shaderInt16:</td><td><input type="checkbox" name="users_shaderInt16" /></td></tr>')
        self.response.out.write('<tr><td>sparseBinding:</td><td><input type="checkbox" name="users_sparseBinding" /></td></tr>')
        self.response.out.write('<tr><td>textureCompressionETC2:</td><td><input type="checkbox" name="users_textureCompressionETC2" /></td></tr>')
        self.response.out.write('<tr><td>vertexPipelineStoresAndAtomics:</td><td><input type="checkbox" name="users_vertexPipelineStoresAndAtomics" /></td></tr>')
        self.response.out.write('<tr><td>RESULT</td><td><input type="submit" value="Query" name="button"/></td></tr>')
        self.response.out.write('</form>')
        if self.request.get("users_geometryShader"):
            geometryShader=True
        else:
            geometryShader=False
        if self.request.get("users_tesselationShader"):
            tesselationShader=True
        else:
            tesselationShader=False
        if self.request.get("users_shaderInt16"):
            shaderInt16=True
        else:
            shaderInt16=False
        if self.request.get("users_sparseBinding"):
            sparseBinding=True
        else:
            sparseBinding=False
        if self.request.get("users_textureCompressionETC2"):
            textureCompressionETC2=True
        else:
            textureCompressionETC2=False
        if self.request.get("users_vertexPipelineStoresAndAtomics"):
            vertexPipelineStoresAndAtomics=True
        else:
            vertexPipelineStoresAndAtomics=False
        self.response.write('<caption align="bottom"><hr/></caption>')
        self.response.write("<caption align='bottom'><a href='/'><h2> Homescreen</h2> </a></caption>")
        if self.request.get('button')=='Query':
                #query = Article.query(ndb.AND(Article.tags == 'python',ndb.OR(Article.tags.IN(['ruby', 'jruby']),ndb.AND(Article.tags == 'php',Article.tags != 'perl')))) """
                a=[]
                a1=[]
                a2=[]
                a3=[]
                a4=[]
                a5=[]
                a6=[]
                z=0
                if geometryShader==True:
                    z=z+1
                if tesselationShader==True:
                    z=z+1
                if shaderInt16==True:
                    z=z+1
                if sparseBinding==True:
                    z=z+1
                if textureCompressionETC2==True:
                    z=z+1
                if vertexPipelineStoresAndAtomics==True:
                    z=z+1
                if z<=1:
                    if geometryShader==True:
                        a1=MyGPU.query(MyGPU.geometryShader==True).fetch()
                    if tesselationShader==True:
                        a2=MyGPU.query(MyGPU.tesselationShader==True).fetch()
                    if shaderInt16==True:
                        a3=MyGPU.query(MyGPU.shaderInt16==True).fetch()
                    if sparseBinding==True:
                        a4=MyGPU.query(MyGPU.sparseBinding==True).fetch()
                    if textureCompressionETC2==True:
                        a5=MyGPU.query(MyGPU.textureCompressionETC2==True).fetch()
                    if vertexPipelineStoresAndAtomics==True:
                        a6=MyGPU.query(MyGPU.vertexPipelineStoresAndAtomics==True).fetch()
                    d=[]
                    a=a1+a2+a3+a4+a5+a6
                    for i in a:
                        if i in d:
                            print ''
                        else:
                            d.append(i)
                    for i in d:
                                self.response.write('<caption align="bottom"><b>%s</b></caption>'%(i.name))
                else:
                    q=MyGPU.query(ndb.AND(MyGPU.geometryShader==geometryShader,ndb.AND(MyGPU.vertexPipelineStoresAndAtomics==vertexPipelineStoresAndAtomics,ndb.AND(MyGPU.tesselationShader==tesselationShader,ndb.AND(MyGPU.shaderInt16==shaderInt16,ndb.AND(MyGPU.sparseBinding==sparseBinding,ndb.AND(MyGPU.textureCompressionETC2==textureCompressionETC2))))))).fetch()
                    for i in q:
                                self.response.write('<caption align="bottom"><b>%s</b></caption>'%(i.name))

                self.response.write('<hr/>')
                self.response.out.write('</html></body>')
