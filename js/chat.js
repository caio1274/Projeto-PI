function enviarMensagem(event) {
  event.preventDefault();

  const input = document.getElementById("mensagem");
  const texto = input.value.trim();
  if (!texto) return;

  adicionarMensagem("user", texto);
  input.value = "";

  setTimeout(() => {
    responderBot();
  }, 800);
}

function adicionarMensagem(tipo, texto) {
  const chat = document.getElementById("chatArea");

  const msg = document.createElement("div");
  msg.className = `msg ${tipo}`;

  if (tipo === "bot") {
    const avatar = document.createElement("span");
    avatar.className = "avatar";
    avatar.textContent = "🤖";
    msg.appendChild(avatar);
  }

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = texto;

  msg.appendChild(bubble);
  chat.appendChild(msg);

  chat.scrollTop = chat.scrollHeight;
}

function responderBot() {
  const respostas = [
    "Entendo 💜 Quer me contar mais?",
    "Estou aqui com você.",
    "Respire fundo… você não está sozinho.",
    "Isso parece importante. Vamos conversar."
  ];

  const resposta = respostas[Math.floor(Math.random() * respostas.length)];
  adicionarMensagem("bot", resposta);
}
