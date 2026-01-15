// ==============================
// Carrega favicon automaticamente
// ==============================
const favicon = document.createElement('link');
favicon.rel = 'shortcut icon';
favicon.href = 'Imagens-logo/arqiuvos fivecons/favicon.ico';
favicon.type = 'image/x-icon';
document.head.appendChild(favicon);

// ==============================
// Carrega CSS automaticamente
// ==============================
const css = document.createElement('link');
css.rel = 'stylesheet';
css.href = 'css/style.css';
document.head.appendChild(css);
