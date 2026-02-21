// =============================
// Gerar Cards Automaticamente
// =============================

function criarCard(imagem, nome) {
    const card = document.createElement("div");
    card.classList.add("game-card");

    card.innerHTML = `
        <img src="${imagem}">
        <div class="game-name">${nome}</div>
    `;

    return card;
}

// Exercícios de cima
const cima = document.getElementById("cima");

for (let i = 1; i <= 15; i++) {
    cima.appendChild(
        criarCard("../assets/imagens-utilizadas/yoga.jpg", "Exercício " + i)
    );
}

// Exercícios de baixo
const baixo = document.getElementById("baixo");

for (let i = 16; i <= 30; i++) {
    baixo.appendChild(
        criarCard("../assets/imagens-utilizadas/respirando.png", "Exercício " + i)
    );
}

// =============================
// Função do Carrossel
// =============================

function scrollCarousel(id, direction) {
    const carousel = document.getElementById(id);

    carousel.scrollBy({
        left: 300 * direction,
        behavior: "smooth"
    });
}