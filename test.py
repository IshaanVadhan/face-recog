from flask import Flask,Response
import csv

app = Flask(__name__)
@app.route('/')
def generate_large_csv():

    recs = [{'big': 200, 'small': 56, 'large': 2009}, 
            {'big': 444, 'small': 34, 'large': 7777}]

    with open('unique-filename.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(recs)

    with open('unique-filename.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print 'row', row 
        def generate():
            for row in reader:
                print 'grow', grow
                yield ','.join(row) + '\n'

        return Response(generate(), mimetype='text/csv')