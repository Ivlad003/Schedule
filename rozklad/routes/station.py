import re

from rozklad.app import app, mysql, jsonify


@app.route("/stations/<idl>/<idr>")
def stationsByRIds(idl,idr):
    cursor = mysql.connect().cursor()
    sql = "select * from station where  route_id=" + idl +" or route_id="+ idr +" ORDER BY number_of_station"
    cursor.execute(sql)
    data = cursor.fetchall()
    list = parseData(data)
    return jsonify(list)

def parseData(data):
    list = []
    n=0
    for row in data:
        station = {}
        station['route_id'] = row[2]
        station['name'] = row[3].encode('utf-8')
        station['number'] = row[4]
        station['interval_test'] = row[5].encode('utf-8')
        result = re.findall(r':\d{2}:', row[5].encode('utf-8'))
        result = re.findall(r'\d',result[0])
        n += int(result[1])
        station['interval'] = n * 60 * 1000
        list.append(station)
    return list


