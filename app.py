from flask import Flask, request, jsonify, render_template
import numpy as np
from get_model_copy import saved
from utils import parse_form_data

model = saved()

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def survey():
    if request.method == 'POST':
        data = request.form
        data1 = parse_form_data(data)
        # data_for_model = np.array([[data1["age"], data1["sex"], data1["highest_qualification"], data1["rural"], data1["disability_status"], data1["is_water_filter"], data1["chew"], data1["smoke"], data1["alcohol"], data1["treatment_source"], data1["marital_status"], data1["injury_treatment_type"], data1["illness_type"], data1["symptoms_pertaining_illness"], data1["sought_medical_care"], data1["diagnosed_for"], data1["regular_treatment_source"], data1["iscoveredbyhealthscheme"]]])
        # columns = ["sex", "highest_qualification", "rural", "disability_status", "is_water_filter", "chew", "smoke", "alcohol","treatment_source"]
        columns = ["rural","sex", "treatment_source","marital_status", "highest_qualification", "disability_status", "symptoms_pertaining_illness","sought_medical_care","injury_treatment_type","diagnosed_for","regular_treatment_source", "chew", "smoke", "alcohol","is_water_filter","illness_type","iscoveredbyhealthscheme"]
        data_for_model = np.array([[data1.get(col, 0) for col in columns]])
        pred = model.predict(data_for_model)

        pred_list = pred.tolist()
        # return jsonify(pred_list)
        return render_template("result.html",value=int(pred_list[0]))
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
