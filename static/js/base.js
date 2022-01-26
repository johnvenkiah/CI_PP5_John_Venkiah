
/* 
* base.js - main Javascript file for project, controlling
* most features that are active throughout the site.
*/

/*jshint esversion: 6 */
/*globals $:false */

// Show toasts
$(document).ready(function() {
    $('.toast').toast('show');
    
    // Fix error where toast is invisible but
    // blocking the elements behind it 
    $('.toast').on('show.bs.toast', function() {
        $(this).removeClass('d-none');
    });
    $('.toast').on('hidden.bs.toast', function() {
        $(this).addClass("d-none");
    });
    
    // Change background color of navbar and menu if toggler
    // or Products menu is clicked on
    $('.navbar-toggler, #products-link').click(function() {
        $(".bg-nav").css({
            'background-color': '#04142f80'
        }).toggleClass('blur-filter');
        $('.navbar-nav').toggleClass('d-md-none');
    });
    
    // Make products menu visible if  item is clicked on
    $('#account-menu').click(function() {
        $('.navbar-nav').toggleClass('d-md-none');
    });
    
    $(window).resize(function() {
        $('.navbar-nav').addClass('d-md-none');
        $('.navbar-collapse').removeClass('show');
    });
    
    $(document).click(function (event) {
        var clickover = $(event.target);
        var _opened = $('.navbar-collapse').hasClass('show');
        if (_opened === true && !clickover.hasClass('navbar-toggler')) {
            $('.navbar-toggler').click();
            $('.navbar-nav').addClass('d-md-none');
        }
    });
    
    // Hide Header on on scroll down
    let didScroll;
    let lastScrollTop = 0;
    let delta = 30;
    let navbarHeight = $('.navbar').outerHeight();
    
    $(window).scroll(function(event){
        didScroll = true;
    });
    
    setInterval(function() {
        if (didScroll) {
            hasScrolled();
            didScroll = false;
        }
    }, 250);
    
    function hasScrolled() {
        var st = $(this).scrollTop();
        
        // Do nothing if scroll is less than delta
        if(Math.abs(lastScrollTop - st) <= delta)
            return;
        
        // If they scrolled passed navbar, hide relevant classes.
        if (st > lastScrollTop && st > navbarHeight) {
            // Scroll Down
            $('.hide-items').addClass('hide').removeClass('hide-items');
            $('.hide-2').addClass('hide-items-2').removeClass('hide-2');
            $('.btt-button').fadeIn();
        
            // If nav menu is not showing, change the navbar to transparent
            if (!$('#products-nav').hasClass('show')) {
                $('.bg-nav').css({'background-color': 'transparent'});
                $('.grand-total, .nav-link.btn-orange').css({'opacity': '0'});
            }
        } else {
            // Scroll Up
            if(st + $(window).height() < $(document).height()) {
                $('.hide-items-2').addClass('hide-2').removeClass('hide-items-2');
                $('.hide').addClass('hide-items').removeClass('hide');
                $('.bg-nav').css({'background-color': '#04142f80'});
                $('.grand-total, .nav-link.btn-orange').css({'opacity': '1'});
                $('.btt-button').fadeOut();
            }
        }
        
        lastScrollTop = st;
    }
});