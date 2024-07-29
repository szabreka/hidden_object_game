# app.py
from flask import Flask, render_template
from obj_det import top_5_entries, get_xy_data, top_5_coordinates, get_image_shape, get_corner_data, top_5_corners, top_5_coords, context_df
from obj_det2 import top_5_entries2, get_xy_data2, top_5_coordinates2, get_image_shape2, get_corner_data2, top_5_corners2, top_5_coords2, context_df
from rijksapi import importing_art
from parser import riddle1, riddle2, riddle3, riddle4, riddle5, riddle6, riddle7, riddle8, riddle9, riddle10, answer1, answer2, answer3, answer4, answer5


 
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/game')
def game():
    get_xy_data(top_5_entries)
    get_corner_data(top_5_coords)
    shape = get_image_shape()

    object_data_list = []

    # API key for Rijksmuseum
    your_key = "your key"

    # list with paintings 
    object_ids = ["SK-C-229"]

    # get artwork information
    artwork_info = importing_art(your_key, object_ids)[object_ids[0]]
    title = artwork_info[2]
    artist = artwork_info[3]
    description = artwork_info[4]

    for i in range(5):
        object_data_list.append({
            f'x_coordinates': top_5_coordinates[i][1],
            f'y_coordinates': top_5_coordinates[i][2],
            f'label_data': top_5_coordinates[i][0],
            f'top_left_x': top_5_corners[i][0],
            f'top_left_y': top_5_corners[i][1],
            f'bottom_right_x': top_5_corners[i][2],
            f'bottom_right_y': top_5_corners[i][3]
        })

    return render_template('image_map.html',
                           object_data_list=object_data_list,
                           original_width = shape[1],
                           original_height = shape[0],
                           title = title,
                           artist = artist,
                           description = description, 
                           riddle1=riddle1,
                            riddle2=riddle2,
                            riddle3=riddle3,
                            riddle4=riddle4,
                            riddle5=riddle5,
                            answer1=answer1,
                            answer2=answer2,
                            answer3=answer3,
                            answer4=answer4,
                            answer5=answer5)

@app.route('/success')
def success():

    # list with paintings 
    object_ids = ["SK-C-229"]

    historical_context = context_df[object_ids[0]][0]

    # API key for Rijksmuseum
    your_key = "your key"
    
    # get artwork information
    artwork_info = importing_art(your_key, object_ids)[object_ids[0]]
    title = artwork_info[2]
    artist = artwork_info[3]
    description = artwork_info[4]    

    return render_template('success.html',
                           description = historical_context,
                           title = title,
                           artist = artist)


@app.route('/newgame')
def newgame(): 
    return render_template('index2.html')

@app.route('/game2')
def game2():
    get_xy_data2(top_5_entries2)
    get_corner_data2(top_5_coords2)
    shape = get_image_shape2()

    object_data_list = []

    # API key for Rijksmuseum
    your_key = "your key"

    # list with paintings 
    object_ids = ["SK-A-4821"]

    # get artwork information
    artwork_info = importing_art(your_key, object_ids)[object_ids[0]]
    title = artwork_info[2]
    artist = artwork_info[3]
    description = artwork_info[4]

    for i in range(5):

        object_data_list.append({
            f'x_coordinates': top_5_coordinates2[i][1],
            f'y_coordinates': top_5_coordinates2[i][2],
            f'label_data': top_5_coordinates2[i][0],
            f'top_left_x': top_5_corners2[i][0],
            f'top_left_y': top_5_corners2[i][1],
            f'bottom_right_x': top_5_corners2[i][2],
            f'bottom_right_y': top_5_corners2[i][3]
        })

    return render_template('image_map2.html',
                           object_data_list=object_data_list,
                           original_width = shape[1],
                           original_height = shape[0],
                           title = title,
                           artist = artist,
                           description = description, 
                           riddle1=riddle6,
                            riddle2=riddle7,
                            riddle3=riddle8,
                            riddle4=riddle9,
                            riddle5=riddle10,
                            answer1=answer1,
                            answer2=answer2,
                            answer3=answer3,
                            answer4=answer4,
                            answer5=answer5)

@app.route('/success2')
def success2():

    # list with paintings 
    object_ids = ["SK-A-4821"]

    historical_context = context_df[object_ids[0]][0]

    # API key for Rijksmuseum
    your_key = "your key"
    
    # get artwork information
    artwork_info = importing_art(your_key, object_ids)[object_ids[0]]
    title = artwork_info[2]
    artist = artwork_info[3]
    description = artwork_info[4]    

    return render_template('success2.html',
                           description = historical_context,
                           title = title,
                           artist = artist)

if __name__ == '__main__':
    app.run(debug=True)



