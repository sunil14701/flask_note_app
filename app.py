from website import create_app # we can do this as website is a python package because we put __init__.py file inside of a folder it becomes a python package . which means when we import the folder website than it will run the stuff in __init__py file . which means we can import anything which is defined in __init__.py file like our create file

app = create_app()

if __name__ == "__main__": # only if we run this file not if we import this file than only execute this file . as if we import the app.py to another folder than without this line app.run will be executed automatically . webserver will be run . we only want to run our webserver only when we run this app.py file 
    app.run(debug=True) # it is going to run our flask application . start a webserver and debug = True means every time we make a change to our python code than it is going to automatically rerun the webserver . we give this a false value when we run this in production . basically this is a entry point of our app
