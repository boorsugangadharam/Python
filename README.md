# Python

First select the source file of the current project<br>

#before that install git<br>
$ sudo apt-get install git<br>
<br>
#config git<br>
$ git config --global user.email "your@example.com"<br>
$ git config --global user.name "your name<br>

#first initiate git<br>
$ git init<br>
$ git add .<br>
$ git commit -m "first commit"<br>
$ git remote add origin Ex :https://github.com/boorsugangadharam/Python.git<br>
#this orgin version already exists<br>
#directly push the code <br>
$ git push -u origin master<br>

connect mongodb connection using python


Open up terminal and enter the following linux commands while changing your desired mongoDB version and Ubuntu release codename:

$ codename=xenial
$ mongodb=3.6

Once the above variables are set, simply enter the below command to import MongoDB release signing key:

$ wget -qO- https://www.mongodb.org/static/pgp/server-${mongodb}.asc | sudo apt-key add

Next, add the repository:

$ sudo bash -c "echo deb http://repo.mongodb.org/apt/ubuntu ${codename}/mongodb-org/$mongodb multiverse > /etc/apt/sources.list.d/mongodb-org.list"

update the repository index:

$ sudo apt update

Use the following linux command to install MongoDB on Ubuntu 18.04 Bionic server:

$ sudo apt-get install -y mongodb-org

Start MongoDB Database
After installation the MongoDB database does not start by default. To start the database enter:

$ sudo service mongod start

Confirm the MongoDB status: 

$ service mongod status


