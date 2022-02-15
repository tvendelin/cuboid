# Cuboid 

Calculates volume, surface area and sum of all sides of a rectangular cuboid.
Can be used as a CLI utility or as ReSTful API server optionally backed with MariaDB database.

## Building

The following implies using `bash` on a (Debian) Linux box. On Mac, install the necessary libraries and
utilities using `macPorts`, `homebrew`, or what have you got. The steps should be similar, but
figure out what the names of the ports are.

The packages required on Debian (and likely Ubuntu) are:

- 'git'
- 'make'
- 'python3-pip'
- 'python3-venv'
- 'libpcre3' 
- 'libpcre3-dev'
- 'libmariadb-dev'

Clone the project, change into project directory, and run

```
make
```

This creates a `wheel` and a `tar.gz` files under `dist` directory and HTML docs
under `html`.

## Install 

using `pip` anywhere on your computer:

```
# create a virtual environment, "v" is an example
python3 -m venv v 

# activate it
. v/bin/activate

# install (the version might differ)
pip install cuboid-0.1.15-py3-none-any.whl
```

## Running from Command Line

Given that Cuboid is installed in virtual environment `v`, run

```
# activate virtual environment
. v/bin/activate

# run thi CLI utility
cuboid
```

and follow on-screen instructions. Alternatively, just

```
v/bin/cuboid
```

## A Standalone uWSGI Web Server

### API

```
GET /v1/cuboids?a=<value>&b=<value>&c=<value>
```

Returns a JSON string containing cuboid sides, volume, surface, perimeter.
If the server is backed with a database, all cuboid properties will be stored
with a timestamp. Should the same cuboid will be requested again, the timestamp
will be updated. The database backend is _not used_ as cache, as computing is faster.

```
GET /v1/cuboids
```

Returns a list of the last 30 viewed cuboids, if the app is backed with a database,
or an empty list otherwise.

### Trying Out (Not a Production Scenario)

Create (or touch) a configuration file. If you happen to have a MariaDB server fro testing,
the configuration file looks like:

```
DB_USER="<user>"
DB_PASSWORD="<app_password>"
DB_HOST="localhost"
DB_PORT=3306
DB_DATABASE="<some_name>"
```

Export path to the config file (even if empty):

```
export CUBOID_CONFIG='/path/to/config'
```

Run (from virtual environment)

```
uwsgi --socket localhost:5000 --protocol=http -w appserver.wsgi:app
```
