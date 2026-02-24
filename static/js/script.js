// Função chamada ao enviar o formulário
function irParaPagina(event) {
    event.preventDefault(); // Evita recarregar a página
    alert("Login realizado com sucesso!"); // Exemplo de ação
    // Aqui você pode colocar validação ou redirecionamento
    // window.location.href = "dashboard.html";
}

// Função chamada quando o mouse entra no botão
function entrou(retangulo) {
    retangulo.style.background = "#663da0b2"; // Roxo mais claro
}

// Função chamada quando o mouse sai do botão
function sair(retangulo) {
    retangulo.style.background = "#673DA0"; // Volta ao roxo original
}
