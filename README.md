### GeoLoc

# setting up virtual environment
    
    prerequisites 
    python3 install
    pip(package installer) install

    first create a virtual environment using python3, 
    $ virtualenv -p path-to-python3 path-for-virtualenv-folder
    eg.
    $ virtualenv -p /usr/bin/python3.6 ./../venv

    then activate it
    $ source path-to-virtualenv/bin/activate
    eg. 
    $ source ./../venv/bin/activate

    install the required packages,
    $ pip install -r requirement.txt


# running the migrations

    to process the unmigrated files do,
    $ python manage.py migrate


# starting the server

    run migration to avoid unwanted behaviour,
    run the following command to start the server
    $ python manage.py runserver
