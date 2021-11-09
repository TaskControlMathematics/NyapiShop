$(document).ready(function(){
	
	$('.count-plus').click(function(){
		// console.log(count)
		var count = $('.input-count input');
		// var cnt = count.val() + 1
		// $('.input-count input').attr('value',cnt);
		count.val(Number(count.val()) + 1 );
		var count_item = Number(count.val())
		// console.log(count_item)
		// console.log(total_price)
		if (count_item != 1){
			$('.count-minus').prop("disabled", false); 

		}
		// if (count.val() == 1){
		// 	console.log('sadasdasd');
		// }
		
		// .html('<input type="text" value="'+count+'"  name="input-count-input">');
	});
	$('.count-minus').click(function(){
		var count = $('.input-count input');
		
		count.val(Number(count.val()) - 1 );
		var count_item = Number(count.val())
		if (count_item == 1){
			// console.log('asdasdasdssdasdasdasdasdsadasdasdasdasd');
			$('.count-minus').prop("disabled", true); 

		}
		// if (count.val() != 1){
		// 	$('.count-minus').attr('disabled','false')
		// }

	});
	// var count = $('.input-count input').val();
	// $('.input-count input').on('change',function(){
	// 	console.log('ASD');
	// });
	// $(document).on('change',function(){
	// 	var cnt = $('.input-count input');
	// 	console.log('asdasd')
	// 	console.log(cnt)
	// })
	$('.count-minus').prop("disabled", true);
	var count_image = $('.product-main-page-card-left img').length
	var height_card = count_image*650
	$('.product-main-page-card').css('height' ,height_card+'px' )
	var form = $('#form-buy-product');
	form.on('submit' , function(e){
		e.preventDefault();
		console.log('in form')

		var count_product = $('.input-count input').val();
		console.log(count_product)

		var product_id  = $('.product-main-page-card-right-buy-buybtn-button').data('product_id');
		console.log(product_id)

		$('.static-navbar-right ul').append('<li>' +'id:' +product_id+ ' '+ 'count:'+count_product+ '</li>');
		var count_item_in_cart = $('.static-navbar-right-cart-count input')
		count_item_in_cart.val(Number(count_item_in_cart.val()) +1 );

		var data = {};
		data.product_id = product_id;
		data.count = count_product;
		console.log(data)
		var csrf_token = $('#form-buy-product [name = "csrfmiddlewaretoken"]').val();//Обработка пост запроса
		data["csrfmiddlewaretoken"] = csrf_token;
		var url = form.attr('action');
		console.log(url)

		$.ajax(
		{
			url:url,
			type:'POST',
			data:data,
			cache:true,
			success: function(data)
			{
				console.log("OK")
				$('.static-navbar-right-cart-count').html('<span>' + data.products_total_count + '</span>');
			},
			error:function(){
				console.log('error')
			}
		})

	})
	var desc = $('.desc_body').text()
	var description = $('.desc_body')
	var desc_array = desc.split(".")
	var desc_html = []
	$.each(desc_array,function(index,value){
		desc_html.push(value + "<p>");
	})
	description.html(desc_html.join(' '))

	$('.button_logout').click(function(){
		var data = {};
		data.user_logout = $(this).data("user_logout");
		data.logout = true;
		console.log(data);
		// data.count = count_product;
		// console.log(data)
		var csrf_token = $('.logout_user_form [name = "csrfmiddlewaretoken"]').val();//Обработка пост запроса
		data["csrfmiddlewaretoken"] = csrf_token;
		var url = "http://127.0.0.1:8000/user_info";
		// console.log(url)

		$.ajax(
		{
			url:url,
			type:'POST',
			data:data,
			cache:true,
			success: function(data)
			{
				console.log("OK");
			},
			error:function(){
				console.log('error');
			}
		})
	})
	$('.button_logout_setting').click(function(){
		var data = {};
		data.user_logout = $(this).data("user_logout");
		data.logout = true;
		console.log(data);
		// data.count = count_product;
		// console.log(data)
		var csrf_token = $('.logout_form_settings [name = "csrfmiddlewaretoken"]').val();//Обработка пост запроса
		data["csrfmiddlewaretoken"] = csrf_token;
		var url = "http://127.0.0.1:8000/user_info_setting";
		// console.log(url)

		$.ajax(
		{
			url:url,
			type:'POST',
			data:data,
			cache:true,
			success: function(data)
			{
				console.log("OK");
			},
			error:function(){
				console.log('error');
			}
		})
	})

	var details = document.querySelectorAll("details");
	for(i=0;i<details.length;i++) {
		details[i].addEventListener("toggle", accordion);
	}
	function accordion(event) {
		if (!event.target.open) return;
		var details = event.target.parentNode.children;
		for(i=0;i<details.length;i++) {
			if (details[i].tagName != "DETAILS" || 
				!details[i].hasAttribute('open') || 
				event.target == details[i]) {
				continue;
		}
		details[i].removeAttribute("open");
	}
}
});
