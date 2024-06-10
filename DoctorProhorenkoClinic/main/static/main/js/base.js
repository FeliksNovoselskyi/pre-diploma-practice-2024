const sLink = document.querySelector('#service-link')

sLink.addEventListener('click', () => {
    const sMenu = document.querySelector('.services-menu')

    if (sMenu.classList.contains('show-s-menu')){
        sMenu.classList.remove('show-s-menu')
    } else {
        sMenu.classList.add('show-s-menu')
    }
})