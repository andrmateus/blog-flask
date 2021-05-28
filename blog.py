from typing import Match
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
import bibliotecas as b
import banco

blog = b.Flask(__name__)
blog.static_folder = 'static'


@blog.route('/', methods=['GET','POST'])

def principal():
    if b.request.method == 'GET':
        return b.render_template('index.html', regs=banco.list())

    if b.request.method == 'POST' and 'put' == b.request.form['operation']:
        descricao = b.request.form['descricao']
        titulo = b.request.form['titulo']
        if descricao and titulo:
            banco.insert(descricao, titulo)
        return render_template('index.html', regs=banco.list())
        

    if b.request.method == 'POST' and 'delete' == b.request.form['operation']:
        idtopico = b.request.form['idtopico']
        banco.delete(idtopico)
        return render_template('index.html', regs=banco.list())

    if b.request.method == 'POST' and 'create' == b.request.form['operation']:
        return b.render_template("criarTopico.html")

    if b.request.method == 'POST' and 'edit' == b.request.form['operation']:
        idtopico = b.request.form['idtopico']
        return b.render_template("alteraTopico.html", regs=banco.selectCamp(idtopico))

    if b.request.method == 'POST' and 'editing' == b.request.form['operation']:
        idEditada = b.request.form['idEditada']      
        descricaoEditada = b.request.form['descricaoEditada']
        tituloEditado = b.request.form['tituloEditado']
        descricaoAntiga = b.request.form['descricaoAntiga']
        tituloAntigo = b.request.form['tituloAntigo']
        if (descricaoAntiga != descricaoEditada) or (tituloAntigo != tituloEditado):
            banco.edita(tituloEditado,descricaoEditada,idEditada)
            return render_template('index.html', regs=banco.list())

if __name__ == '__main__':
    blog.run(debug="yes")