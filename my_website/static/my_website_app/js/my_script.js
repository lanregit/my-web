$(function(){
    $("#name").hide();
    $("#named").hide();
    // $("#abt1").hide();
    // $("#abt2").hide();
    $(window).load(function(){
        $("#name").slideDown(2000);
        $("#named").slideDown(3000);
    });
    // $(window).scroll(function(){
    //     $("#abt1").fadeIn(3000);
    //     $("#abt2").fadeIn(5000);
    // });
    let canvas = {
        radius: 150,
        speed: 3,
        slower: 0.9,
        timer: 5,
        fontMultiplier: 16
    };

    $(document).ready(function(){
        $("#sphere").tagoSphere(canvas);
    });

})