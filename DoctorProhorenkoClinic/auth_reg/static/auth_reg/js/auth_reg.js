const showHide = document.querySelector('.show-hide-btn')
let input = document.querySelector('.form-input.password')

showHide.addEventListener('click', () => {
    if (input.type == 'password') {
        input.type = 'text'
    }
    else {
        input.type = 'password'
    }
})