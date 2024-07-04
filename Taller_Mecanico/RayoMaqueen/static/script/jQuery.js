$(function() {
  
    $("#segundo").mouseenter(function(){
        $(".tercero").fadeOut();
    });

    $("#segundo").mouseleave(function(){
        $(".tercero").fadeIn();
    });

});