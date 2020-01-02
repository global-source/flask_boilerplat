## Flask Boilerpalt
Ready to go with Flask

## 1. To Setup Your Environment

### For Virtual Environment

#### Debian, Ubuntu
`$ sudo apt-get install python-virtualenv`

#### CentOS, Fedora
`$ sudo yum install python-virtualenv`

#### Arch
`$ sudo pacman -S python-virtualenv`

If you are on Mac OS X or Windows, download get-pip.py, then:

`$ sudo python2 Downloads/get-pip.py`

`$ sudo python2 -m pip install virtualenv`

### For Project Dir

`$ mkdir your-project-name`

`$ cd your-project-name`

`$ python3 -m venv venv`

#### On Windows:

`$ py -3 -m venv venv`

If you needed to install virtualenv because you are using Python 2, use the following command instead:

`$ python2 -m virtualenv venv`

#### On Windows:

`> \Python\Scripts\virtualenv.exe venv`

### Activate the environment
Before you work on your project, activate the corresponding environment:

`$ . venv/bin/activate`
#### On Windows:

`> venv\Scripts\activate`

#### To install required 'pip' bundles. 

Move to boilerplate's root directory and execute the following.

` pip install -r requirements.txt `

## 2. To start your Flask boilerplate
It will set the application to execute

#### Linux
`$ export FLASK_APP main.py`

#### Windows
`> set FLASK_APP main.py`

### To set Environment
It will allow you to manage your application behaviour with different environment.
#### Linux
`$ export FLASK_ENV development`

#### Windows
`> set FLASK_ENV development`

### To enable Debug
It will allow us to do application debug during execution.
#### Linux
`$ export FLASK_DEBUG=1`

#### Windows
`> set FLASK_DEBUG=1`

### To Run Flask boilerplate
It will run the Flask application based on your configurtion/env-variables that have been assigned.

` flask run`

