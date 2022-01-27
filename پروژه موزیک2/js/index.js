jQuery(function($) {
    $(".panel-u ul li a")
        .click(function(e) {
            var link = $(this);

            var item = link.parent("li");

            if (item.hasClass("active")) {
                item.removeClass("active").children("a").removeClass("active");
            } else {
                item.addClass("active").children("a").addClass("active");
            }

            if (item.children("ul").length > 0) {
                var href = link.attr("href");
                link.attr("href", "#");
                setTimeout(function() {
                    link.attr("href", href);
                }, 300);
                e.preventDefault();
            }
        })
        .each(function() {
            var link = $(this);
            if (link.get(0).href === location.href) {
                link.addClass("active").parents("li").addClass("active");
                return false;
            }
        });
});

$(window).load(function() {
    var lang = localStorage.lang || 'EN';
    $('a[lang="' + lang + '"]').addClass('active');
});

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


$(function() {
    var playerTrack = $("#player-track"),
        bgArtwork = $("#bg-artwork"),
        bgArtworkUrl,
        albumName = $("#album-name"),
        titleplay = $("#title-play"),
        trackName = $("#track-name"),
        albumArt = $("#album-art"),
        sArea = $("#s-area"),
        seekBar = $("#seek-bar"),
        trackTime = $("#track-time"),
        insTime = $("#ins-time"),
        sHover = $("#s-hover"),
        playPauseButton = $("#play-pause-button"),
        playPausespan = $("#play-pause-span"),
        i = playPauseButton.find("i"),
        tProgress = $("#current-time"),
        tTime = $("#track-length"),
        seekT,
        seekLoc,
        seekBarPos,
        cM,
        ctMinutes,
        ctSeconds,
        curMinutes,
        curSeconds,
        durMinutes,
        durSeconds,
        playProgress,
        bTime,
        nTime = 0,
        buffInterval = null,
        tFlag = false,
        albums = [
            "Dawn",
            "Me & You",
            "Electro Boy",
            "Home",
            "Proxy (Original Mix)"
        ],
        trackNames = [
            "Skylike - Dawn",
            "Alex Skrindo - Me & You",
            "Kaaze - Electro Boy",
            "Jordan Schor - Home",
            "Martin Garrix - Proxy"
        ],
        albumArtworks = ["_1", "_2", "_3", "_4", "_5"],
        trackUrl = [
            "https://raw.githubusercontent.com/himalayasingh/music-player-1/master/music/2.mp3",
            "https://raw.githubusercontent.com/himalayasingh/music-player-1/master/music/1.mp3",
            "https://raw.githubusercontent.com/himalayasingh/music-player-1/master/music/3.mp3",
            "https://raw.githubusercontent.com/himalayasingh/music-player-1/master/music/4.mp3",
            "https://raw.githubusercontent.com/himalayasingh/music-player-1/master/music/5.mp3"
        ],
        playPreviousTrackButton = $("#play-previous"),
        playNextTrackButton = $("#play-next"),
        currIndex = -1;

    function playPause() {
        setTimeout(function() {
            if (audio.paused) {
                playerTrack.addClass("active");
                albumArt.addClass("active");
                checkBuffering();
                i.attr("class", "fas fa-pause");
                audio.play();
            } else {
                playerTrack.removeClass("active");
                albumArt.removeClass("active");
                clearInterval(buffInterval);
                albumArt.removeClass("buffering");
                i.attr("class", "fas fa-play");
                audio.pause();
            }
        }, 300);
    }

    function playPausetitle() {
        setTimeout(function() {
            if (audio.paused) {
                playerTrack.addClass("active");
                albumArt.addClass("active");
                checkBuffering();
                i.attr("class", "fas fa-pause");
                audio.play();
            } else {
                playerTrack.removeClass("active");
                albumArt.removeClass("active");
                clearInterval(buffInterval);
                albumArt.removeClass("buffering");
                i.attr("class", "fas fa-play");
                audio.pause();
            }
        }, 300);
    }

    function playPauseSpan() {
        setTimeout(function() {
            if (audio.paused) {
                playerTrack.addClass("active");
                albumArt.addClass("active");
                checkBuffering();
                i.attr("class", "fas fa-pause");
                audio.play();
            } else {
                playerTrack.removeClass("active");
                albumArt.removeClass("active");
                clearInterval(buffInterval);
                albumArt.removeClass("buffering");
                i.attr("class", "fas fa-play");
                audio.pause();
            }
        }, 300);
    }

    function showHover(event) {
        seekBarPos = sArea.offset();
        seekT = event.clientX - seekBarPos.left;
        seekLoc = audio.duration * (seekT / sArea.outerWidth());

        sHover.width(seekT);

        cM = seekLoc / 60;

        ctMinutes = Math.floor(cM);
        ctSeconds = Math.floor(seekLoc - ctMinutes * 60);

        if (ctMinutes < 0 || ctSeconds < 0) return;

        if (ctMinutes < 0 || ctSeconds < 0) return;

        if (ctMinutes < 10) ctMinutes = "0" + ctMinutes;
        if (ctSeconds < 10) ctSeconds = "0" + ctSeconds;

        if (isNaN(ctMinutes) || isNaN(ctSeconds)) insTime.text("--:--");
        else insTime.text(ctMinutes + ":" + ctSeconds);

        insTime.css({ left: seekT, "margin-left": "-21px" }).fadeIn(0);
    }

    function hideHover() {
        sHover.width(0);
        insTime.text("00:00").css({ left: "0px", "margin-left": "0px" }).fadeOut(0);
    }

    function playFromClickedPos() {
        audio.currentTime = seekLoc;
        seekBar.width(seekT);
        hideHover();
    }

    function updateCurrTime() {
        nTime = new Date();
        nTime = nTime.getTime();

        if (!tFlag) {
            tFlag = true;
            trackTime.addClass("active");
        }

        curMinutes = Math.floor(audio.currentTime / 60);
        curSeconds = Math.floor(audio.currentTime - curMinutes * 60);

        durMinutes = Math.floor(audio.duration / 60);
        durSeconds = Math.floor(audio.duration - durMinutes * 60);

        playProgress = (audio.currentTime / audio.duration) * 100;

        if (curMinutes < 10) curMinutes = "0" + curMinutes;
        if (curSeconds < 10) curSeconds = "0" + curSeconds;

        if (durMinutes < 10) durMinutes = "0" + durMinutes;
        if (durSeconds < 10) durSeconds = "0" + durSeconds;

        if (isNaN(curMinutes) || isNaN(curSeconds)) tProgress.text("00:00");
        else tProgress.text(curMinutes + ":" + curSeconds);

        if (isNaN(durMinutes) || isNaN(durSeconds)) tTime.text("00:00");
        else tTime.text(durMinutes + ":" + durSeconds);

        if (
            isNaN(curMinutes) ||
            isNaN(curSeconds) ||
            isNaN(durMinutes) ||
            isNaN(durSeconds)
        )
            trackTime.removeClass("active");
        else trackTime.addClass("active");

        seekBar.width(playProgress + "%");

        if (playProgress == 100) {
            i.attr("class", "fa fa-play");
            seekBar.width(0);
            tProgress.text("00:00");
            albumArt.removeClass("buffering").removeClass("active");
            clearInterval(buffInterval);
        }
    }

    function checkBuffering() {
        clearInterval(buffInterval);
        buffInterval = setInterval(function() {
            if (nTime == 0 || bTime - nTime > 1000) albumArt.addClass("buffering");
            else albumArt.removeClass("buffering");

            bTime = new Date();
            bTime = bTime.getTime();
        }, 100);
    }

    function selectTrack(flag) {
        if (flag == 0 || flag == 1) ++currIndex;
        else --currIndex;

        if (currIndex > -1 && currIndex < albumArtworks.length) {
            if (flag == 0) i.attr("class", "fa fa-play");
            else {
                albumArt.removeClass("buffering");
                i.attr("class", "fa fa-pause");
            }

            seekBar.width(0);
            trackTime.removeClass("active");
            tProgress.text("00:00");
            tTime.text("00:00");

            currAlbum = albums[currIndex];
            currTrackName = trackNames[currIndex];
            currArtwork = albumArtworks[currIndex];

            audio.src = trackUrl[currIndex];

            nTime = 0;
            bTime = new Date();
            bTime = bTime.getTime();

            if (flag != 0) {
                audio.play();
                playerTrack.addClass("active");
                albumArt.addClass("active");

                clearInterval(buffInterval);
                checkBuffering();
            }

            albumName.text(currAlbum);
            trackName.text(currTrackName);
            albumArt.find("img.active").removeClass("active");
            $("#" + currArtwork).addClass("active");

            bgArtworkUrl = $("#" + currArtwork).attr("src");

            bgArtwork.css({ "background-image": "url(" + bgArtworkUrl + ")" });
        } else {
            if (flag == 0 || flag == 1) --currIndex;
            else ++currIndex;
        }
    }

    function initPlayer() {
        audio = new Audio();

        selectTrack(0);

        audio.loop = false;

        playPauseButton.on("click", playPause);
        titleplay.on("click", playPausetitle);
        playPausespan.on("click", playPauseSpan);
        sArea.mousemove(function(event) {
            showHover(event);
        });

        sArea.mouseout(hideHover);

        sArea.on("click", playFromClickedPos);

        $(audio).on("timeupdate", updateCurrTime);

        playPreviousTrackButton.on("click", function() {
            selectTrack(-1);
        });
        playNextTrackButton.on("click", function() {
            selectTrack(1);
        });
    }

    initPlayer();
});

$(".panel-u ul li").click(function() {
    $(this).closest('ul').find('li').each(function() {
        $(this).removeClass('active');
    });
    $(this).addClass('active');
    defaultWidth = lineWidth = activeElement.width();
    defaultPosition = linePosition = activeElement.position().left;
    menuLine.css("width", lineWidth);
    menuLine.css("left", linePosition);
});