
from flaskr import bibliotecas as b # chama o arquivo que contem as bibliotecas utilizadas
from flaskr import banco # chama o arquivo que contem as funções de banco


blog = b.Flask(__name__)
blog.static_folder = 'static'

# pagina principal
@blog.route('/', methods=['GET','POST'])

def principal():
    # metodo de acesso get retorna a pagina natural
    if b.request.method == 'GET':
        return b.render_template('index.html', regs=banco.list())

    # carrega a listagem do banco de dados
    if b.request.method == 'POST':
        if 'put' == b.request.form['operation']:
            descricao = b.request.form['descricao']
            titulo = b.request.form['titulo']
            # funcao para inserir informações no blog
            if descricao and titulo:
                banco.insert(descricao, titulo)
            return b.render_template('index.html', regs=banco.list())
        
         # funcao para apagar informações do blog
        if 'delete' == b.request.form['operation']:
            idtopico = b.request.form['idtopico']
            banco.delete(idtopico)
            return b.render_template('index.html', regs=banco.list())

        # funcao que busca a pagina para inserir um novo topico
        if 'create' == b.request.form['operation']:
            return b.render_template("criarTopico.html")

        # funcao que busca a pagina para editar os topicos
        if 'edit' == b.request.form['operation']:
            idtopico = b.request.form['idtopico']
            return b.render_template("alteraTopico.html", regs=banco.selectCamp(idtopico))

        # funcao que grava a edicao do topico no banco
        if 'editing' == b.request.form['operation']:
            idEditada = b.request.form['idEditada']      
            descricaoEditada = b.request.form['descricaoEditada']
            tituloEditado = b.request.form['tituloEditado']
            descricaoAntiga = b.request.form['descricaoAntiga']
            tituloAntigo = b.request.form['tituloAntigo']
            if (descricaoAntiga != descricaoEditada) or (tituloAntigo != tituloEditado):
                banco.edita(tituloEditado,descricaoEditada,idEditada)
            return b.render_template('index.html', regs=banco.list())

# tratativa de error pagina nao encontrada
@blog.errorhandler(404)

def pagina_nao_encontrada(e):
    return b.render_template('404.html'), 404


# inicia o programa
if __name__ == '__main__':
    blog.run(debug="yes")