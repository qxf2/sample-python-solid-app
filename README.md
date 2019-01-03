# sample-python-solid-app
A sample Python Flask app Qxf2 wrote to tinker with Inrupt's Solid. The application loads the Full Name and friends webID lists for the given URI

For convenience, this app will be shortly hosted at pythonanywhere.com

<strong>Pre-requisites</strong>: In order to read and write data, you need your own Solid POD and identity. Create a POD from <a href="https://solid.inrupt.com/get-a-solid-pod">Get a Solid POD</a> 

To brief, our sample python solid web application does the following: 

1. Gets the user input 'Profile' webID using the HTTP Get method.
2. Based on this webID, reads data from a Solid pod.
3. Creates a RDF Graph
4. Parse the data returned into a graph 
5. Get the friends lists for the given webID
6. Display the returned friends list on the browser 

## Setup
 
1. To get started, download and install some RDF data.

 `pip install rdflib`

2. Create a Solid POD from <a href="https://solid.inrupt.com/get-a-solid-pod">Get a Solid POD</a>
3. Clone the repo - https://github.com/qxf2/sample-python-solid-app


## How to run the Sample python solid profile viewer application

To start the application, 

1. Run `python sample_python_solid.py` from the console.
2. Visit `localhost:6464` in your browser. 
3. Give the webID as input and click on the 'View' button