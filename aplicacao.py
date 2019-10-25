from flask import Flask, render_template
app  = Flask(__name__)

@app.route('/')


def index('/index'):
    return render_templates("index.html")

def cursos('/cursos'):
    return render_templates("cursos.html")

def Administracao('/Administracao'):
    return render_templates("Administracao.html")

def Cienciasdacomptacao('/Ciências da Computação'):
    return render_templates("Ciências da Computação.html") 

def diciplina('/diciplina'):
        return render_templates("diciplina.html")

def Engenharia da Computação('/Engenharia da Computação'):
    return render_templates("Engenharia da Computação.html")   

def noticias('/noticias'):

    return render_templates("noticias.html")  

def Sistemas de informacao('/Sistemas de informacao'):
    return render_templates("Sistemas de informacao.html")  

app.run()