from flask import Flask, request, send_from_directory, Response
import os
from xml.etree.ElementTree import Element, SubElement, tostring

app = Flask(__name__)

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/generate', methods=['POST'])
def generate():
    title = request.form['title']
    artist_name = request.form['artist_name']
    isrc = request.form['isrc']
    upc = request.form['upc']

    song = Element('Song')

    artist = SubElement(song, 'Artist')
    name = SubElement(artist, 'Name')
    name.text = artist_name

    title_element = SubElement(song, 'Title')
    title_element.text = title

    identifier = SubElement(song, 'Identifier')
    upc_element = SubElement(identifier, 'UPC')
    upc_element.text = upc
    isrc_element = SubElement(identifier, 'ISRC')
    isrc_element.text = isrc

    xml_string = tostring(song, encoding='utf-8', method='xml')
    response = Response(xml_string, content_type='text/xml')
    response.headers['Content-Disposition'] = 'attachment; filename=song.xml'
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
