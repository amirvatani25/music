$(".alm-carousel").owlCarousel({
    stagePadding: 40,
    margin: 15,
    loop: true,
    rtl: true,
    mouseDrag: true,
    autoplay: true,
    autoplayHoverPause: true,
    autoplaySpeed: 4000,
    autoplayTimeout: 4000,
    dots: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
});


$(".category-carousel").owlCarousel({
    stagePadding: 40,
    margin: 15,
    loop: true,
    rtl: true,
    mouseDrag: true,
    autoplay: true,
    autoplayHoverPause: true,
    autoplaySpeed: 4000,
    autoplayTimeout: 4000,
    dots: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 7
        }
    }
});

$(".dots").click(function() {
    $("body").css("overflow", "hidden");
    $(".drop-menu").toggleClass("add-drop");
    $(".menu-overlay").toggleClass("add-overlay");
    $(".z-span").click(function() {
        $("body").css("overflow", "unset");
        $(".drop-menu").removeClass("add-drop");
        $(".menu-overlay").removeClass("add-overlay");
    });
});


$(".menu-overlay").click(function() {
    $("body").css("overflow", "unset");
    $(".drop-menu").removeClass("add-drop");
    $(".menu-overlay").removeClass("add-overlay");
});
// $(".z-span").click(function() {
//     $('.drop-menu').toggleClass('remove-drop');
// });

$(".search-icon").click(function() {
    $(".search-form").toggleClass("search-open");
    $('.search-icon').toggleClass('menu-op');
});