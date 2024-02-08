# Warehouse manager

A simple warehouse manager written with Flask, which hold articles, and the articles contains an identification number, a name and available stock. 
It also has products, products are made of different articles. Products have a name, price and a list of articles of which they are made from with a quantity. 
It loads articles and products into the software from [json files](db_samples), at the start of the software, so every time the software starts, it will have the same data.

It provides two main endpoints:
* Get all products and quantity of each that is an available with the current inventory
* Sell a product and update the inventory accordingly
</br>


### Requirements:
1. install [docker](https://docs.docker.com/desktop/install/linux-install) 
2. install [docker-compose](https://docs.docker.com/compose/install/).


### How to run:
* run ```make run-server```.


### How to run tests:
* run ```pytest``` at project directory.


### Further info:
This Project is a simple warehouse manager, its dependency is **PostgreSQL** database, so if you are not using docker-compose or instructions above for running the project
you need to run a postgresql somewhere that be accessible by service. </br>
By default if you use docker to run the project, docker-compose command will bring up a **PostgreSQL** database first and then connects the service to it.


## Endpoints
1. ```GET /``` used for getting all products and quantity of availability.
2. ```Get /sell/<productId>``` used for selling a product.
