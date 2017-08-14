from flask import Flask, Response, render_template,request,redirect
import json
from datatable import BaseDataTables
app = Flask(__name__)

@app.route("/")
def index():

    return render_template('index.html')
@app.route('/load',methods=['GET','POST'])
def load():
    table = BaseDataTables(request, columns=['f_id','first_name','last_name','region','office','salary'], table='t_test_datatale')
    result=table.output_result_data()
    if request.method == 'POST':
        data = table.get_request_data(request.form)
        table.update_table_data(data)
        return redirect('load')
    return json.dumps(result)

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
