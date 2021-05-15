# kanban-challenge
Coding challenge for lightfeather.io

While a proper installion of this project would require configuring a web server for access, along with reverse-proxy to the flask app, using it locally is straightforward and can be done with only a web browser, python3, and pip. Assuming those requirements are met, the process to test the page and service are as follows:

The server requires flask, and flask-cors, and needs to have some environmental variables set. Put main.py and conf.json in the same directory, open your shell, and enter the following (assuming you're on Windows):

  pip install flask
  
  pip install flask-cors

  set FLASK_APP=main
  
  set FLASK_RUN_PORT=23456

  flask run
  
And that's it. The server is now running and index.html should function in any web browser (except IE, and possibly some versions of safari).

To be totally honest, I've never written javascript from scratch before, and I haven't touched css in over a decade, and that's all painfully obvious looking at my submission. The code in index.html literally improves between functions and elements as I learned  more about this technology over the past few days, like the fact that fetch is now a thing. I was done with the backend in a couple of hours, although it helped that I had an existing flask application I had just built for a client to expand on, but I put a disquieting amount of time into the page. That said, I hope that Sarah was right, and that you might be impressed that someone whose last webpage was https://people.clarkson.edu/~schayae/ took a shot at this challenge (trying to be funny and seem human doesn't hurt either, right?).

Frankly, I think I'm going to go back in and try to refactor this into something less... disgusting to try and earn some brownie points.

I hope that this work is acceptable, look forward to the opportunity to speak in the future.
