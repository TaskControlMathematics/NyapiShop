$(document).ready(function(){
 function htmSlider(){
  /* Зададим следующие параметры */
  /* обертка слайдера */
  var slideWrap = jQuery('.slide-wrap');
  /* кнопки вперед/назад и старт/пауза */
  var nextLink = jQuery('.next-slide');
  var prevLink = jQuery('.prev-slide');
  var playLink = jQuery('.auto');
  /* Проверка на анимацию */
  var is_animate = false;
  /* ширина слайда с отступами */
  var slideWidth = jQuery('.slide-item').outerWidth();
  /* смещение слайдера */
  var scrollSlider = slideWrap.position().left - slideWidth;
        
  /* Клик по ссылке на следующий слайд */
  nextLink.click(function(){
   if(!slideWrap.is(':animated')) {
    slideWrap.animate({left: scrollSlider}, 500, function(){
     slideWrap
      .find('.slide-item:first')
      .appendTo(slideWrap)
      .parent()
      .css({'left': 0});
    });
   }
  });

  /* Клик по ссылке на предыдующий слайд */
  prevLink.click(function(){
   if(!slideWrap.is(':animated')) {
    slideWrap
     .css({'left': scrollSlider})
     .find('.slide-item:last')
     .prependTo(slideWrap)
     .parent()
     .animate({left: 0}, 500);
   }
  });
        
  /* Функция автоматической прокрутки слайдера */
  function autoplay(){
   if(!is_animate){
    is_animate = true;
    slideWrap.animate({left: scrollSlider}, 500, function(){
     slideWrap
      .find('.slide-item:first')
      .appendTo(slideWrap)
      .parent()
      .css({'left': 0});
     is_animate = false;
    });
   }
  }
        
  /* Клики по ссылкам старт/пауза */
  playLink.click(function(){
   if(playLink.hasClass('play')){
    /* Изменяем клас у кнопки на клас паузы */
    playLink.removeClass('play').addClass('pause');
    /* Добавляем кнопкам вперед/назад клас который их скрывает */
    jQuery('.navy').addClass('disable');
    /* Инициализируем функцию autoplay() через переменную
       чтобы потом можно было ее отключить
    */
    timer = setInterval(autoplay, 1000);
   } else {
    playLink.removeClass('pause').addClass('play');
    /* показываем кнопки вперед/назад */
    jQuery('.navy').removeClass('disable');
    /* Отключаем функцию autoplay() */
    clearInterval(timer);
   }
  });

 }
 
 /* иницилизируем функцию слайдера */
 htmSlider();
    $('.cart-container').mouseenter(function(){
        $('.animate_checkout').css('visibility','visible')
        $('.static-navbar-right-cart-image').css('margin-left' , "-70px")
        $('.static-navbar-right-cart-count').css('margin-left' , "-10px")
        $('.static-navbar-right-cart-count').css('background-color','black')
    });

    $('.cart-container').mouseleave(function(){
        $('.animate_checkout').css('visibility','hidden')
        $('.static-navbar-right-cart-image').css('margin-left' , "0px")
        $('.static-navbar-right-cart-count').css('margin-left' , "45px")
        $('.static-navbar-right-cart-count').css('background-color','rgb(139, 49, 145)')
    });
    // $('.checkout_button').mouseenter(function(){
    //   $('.cart-container').animate({
    //     width:"150",
    //   }, 100);

    // });
    var menu_element = $(".menu_button");
    var src_element = $(".search_button");
    var cho_element = $('.checkout_button')
    var menu_height_el = menu_element.offset().top;
    
    
    $("body").css({
      "width": menu_element.outerWidth(),
      "height": menu_element.outerHeight()
    });

    $(window).scroll(function() {
      
      if($(window).scrollTop() > menu_height_el) {
      
        menu_element.addClass("fixed");

      } else {
      
        menu_element.removeClass("fixed");

      }

    });
    $(window).scroll(function() {
      
      if($(window).scrollTop() > menu_height_el) {
      
        src_element.addClass("fixed");

      } else {
      
        src_element.removeClass("fixed");

      }

    });
     $(window).scroll(function() {
      
      if($(window).scrollTop() > menu_height_el) {
      
        cho_element.addClass("fixed");

      } else {
      
        cho_element.removeClass("fixed");

      }

    });

});