from flask import render_template

def show():
   
#  with open(os.path.join(BP,'info.yml'), 'r') as f:

#    return jsonify(f.read()) 
  return render_template('info.html')



  
