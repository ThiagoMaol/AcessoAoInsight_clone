function abrir(url){
	window.open(url);
}

// Interceptador global para redirecionar links de mídias ausentes para o site original
document.addEventListener("click", function(event) {
    var target = event.target;
    
    // Caminha pela árvore do DOM para achar a tag <a> mais próxima do clique
    while (target && target.tagName !== 'A') {
        target = target.parentNode;
    }
    
    if (target && target.href) {
        var hrefAttr = target.getAttribute('href') || '';
        var fullUrl = target.href || '';
        
        // Critério para identificar links de mídias ausentes (.mp3, .m4b, .epub, .azw3, .pdf, .zip)
        // ou caminhos que apontavam para as pastas de mídia (/audiobooks/, /ebooks/, /podcasts/, /livros/)
        var isMedia = /audiobooks\/|ebooks\/|podcasts\/|livros\/|\.(mp3|m4b|epub|azw3|pdf|zip)$/i.test(hrefAttr) ||
                      /audiobooks\/|ebooks\/|podcasts\/|livros\/|\.(mp3|m4b|epub|azw3|pdf|zip)$/i.test(fullUrl);
        
        // Verifica se o link é local ou aponta para o domínio original
        var isTargetDomain = fullUrl.indexOf("acessoaoinsight.net") !== -1 || 
                             (!/^(?:[a-z]+:)?\/\//i.test(hrefAttr)); // links relativos
        
        if (isMedia && isTargetDomain) {
            // Cancela a navegação padrão (que daria erro 404 local ou tiraria o usuário do site)
            event.preventDefault();
            
            // Remove caminhos relativos iniciais (como ../../ ou ./)
            var cleanPath = hrefAttr.replace(/^(\.\.\/|\.\/)+/, '');
            
            // Se o link for relativo, reconstrói apontando para o site original online
            var finalUrl = fullUrl;
            if (!/^(?:[a-z]+:)?\/\//i.test(hrefAttr)) {
                finalUrl = "http://www.acessoaoinsight.net/" + cleanPath;
            }
            
            // Abre o download ou áudio em uma nova aba para que o usuário não saia do site clone
            window.open(finalUrl, '_blank');
        }
    }
});