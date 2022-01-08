(function ($) {
"use strict";

// preloader
function preloader() {
	$('#preloader').delay(0).fadeOut();
};

$(window).on('load', function () {
	preloader();
	aosanimation();
	counter();
	wowanimation();
});


// meanmenu
$('#mobile-menu').meanmenu({
	meanMenuContainer: '.mobile-menu',
	meanScreenWidth: "992"
});


// sticky-menu
$(window).on('scroll', function () {
	var scroll = $(window).scrollTop();
	if (scroll < 245) {
		$("#header-sticky").removeClass("sticky-menu");
	} else {
		$("#header-sticky").addClass("sticky-menu");
	}
});



// mainSlider
function mainSlider() {
	var BasicSlider = $('.slider-active');
	BasicSlider.on('init', function (e, slick) {
		var $firstAnimatingElements = $('.single-slider:first-child').find('[data-animation]');
		doAnimations($firstAnimatingElements);
	});
	BasicSlider.on('beforeChange', function (e, slick, currentSlide, nextSlide) {
		var $animatingElements = $('.single-slider[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
		doAnimations($animatingElements);
	});
	BasicSlider.slick({
		autoplay: false,
		autoplaySpeed: 10000,
		dots: false,
		fade: true,
		arrows: false,
		responsive: [
			{ breakpoint: 767, settings: { dots: false, arrows: false } }
		]
	});

	function doAnimations(elements) {
		var animationEndEvents = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
		elements.each(function () {
			var $this = $(this);
			var $animationDelay = $this.data('delay');
			var $animationType = 'animated ' + $this.data('animation');
			$this.css({
				'animation-delay': $animationDelay,
				'-webkit-animation-delay': $animationDelay
			});
			$this.addClass($animationType).one(animationEndEvents, function () {
				$this.removeClass($animationType);
			});
		});
	}
}
mainSlider();


 // Products Tooltip
$(".site-preview").smartImageTooltip({previewTemplate: "gemas", imageWidth: "500px"});



// testimonial-active
$('.testimonial-active').slick({
  dots: true,
  infinite: true,
  speed: 1000,
  arrows: false,
  slidesToShow: 1,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 575,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
		arrows: false,
		fade: true,
      }
    },
  ]
});


// Pricing
$('.ct-pricing-body').each(function () {
	$(this).find('.item--first').hover(function () {
		$(this).parent().addClass('item--first-active');
	}, function () {
		$(this).parent().removeClass('item--first-active');
	});
	$(this).find('.item--last').hover(function () {
		$(this).parent().addClass('item--last-active');
	}, function () {
		$(this).parent().removeClass('item--last-active');
	});
});
$(".item--nav").on('click', function () {
	$(this).parent().toggleClass('active');
	$(this).parents('.ct-pricing').find('.ct-pricing-monthly').toggleClass('pr-hide');
	$(this).parents('.ct-pricing').find('.ct-pricing-year').toggleClass('pr-active');
});


// price - slider active
$("#slider-range").slider({
  range: true,
  min: 40,
  max: 600,
  values: [60, 570],
  slide: function (event, ui) {
    $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
  }
});
$("#amount").val("$" + $("#slider-range").slider("values", 0) + " - $" + $("#slider-range").slider("values", 1));


/* magnificPopup img view */
$('.popup-image').magnificPopup({
	type: 'image',
	gallery: {
	  enabled: true
	}
});

/* magnificPopup video view */
$('.popup-video').magnificPopup({
	type: 'iframe'
});


// isotop
$('.product-active').imagesLoaded( function() {
	// init Isotope
	var $grid = $('.product-active').isotope({
	  itemSelector: '.grid-item',
	  percentPosition: true,
	  masonry: {
		columnWidth: 1,
	  }
	});
	// filter items on button click
	$('.product-menu').on('click', 'button', function () {
		var filterValue = $(this).attr('data-filter');
		$grid.isotope({ filter: filterValue });
	});
});


//for menu active class
$('.product-menu button').on('click', function(event) {
	$(this).siblings('.active').removeClass('active');
	$(this).addClass('active');
	event.preventDefault();
});


// aos-active
function aosanimation() {
	AOS.init({
		duration: 1000,
		mirror: true
	});
}

// counterUp
function counter() {
	$(".count").counterUp({
		delay: 10,
		time: 1000
	});
}

// countdown
$('[data-countdown]').each(function () {
var $this = $(this), finalDate = $(this).data('countdown');
$this.countdown(finalDate, function (event) {
	$this.html(event.strftime('<div class="time-count"><span>%D</span>Days</div>'));
});
});


// scrollToTop
$.scrollUp({
	scrollName: 'scrollUp',
	topDistance: '300',
	topSpeed: 300,
	animation: 'fade',
	animationInSpeed: 200,
	animationOutSpeed: 200,
	scrollText: '<i class="fas fa-chevron-up"></i>',
	activeOverlay: false,
});


// WOW active
function wowanimation() {
	var wow = new WOW({
		boxClass: 'wow',
		animateClass: 'animated',
		offset: 0,
		mobile: false,
		live: true
	});
	wow.init();
}


})(jQuery);