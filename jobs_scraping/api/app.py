from flask import Flask, jsonify, request
import pandas as pd
from flask import Response

app= Flask(__name__)
records = pd.read_csv(r'C:\Users\jacoo\OneDrive\Desktop\jobs_scraping\api\data.csv')

@app.route('/brigada_data/<city>/<max_results>')
def profile(city, max_results):
    max_results = int(max_results)
    to_send = records[(records['place'] == city)]
    if len(to_send)> max_results:
        to_send = to_send[:max_results]

    return Response(to_send.to_json(orient="records"), mimetype='application/json')#f'{username}\'s profile {other_thing}'
#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)