from flask import Flask , jsonify, request
from src.models import Task


  # Import Relativo Correto

  app = Flask (_ name _)

tasks = []

@app.route("/")
def home():
 return jsonify ({"sataus":"API funcioando"}) 
 
@app.route("/task", methods=["POST"])
def create_task():
  task = Task (
    title=data["title"],
    description=data.get("description",""),
    priority =data.get("priority"," Média")     

  )               
   task.append (task)
  return jsonify(task.to_dict()) , 201
