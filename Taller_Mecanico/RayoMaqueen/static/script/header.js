$(document).ready(function () {
    $(function () {
        $("#contenidoHeader").load("{% static 'RayoMaqueen/header.html' %}");
    });
});

$(document).ready(function () {
    $(function () {
        $("#contenidoFooter").load("{% static 'RayoMaqueen/footer.html' %}");
    });
});
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 0) {
            $('header').addClass('header2');
        } else {
            $('header').removeClass('header2');
        }
    });
});