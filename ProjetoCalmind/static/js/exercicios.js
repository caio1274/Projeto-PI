// =============================
// Função para criar os cards
// =============================

function criarCard(imagem, nome) {
    const card = document.createElement("div");
    card.classList.add("game-card");

    card.innerHTML = `
        <img src="${imagem}" alt="${nome}">
        <div class="game-name">${nome}</div>
    `;

    return card;
}


// =============================
// Carrossel - Parte de Cima
// =============================

const cima = document.getElementById("cima");

if (cima) {
    for (let i = 1; i <= 15; i++) {
        cima.appendChild(
            criarCard(
                "/static/assets/imagens-utilizadas/yoga.jpg",
                "Exercício " + i
            )
        );
    }
}


// =============================
// Carrossel - Parte de Baixo
// =============================

const baixo = document.getElementById("baixo");

if (baixo) {
    for (let i = 16; i <= 30; i++) {
        baixo.appendChild(
            criarCard(
                "/static/assets/imagens-utilizadas/respirando.png",
                "Exercício " + i
            )
        );
    }
}


// =============================
// Função de Scroll do Carrossel
// =============================

function scrollCarousel(id, direction) {
    const carousel = document.getElementById(id);

    if (carousel) {
        carousel.scrollBy({
            left: 300 * direction,
            behavior: "smooth"
        });
    }
}