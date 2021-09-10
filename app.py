import enum
from flask import Flask, request, jsonify


app = Flask(__name__)


# dummy data for testing 
composers_list = [
    {
        "id" : 1,
        "name" : "John Williams",
        "movies": "Jaws, Star Wars, Jurassic Park, Harry Potter"

    },
    {
        "id": 2,
        "name" : "John Powell",
        "movies": "How To Train Your Dragon"
    },
    {   
        "id": 3,
        "name" : "Joe Hisaishi",
        "movies": "Spirited Away, Howl's Moving Castle"
    }]


@app.route('/')
@app.route('/home')
def index():
    return ('Hello World')



@app.route('/composers', methods=['GET', 'POST'])
def composers():
    '''Create (POST) and Read (GET)'''
    # Read
    if request.method == 'GET':
        if len(composers_list) > 0:
            return jsonify(composers_list)
        else:
            return 'Nothing\'s there', 404
    # Create
    if request.method == 'POST':
        id = composers_list[-1]['id'] + 1
        
        name = request.form['name']
        movies = request.form['movies']
        
        new_object = {
            "id" : id,
            "name" : name,
            "movies": movies
        }
        
        composers_list.append(new_object)
        return jsonify(composers_list), 201


@app.route('/composers/id/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_composer(id):
    '''Read (GET), Update (PUT) and Delete (DELETE) methods using an id of the composer
       Update (PUT) method will replace all the old data with the new data provided, 
       witch exception of id which will stay the same
    '''
    # Read
    if request.method == 'GET':
        for composer in composers_list:
            if composer['id'] == id:
                return jsonify(composer)
    # Update
    elif request.method == 'PUT':
        for composer in composers_list:
            if composer['id'] == id:
                composer['name'] = request.form['name']
                composer['movies'] = request.form['movies']

                updated_object = {
                    'id': id,
                    'name': composer['name'],
                    'movies': composer['movies']
                }
                return jsonify(updated_object)
    # Delete
    elif request.method == 'DELETE':
        for index, composer in enumerate(composers_list):
            if composer['id'] == id:
                composers_list.pop(index)
                
                return jsonify(composers_list)


@app.route('/urltest/<name>/<second_name>')
def print_name(name, second_name):
    return f'URL: .../urltest/{name}/{second_name}'


if __name__ == '__main__':
    app.run(debug=True)
