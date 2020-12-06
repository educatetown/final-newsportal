/* team section */
$(function () {
    $("#team-members").owlCarousel({
        items: 3,
        autoplay: true,
        smartSpeed: 700,
        loop: true,
        autoplayHoverPause: true,
        nav: true,
        dots: true,
        navText: ['<i class="fa fa-angle-left fa-2x"></i>', '<i class="fa fa-angle-right fa-2x"></i>'],
        responsive: {
            //breakpoint for 0 up
            0:{
                items:1
            },
            // breakpoint from 480 up
            480:{
                items:3
            }
        }
    });
});

/* Navigation*/

/* Show and Hide white Navigation */
$(function(){
    //show /hide nav on page load
    showHideNav();
    $(window).scroll(function(){
        //show/hide nav on windows call
        showHideNav();
    });
    function showHideNav(){
        if($(window).scrollTop()>50){
            //Show white nav
            $("nav").addClass("white-nav-top");
            //show dark logo
            $(".navbar-brand img").attr("src","img/logo/logo-dark.png");

            //show back to top buttton
            $("#back-to-top").fadeIn();

        }else{
            //hide white nav
             $("nav").removeClass("white-nav-top");
            //show logo
             $(".navbar-brand img").attr("src","img/logo/logo.png");
            //shoHidew back to top buttton
            $("#back-to-top").fadeOut();
        }
    }
});



/*=========================================================
            Animation
===========================================================*/
//animate on scroll
$(function(){
    new wow().init();
});

$(window).on('load',function(){
    $("#home-heading-1").addClass("animated fadeInDown");
    $("#home-heading-2").addClass("animated fadeInLeft");
    $("#home-text").addClass("animated zoomIn");
    $("#home-btn").addClass("animated zoomIn");
    $("#arrow-down i").addClass("animated fadeInDown infinite");
});






