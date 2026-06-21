// enviar mensagem
function enviarMensagem(event) {
  event.preventDefault();

  const input = document.getElementById("mensagem");
  const texto = input.value.trim();

  if (!texto) return;

  adicionarMensagem("user", texto);
  input.value = "";

  responderBot(texto);
}


// resposta da IA
async function responderBot(textoUsuario){

  const chat = document.getElementById("chatArea");

  const msg = document.createElement("div");
  msg.className = "msg bot";

  const avatar = document.createElement("span");
  avatar.className = "avatar";
  avatar.textContent = "🤖";

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = "Digitando...";

  msg.appendChild(avatar);
  msg.appendChild(bubble);
  chat.appendChild(msg);

  chat.scrollTop = chat.scrollHeight;

  try {

    const resposta = await fetch("/chat/", {   // 🔥 AQUI CORRIGIDO
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: textoUsuario })
    });

    const dados = await resposta.json();

    bubble.textContent = "";
    escreverAnimado(bubble, dados.reply || "Erro: sem resposta");

  } catch (erro) {

    bubble.textContent = "Erro ao conectar com o servidor.";
    console.error(erro);

  }

}


// adiciona mensagem do usuário
function adicionarMensagem(tipo, texto) {

  const chat = document.getElementById("chatArea");

  const msg = document.createElement("div");
  msg.className = `msg ${tipo}`;

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = texto;

  msg.appendChild(bubble);
  chat.appendChild(msg);

  chat.scrollTop = chat.scrollHeight;
}


// efeito máquina de escrever
function escreverAnimado(elemento, texto, velocidade = 20) {

  let i = 0;
  elemento.textContent = "";

  function digitar() {
    if (i < texto.length) {
      elemento.textContent += texto.charAt(i);
      i++;
      setTimeout(digitar, velocidade);
    }
  }

  digitar();
}