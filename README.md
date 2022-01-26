# python_server_testing

## Author
  * Numan SAHNOU

# To install :
  * `pip install -r requirements.txt`

## Work to do :
You are to create a python website, using flask, that calculates the mean of GET requests containing a list of numbers. The website should be dockerized, and built using docker compose. Then you will create a testing file, using the python library pytest, and these tests should cover: The site working: 
- a test that calls the website's url and confirms a code reply of 200. The site output is correct: 
- a test that sends a GET request to the website and confirms that the website returns the correct answer. 
- The site can handle stress: the average response time of the site should be below 100 ms per request, when 1000 requests are sent per second.

## How to run the application :
* Build the application with docker : `docker build . -t python_server_testing_image`
* Run the application with docker : `docker run -p 5000:5000 python_server_testing_image`
* Build the application with docker compose : `docker-compose up`
* Try GET requests: `http://localhost:5000/mean?list=1&list=2&list=3&list=4`
* Execute tests : `pytest .`
webhook jenkins
