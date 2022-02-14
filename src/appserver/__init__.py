from flask import Flask, request, jsonify, make_response
from werkzeug.exceptions import NotFound
from cuboid import Cuboid
from decimal import Decimal, InvalidOperation
import os
import mariadb

def create_api(test_config=None):
    api = Flask(__name__)
    api.config.from_envvar('CUBOID_CONFIG')

    try:
        conn = mariadb.connect(
            user=api.config['DB_USER'],
            password=api.config['DB_PASSWORD'],
            host=api.config['DB_HOST'],
            port=api.config['DB_PORT'],
            database=api.config['DB_DATABASE']        
        )
        api.config['CONN'] = conn

    except mariadb.Error:
        api.config['CONN'] = None
        print('Could not connect to database, proceeding with limited functionality')


    @api.route('/v1/cuboids', methods=['GET'])
    def get_cuboid():
        if len(request.args) == 0:
            return list_cuboids()

        valid = list()
        for a in ['a', 'b', 'c']:
            valid.append(validate(request.args.get(a)))

        cub = Cuboid(*valid)

        about_cuboid = {
            'cuboid': cub.__dict__,
            'volume': cub.volume(),
            'surface': cub.surface(),
            'perimeter': cub.perimeter()
        }

        if api.config['CONN']:
            cur = api.config['CONN'].cursor()
            cur.execute("REPLACE INTO cuboid(a, b, c, vol, surf, per) VALUES(?,?,?,?,?,?)",
                    *sorted(valid), cub.volume(), cub.surface(), cub.perimeter())

        r = make_response(jsonify(about_cuboid), 200)
        return r

        return r
        

    @api.errorhandler(NotFound)
    def not_found_handler(e):
        return jsonify(e.__dict__), 404

    return api


def list_cuboids():
    if api.config['CONN']:
        cur = api.config['CONN'].cursor()
        cur.execute("SELECT * FROM cuboid ORDER BY tstamp DESC LIMIT 30",
                *sorted(valid), cub.volume(), cub.surface(), cub.perimeter())
        for l in cur:
            res = dict(zip('a', 'b', 'c', 'volume', 'surface', 'perimeter'), l)

    r = make_response(jsonify(res), 200)
    return r


def validate(a):
    try:
        x = Decimal(a)
        if x <= 0:
            raise ValueError()
    except (ValueError, InvalidOperation):
        raise NotFound('All edges of a cuboid must be positive real numbers')
    return x

if __name__ == '__main__':
    create_api().run()
