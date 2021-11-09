$(document).ready(function(){
	var thispage = window.location.href	
	// console.log(thispage)
	var page_num = thispage.split("/").pop()
	// var page_left = Number(page_num) - 1
	// var page_right = Number(page_num) + 1
	// var page_left_left = Number(page_num) - 2
	if (thispage == "http://127.0.0.1:8000/" || thispage == "http://127.0.0.1:8000/p/1" ){
		$('.left_page').css('border-radius' , '50%').css('border' , '1px solid')

	}
	else{
		$('.center_page').css('border-radius' , '50%').css('border' , '1px solid')
	}
	var count = $('.producttobasket').length;
	var catalog_height = (count / 3)
	if (Number.isInteger(catalog_height)){
		var column_count  = Number(Math.floor(catalog_height) ) 
	}
	else{
		var column_count  = Number(Math.floor(catalog_height) ) + 1
	}
	
	catalog_height = column_count * 780
	// console.log(column_count)
	$('.popular-wrapper-list').css('height',catalog_height+'px')


	var form = $('.producttobasket');
	// console.log('form:',form)
	form.on('submit' , function(e){
		e.preventDefault();
		console.log('in form')

		var count_product = 1
		console.log('count:',count_product)
		// console.log($('. button'))

		// $('.card-buy').click(function(){
		// 	product_id =$(this).data('product_id');
		// 	// console.log(asd)
		// 	});
		// console.log($(this));
		product_id = $(this).find('button').data('product_id');
		// var product_id = $('.producttobasket [data-product_id]')
		// // var product_id  = $('.card-buy').data('product_id');
		// console.log('product_id:',product_id)
		// $('.card-buy').each(function(e){
		// 	e.
		// })
		var data = {};
		data.product_id = product_id;
		data.count = count_product;
		// console.log(data)

		var csrf_token = $('.producttobasket [name = "csrfmiddlewaretoken"]').val();//Обработка пост запроса
		data["csrfmiddlewaretoken"] = csrf_token;
		var url = form.attr('action');
		// console.log(url)

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

	});
	$('.filter_form').change(function(){
		$('#qwe_form').submit();
	})




});
