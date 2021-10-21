from flask import Flask

app = Flask(__name__)


@app.route('/')
def domov():
	return"raz tu mozno bude aj htmlko";

#funkcia ktora vrati aktualny cas na http://localhost:5000/cas   
@app.route('/cas')
def funkcia1(): 
	from cas import cas   
	funkcia1 = cas
	return funkcia1()

#funkcia ktora vrati info o pocte infikovanych json formate na http://127.0.0.1:5000/korona
@app.route('/korona')
def funkcia2():
	from korona import korona
	funkcia2 = korona
	return funkcia2()

#flask sa automaticky reloadne ak zisti zmenu v kode
if __name__ == "__main__":
    app.run(debug=True)
    app.run(use_reloader=True)


