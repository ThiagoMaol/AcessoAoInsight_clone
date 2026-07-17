function abrir(url){
	window.open(url);
}

// Injeta a faixa de aviso assim que a página é carregada
document.addEventListener("DOMContentLoaded", function() {
    // 1. Criar o elemento da faixa
    var banner = document.createElement("div");
    banner.id = "clone-warning-banner";

    // Mensagem sucinta com links em HTML
    banner.innerHTML = "Este site é um clone do original: " +
                       "<a href='<http://www.acessoaoinsight.net>'>acessoaoinsight.net</a>. " +
                       "Para entender o projeto, acesse o <a href='<https://github.com/ThiagoMaol/AcessoAoInsight_clone>'>repositório</a>.";

    // 2. Estilizar a faixa (cinza quase preto, fixa no topo, z-index alto)
    banner.style.position = "fixed";
    banner.style.top = "0";
    banner.style.left = "0";
    banner.style.width = "100%";
    banner.style.backgroundColor = "#1c1c1c"; // Cinza quase preto
    banner.style.color = "#ffffff";           // Texto em branco
    banner.style.textAlign = "center";
    banner.style.padding = "5px 10px";
    banner.style.fontSize = "10px";
    banner.style.fontFamily = "sans-serif";
    banner.style.zIndex = "99999";            // Garante que fique acima de tudo
    banner.style.boxShadow = "0 2px 10px rgba(0,0,0,0.5)";

    // 3. Estilizar os links dentro da faixa (azul claro para contraste)
    var links = banner.getElementsByTagName("a");
    for (var i = 0; i < links.length; i++) {
        links[i].style.color = "#66b2ff";      // Azul claro contrastante
        links[i].style.textDecoration = "underline";
        links[i].style.fontWeight = "bold";
        links[i].setAttribute("target", "_blank"); // Abre em nova aba
    }

    // 4. Inserir no início do corpo da página (body)
    document.body.insertBefore(banner, document.body.firstChild);

    // 5. Empurrar o conteúdo do site para baixo para não ficar coberto pela faixa
    // O banner tem cerca de 36px de altura, então adicionamos esse espaçamento no topo do body
    document.body.style.paddingTop = "36px";
});