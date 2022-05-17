from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
## Importing request module
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///MojaGlobal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80),nullable=False)
    desc=db.Column(db.String(120),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

   ##Excutes when the objects printing
    def __repr__(self):
        return  f"{self.title}'-'{self.desc}"

@app.route('/',methods=['GET','POST'])
def overview():
   if request.method=='POST':
        title=request.form.get('title')
        desc=request.form.get('desc')
        ob=Todo(title=title,desc=desc)
        db.session.add(ob)
        db.session.commit()
       
        alltodo=Todo.query.all()
        return render_template('index.html',todo=alltodo)
     
  
    
   return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True,port=8080)