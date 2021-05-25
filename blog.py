from flask.templating import render_template
import bibliotecas as b
import banco

blog = b.Flask(__name__)
blog.static_folder = 'static'

@blog.route('/', methods=['GET','POST'])

def index():
    if b.request.method == 'POST':
        descricao = b.request.form['descricao']
        
        banco.insert(descricao)

    return b.render_template('index.html', regs=banco.list())

@blog.route('/novotopico', methods=['GET', 'POST'])

def novotopico():
    return b.render_template("criarTopico.html")

@blog.route('/apagatopico', methods=['GET', 'POST'])

def apagar():
    
    if b.request.method == 'POST':
        idtopico = b.request.form['idtopico']
        print(idtopico)
        banco.delete(idtopico)
        print('apagado')
    return b.render_template("apaga.html")


if __name__ == '__main__':
    blog.run(debug="yes")
