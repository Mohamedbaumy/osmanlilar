$(document).ready(function(){
    $('.owl-carousel').owlCarousel({
      rtl:true,
      loop:true,
      margin:10,
      nav:true,
      navText : ['<i class="fa fa-angle-right" aria-hidden="true"></i>','<i class="fa fa-angle-left" aria-hidden="true"></i>'],
      dots:false,
      responsive:{
          0:{
              items:1
          },
          600:{
              items:3
          },
          1000:{
              items:6
          }
      }
    })
    var $grid = $('.grid').isotope({
      // options
      itemSelector: '.grid-item',
      layoutMode: 'fitRows'
    });
    
    $(".filter .filter__cont ul > li").click(function(){
      $('.filter .filter__cont ul > li').removeClass('active');
      $(this).addClass('active');
    })
    
  });