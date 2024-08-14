window.addEventListener('scroll', function() {
    var mainContent = document.getElementById('main-content');
    var startScreen = document.getElementById('start-screen');
    var scrollPosition = window.scrollY || window.pageYOffset;

    if (scrollPosition > 50) {
        mainContent.style.display = 'block';
    } else {
        mainContent.style.display = 'none';
    }
});
