from rozklad.app import app, mysql, jsonify

@app.route("/transport/<id>")
def transport(id):
    cursor = mysql.connect().cursor()
    sql = "select * from route where type_transport_id=" + id + " ORDER BY number"
    cursor.execute(sql)
    data = cursor.fetchall()
    list = parseData(data)
    return jsonify(list)
                                                
def parseData(data):
    dictonary = {}
    for row in data:
        transport = {}
        if dictonary.get(row[3], None) == None:
            transport['name_route'] = row[2].encode('utf-8')
            transport['number_route'] = row[3]
            transport['number'] = row[6]
            transport['route_id_from'] = row[1]
            transport['transport_id'] = row[5]
    	    dictonary[row[3]] = transport
        else:
            transport = dictonary[row[3]]
            transport['name_route'] = row[2].encode('utf-8')
            transport['number_route'] = row[3]
            transport['route_id_to'] = row[1]
            transport['transport_id'] = row[5]
	    dictonary[row[3]] = transport
    return dictonary.values()