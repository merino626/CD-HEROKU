import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''<h1>Ola!</h1><br>
    <button onclick='mostra()'>Clique para descobrir o endereço</button>
    <div id='1'></div>
    <style>h1 {
        font-size: 50px;
        margin-left: 600px;
    }
    button {
        margin-left: 600px;
    }
    div {
        background-color: red;
        margin-left:600px;
        font-size:100px;

    }
    </style>
    <script>
    function mostra(){
        var elemento = document.getElementById('1')
        elemento.innerHTML = 'Rua tupi, jardim são silvestre, vulgo quebrada.'
    }
     </script>
    
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
