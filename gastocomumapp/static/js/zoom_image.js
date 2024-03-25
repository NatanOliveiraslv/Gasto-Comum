// Obtém a imagem clicável
var imagem = document.getElementById("image-voucher");

// Obtém a imagem ampliada
var overlay = document.getElementById("overlay");
var imagemAmpliada = document.getElementById("enlarged-Image");

// Adiciona um evento de clique à imagem
imagem.onclick = function() {
    // Exibe a imagem ampliada
    overlay.style.display = "block";
}

// Adiciona um evento de clique à imagem ampliada (para fechar)
overlay.onclick = function() {
    // Oculta a imagem ampliada quando clicada fora da imagem
    overlay.style.display = "none";
}
