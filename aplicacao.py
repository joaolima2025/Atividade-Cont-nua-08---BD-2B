from flask import Flask, render_template
app  = Flask(__name__)

@app.route('/index/<user>')


def index(user):
    return render_template("index.html", user=User)

def cursos('/cursos'):
    return render_template("cursos.html")

def Administracao("/Administracao"):
    return render_template("Administracao.html")

def Cienciasdacomptacao('/Ciências da Computação'):
    return render_template("Ciências da Computação.html") 

def diciplina('/diciplina'):
        return render_template("diciplina.html")

def Engenharia da Computação('/Engenharia da Computação'):
    return render_template("Engenharia da Computação.html")   

def noticias('/noticias'):

    return render_template("noticias.html")  

def Sistemas de informacao('/Sistemas de informacao'):
    return render_template("Sistemas de informacao.html")  

app.run()