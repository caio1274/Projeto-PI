
// Função chamada quando o usuário envia uma mensagem no formulário
function enviarMensagem(event) {
  event.preventDefault(); // Impede que o formulário recarregue a página

  const input = document.getElementById("mensagem"); // Pega o campo de texto
  const texto = input.value.trim(); // Remove espaços extras no início/fim
  if (!texto) return; // Se estiver vazio, não faz nada

  adicionarMensagem("user", texto); // Adiciona a mensagem do usuário no chat
  input.value = ""; // Limpa o campo de texto

  // Aguarda 800ms e chama a resposta do bot
  setTimeout(() => {
    responderBot();
  }, 800);
}

// Função que adiciona uma nova mensagem ao chat
function adicionarMensagem(tipo, texto) {
  const chat = document.getElementById("chatArea"); // Área do chat

  const msg = document.createElement("div"); // Cria um novo bloco de mensagem
  msg.className = `msg ${tipo}`; // Define a classe (msg user ou msg bot)

  // Se for mensagem do bot, adiciona o avatar 🤖
  if (tipo === "bot") {
    const avatar = document.createElement("span");
    avatar.className = "avatar"; // Classe para estilizar o avatar
    avatar.textContent = "\u{1F916}"; // Emoji do robô
    msg.appendChild(avatar); // Coloca o avatar dentro da mensagem
  }

  // Cria a bolha de texto
  const bubble = document.createElement("div");
  bubble.className = "bubble"; // Classe para estilizar a bolha
  bubble.textContent = texto; // Texto da mensagem

  // Junta tudo: avatar (se houver) + bolha
  msg.appendChild(bubble);
  chat.appendChild(msg); // Adiciona a mensagem na área do chat

  // Faz o scroll automático para mostrar a última mensagem
  chat.scrollTop = chat.scrollHeight;
}

// Função que gera uma resposta automática do bot
function responderBot() {
  // Lista de respostas possíveis
  const respostas = [
    "Entendo \u{1F49C} Quer me contar mais?",
    "Estou aqui com você.",
    "Respire fundo… você não está sozinho.",
    "Isso parece importante. Vamos conversar."
  ];

  // Escolhe uma resposta aleatória da lista
  const resposta = respostas[Math.floor(Math.random() * respostas.length)];

  // Adiciona a resposta do bot no chat
  adicionarMensagem("bot", resposta);
}
