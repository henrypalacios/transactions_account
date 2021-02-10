# Account Transactions

## Getting Started

The easy way to start using Docker containers.

Create a local copy of this repository and run

    docker-compose build

This spins up Compose and builds a local development environment according to
our specifications in [docker-compose.yml](docker-compose.yml).

After the containers have been built (this may take a few minutes), run

    docker-compose up

This one command boots up a local server for Flask (on port 5000)
and React (on port 3000). Head over to

    http://localhost:5000/
    http://localhost:3000/
