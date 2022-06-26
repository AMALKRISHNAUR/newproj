from flask import Blueprint,render_template,request
from flask_login import login_required,current_user
from arduino_rpi_taskmaster import ServerClient
s = ServerClient.Client.Client(9999)
views = Blueprint('views',__name__)
ip = "10.0.8.188"
@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        data = request.form.get('co')
        if data == 'lighton':
            s.send_data(ip,"on\r")
            
        if data == 'lightoff':
            s.send_data(ip,"off\r")
        if data =='dooron':
            s.send_data(ip,"don\r")
        if data == "doorclose":
            s.send_data(ip,"doff\r")
        if data == "fanon":
            s.send_data(ip,"mon\r")
        if data == 'fanoff':
            s.send_data(ip,"moff\r")

    return render_template('home.html',user=current_user)
