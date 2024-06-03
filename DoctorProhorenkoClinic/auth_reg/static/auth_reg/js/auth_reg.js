const showHide = document.querySelector('.show-hide-btn')
const showHideImg = document.querySelector('.show-hide-img')

showHide.addEventListener('click', () => {
    let input = document.querySelector('.form-input.password')
    let showHideImgDiv = document.querySelector('.show-hide-img-div')
    let hideImgPath = "/static/auth_reg/img/hide.png"
    let showImgPath = "/static/auth_reg/img/show.png"

    if (input.type == 'password') {
        input.type = 'text'
        showHideImgDiv.innerHTML = `
        <img src="${hideImgPath}" alt='show_hide' class='show-hide-img'>
        `
    }
    else {
        input.type = 'password'
        showHideImgDiv.innerHTML = `
        <img src="${showImgPath}" alt='show_hide' class='show-hide-img'>
        `
    }
})