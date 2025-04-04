function enviarComando(acao, valor) {
    fetch('http://localhost:5000/comando', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ acao: acao, valor: valor })
    })
    .then(response => response.text())
    .then(data => console.log(data))
    .catch(error => console.error('Erro:', error));
}
