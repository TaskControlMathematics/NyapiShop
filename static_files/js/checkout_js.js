$(document).ready(function(){
	function calculate_all_total_price(){
		var sum = 0;
		$('.basket_product_info_total_price_value').each(function(){
			sum = sum + Number($(this).text())
		})
		var nds = sum * 0.1
		$('#total_price_in_basket').html('<span>'+sum+' руб.</span>')
		$('#nds_in_basket').html('<span>'+ nds +' руб.</span>')
		$('#all_total_price_in_basket').html('<span>'+sum+' руб.</span>')

	}
	$('.count-plus_checkout').click(function(){

		var this_tr = $(this).closest('tr');
		var price_one = Number(this_tr.find('.basket_product_info_price_per_item_value').text());
		// console.log(price_one)
		var count = this_tr.find('.input_count');

		// count.val(Number(count) + 1 )
		count.val(Number(count.val()) + 1 );
		var count_item = Number(count.val())
		var total_price = Number(count_item * price_one);
		// console.log(count_item)
		// console.log(total_price)
		if (count_item != 1){
			$('.count-minus_checkout').prop("disabled", false); 

		}
		this_tr.find('.basket_product_info_total_price_value').html(total_price)
		// console.log(count);
		calculate_all_total_price();
		// count.val(Number(count.val()) + 1 );
	});
	$('.count-minus_checkout').click(function(){

		var this_tr = $(this).closest('tr');
		var price_one = Number(this_tr.find('.basket_product_info_price_per_item_value').text());
		// console.log(price_one)
		var count = this_tr.find('.input_count');

		// count.val(Number(count) + 1 )
		count.val(Number(count.val()) - 1 );
		
		var count_item = Number(count.val())
		var total_price = Number(count_item * price_one);
		console.log(count_item)
		if (count_item == 1){
			// console.log('asdasdasdssdasdasdasdasdsadasdasdasdasd');
			$('.count-minus_checkout').prop("disabled", true); 

		}
		// else{
		// 	$('.count-minus_checkout').prop("disabled", false); 
		// }
		// console.log(total_price)
		this_tr.find('.basket_product_info_total_price_value').html(total_price)
		// console.log(count);
		calculate_all_total_price();
		// count.val(Number(count.val()) + 1 );
	});


	$('.basket_product_info_total_price_value').each(function(){
		var cur_tr = $(this).closest('tr')
		var cur_price_per_item = Number(cur_tr.find('.basket_product_info_price_per_item_value').text())
		var cur_count = Number(cur_tr.find('.input_count').val())
		// if (cur_count != 1){
		// 	console.log(cur_count);
		// 	$('.count-minus_checkout').prop("disabled", false); 
		// }
		// else{
		// 	$('.count-minus_checkout').prop("disabled", true); 
		// }
		var cur_total_price = cur_count * cur_price_per_item
		cur_tr.find('.basket_product_info_total_price_value').text(cur_total_price)
	})
	calculate_all_total_price();


	

	$(document).on('change' , ".input_count" , function(){
		var current_count = Number($(this).val())
		var current_tr = $(this).closest('tr')
		var current_price = Number(current_tr.find('.basket_product_info_price_per_item_value').text())
		var current_total_price = current_count * current_price
		var current_total_price_item = current_tr.find('.basket_product_info_total_price_value').text(current_total_price)

		calculate_all_total_price();
		
		/*
		$('.basket_product_info_total_price_value').text(current_total_price)*/
	})
	$('.option_type').each(function(){
		$(this).click(function(){
			$(this).children('.option_type_body').css('visibility','hidden');
			$(this).css('margin-top','50px')
			
		})
			
		
	})
	$('.delete_link').click(function(){
		var data = {};
		var cur_tr = $(this).parent().parent().parent();
		console.log(cur_tr)
		data.product_id = $(this).data("product_id");
		data.is_delete = true;
		console.log(data);
		// data.count = count_product;
		// console.log(data)
		var csrf_token = $('.chekout_form [name = "csrfmiddlewaretoken"]').val();//Обработка пост запроса
		data["csrfmiddlewaretoken"] = csrf_token;
		var url = "http://127.0.0.1:8000/orders/checkout/";
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
					$('.static-navbar-right-cart-count').html('<span>' + data.products_total_count + '</span>');
					cur_tr.html("");
					calculate_all_total_price();
				},
				error:function(){
					console.log('error');
				}
			})
	})
	$('.delete_all_product').click(function(){
		var data = {};
		var cur_tr = $('.basket_product');
		var csrf_token = $('.chekout_form [name = "csrfmiddlewaretoken"]').val();//Обработка пост запроса
		data["csrfmiddlewaretoken"] = csrf_token;
		data.is_delete_all = true;
		console.log(data)
		var url = "http://127.0.0.1:8000/orders/checkout/";
		$.ajax(
			{
				url:url,
				type:'POST',
				data:data,
				cache:true,
				success: function(data)
				{
					console.log("OK");
					$('.static-navbar-right-cart-count').html('<span>' + data.products_total_count + '</span>');
					$('.delete_all_product').html(" ")
					cur_tr.html("<div>Ваша корзина пуста</div>");
				},
				error:function(){
					console.log('error');
				}
			})
	})


	// $('.count-minus').click(function(){
	// 	var count = $('.input_count');
		
	// 	count.val(Number(count.val()) - 1 );
	// 	// if (count.val() != 1){
	// 	// 	$('.count-minus').attr('disabled','false')
	// 	// }

	// });

});
