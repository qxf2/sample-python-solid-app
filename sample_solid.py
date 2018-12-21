"""
This is a Flask application for Inrupt Solid profile viewer. 

"""

from flask import Flask, jsonify, render_template, request
import json
import logging
import urllib2
import rdflib   
from rdflib import URIRef,Graph,RDF
from rdflib.namespace import FOAF


app = Flask(__name__)

def post_friends_list(uri):
    "create,parse graph and get the friends list for the given URI"
    # Create a Empty graph      
    graph = rdflib.Graph()   
    graph.parse(uri)   
    for person in graph[: RDF.type: FOAF.Person]:
        name = graph.value(person, FOAF.name)             
        friends = list(graph[person:FOAF.knows])
        app.logger.info('%s friends', friends)
        if friends:
            app.logger.info("%s's friends:", graph.value(person, FOAF.name))           

        return friends,name          


@app.route("/", methods=['GET','POST'])
@app.route("/view", methods=['GET','POST'])
def view():
    "Endpoint for getting the friends list for the given URI"
    if request.method == 'GET':
        #return the form
        return render_template('sample_solid.html')
    if request.method == 'POST':
        #return the answer
        uri = request.form.get('profile')        
        result,name = post_friends_list(uri)        
        api_response = {"answer": result, 
                        "name": name}        
        return jsonify(api_response)
            
   
#---START OF SCRIPT
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6464, debug= True)