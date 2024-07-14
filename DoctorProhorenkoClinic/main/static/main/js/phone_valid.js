document.addEventListener("DOMContentLoaded", function() {
    const validOperators = ["50", "63", "66", "67", "68", "70", "73", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"];

    $(".phone").inputmask({
        mask: "+380(99)999-99-99",
        placeholder: "_",
        showMaskOnHover: false,
        showMaskOnFocus: true,
        onincomplete: function() {
            $(this).val("");
        },
        oncomplete: function() {
            const operatorCode = $(this).val().slice(5, 7);
            
            if (!validOperators.includes(operatorCode)) {
                $(this).val("");
            }
        }
    });

    $("#enroll-form").on("submit", function(event) {
        const usernameValue = $("input[name='username']").val();
        const surnameValue = $("input[name='surname']").val();
        const emailValue = $("input[name='email']").val();
        const phoneValue = $("input[name='phone']").val();
        
        if (phoneValue.length < 17 || usernameValue.length < 1 || surnameValue.length < 1 || emailValue.length < 1) {
            event.preventDefault();
        } else {
            $(".suc-enroll-modal").modal("show");
        }
    });
});