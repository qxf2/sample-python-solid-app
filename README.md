# sample-python-solid-app
A sample Python Flask app Qxf2 wrote to tinker with Inrupt's Solid

<strong>Pre-requisites</strong>: In order to read and write data, you need your own Solid POD and identity. Create a POD from <a href="https://solid.inrupt.com/get-a-solid-pod">Get a Solid POD</a> 

To brief, our sample solid web application does the following: 

1. Gets the user input 'Profile' webID using the HTTP Get method.
2. Based on this webID, reads data from a Solid pod.
3. Creates a RDF Graph
4. Parse the data returned into a graph 
5. Get the friends lists for the given webID
6. Display the returned friends list on the browser 

To get started, download and install some Python modules. While there are several Python modules for working with RDF data, we used <a href="https://github.com/RDFLib/rdflib">RDFLib</a>. The RDFLib module provides a powerful set of tools for creating, parsing, traversing and editing RDF data.
