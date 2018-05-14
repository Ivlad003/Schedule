from rozklad.app import app, mysql, jsonify

@app.route("/time/<idl>/<idr>")
def timeByRIds(idl,idr):
    cursor = mysql.connect().cursor()
    sql = "select * from time where  route_id=" + idl +" or route_id="+ idr
    cursor.execute(sql)
    data = cursor.fetchall()
    list = parseData(data)
    return jsonify(list)

def parseData(data):
    list = []
    for row in data:
        time = {}
        time['route_id'] = row[1]
        time['time'] = row[2].encode('utf-8')
        time['weekend'] = bytearray(row[3])[0]
        time['number'] = bytearray(row[4])[0]
        time['winter_table'] = bytearray(row[5])[0]
        time['in_depot'] = bytearray(row[6])[0]
        list.append(time)
    return list


