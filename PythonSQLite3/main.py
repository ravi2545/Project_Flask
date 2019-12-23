from flask import Flask, request, render_template
from allfunctions import ShowDict
app = Flask(__name__)



@app.route('/')
def hello_world():
   return render_template('upload.html')



@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':
            name=request.form['name']
            k=ShowDict()
            # r=k.ins()
            r=k.dis(name)
            if len(r)==0:
                return "Word is not found"
            else:
                return str(r)



if __name__ == '__main__':
   app.run(debug=True)