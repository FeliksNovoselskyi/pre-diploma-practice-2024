document.addEventListener("DOMContentLoaded", function() {
    $(".phone").inputmask({
        mask: "+380(99)999-99-99",
        placeholder: "_",
        showMaskOnHover: false,
        showMaskOnFocus: true
    });
});