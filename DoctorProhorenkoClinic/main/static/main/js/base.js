const sLink = document.querySelector('#service-link')
const sMenu = document.querySelector('.services-menu')

const sLinkFooter = document.querySelector('#service-link-footer')
const sMenuFooter = document.querySelector('.services-menu-footer')

sLink.addEventListener('click', () => {
    const linkObj = sLink.getBoundingClientRect()
    
    sMenu.classList.toggle('show-s-menu')
    sMenu.style.top = linkObj.bottom + 'px'
    sMenu.style.left = linkObj.left + 'px'
});

sLinkFooter.addEventListener('click', () => {
    const linkObjFooter = sLinkFooter.getBoundingClientRect()
    
    sMenuFooter.classList.toggle('show-s-menu-footer')
    sMenuFooter.style.top = (linkObjFooter.bottom + window.scrollY) + 'px';
    sMenuFooter.style.left = (linkObjFooter.left + window.scrollX) + 'px';
});

document.addEventListener('click', (event) => {
    if (!sLink.contains(event.target) && !sMenu.contains(event.target)) {
        sMenu.classList.remove('show-s-menu')
    }
})

document.addEventListener('click', (event) => {
    if (!sLinkFooter.contains(event.target) && !sMenuFooter.contains(event.target)) {
        sMenuFooter.classList.remove('show-s-menu-footer')
    }
})
