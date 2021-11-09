$(document).ready(function(){
	// var catalog = window.location.href.split("/")[4].split("%20")[1]
	// var catalog_for_link = window.location.href.split("/")[4]
	var thispage = window.location.href
	var page_num = thispage.split("/").pop()
	console.log(thispage)
	console.log(page_num)
	// var page_left = Number(page_num) - 1
	// var page_right = Number(page_num) + 1
	// var page_left_left = Number(page_num) - 2
	if (thispage == "http://127.0.0.1:8000/catalog/" + page_num || thispage == "http://127.0.0.1:8000/catalog/page_num/p/1" ){
		$('.left_page_catalog').css('border-radius' , '50%').css('border' , '1px solid')
	}
	else{
		$('.center_page_catalog').css('border-radius' , '50%').css('border' , '1px solid')
	}
	// var link = "http://127.0.0.1:8000/catalog/" + catalog_for_link
	// var page_num = Number(thispage.split("/").pop())
	// console.log(page_num)
	
	// if (catalog == 'anime'){
	// 	var last_page = 313		
	// }
	// if (catalog == 'manga'){
	// 	var last_page = 30		
	// }
	// if (catalog == 'figures'){
	// 	var last_page = 28		
	// }
	// if (catalog == 'kigurumi'){
	// 	var last_page = 6		
	// }
	// if (catalog == 'food'){
	// 	var last_page = 25		
	// }
	// if (catalog == 'color_lenses'){
	// 	var last_page = 17		
	// }
	// if (catalog == 'other'){
	// 	var last_page = 8		
	// }
	// if (catalog == 'kpop'){
	// 	var last_page = 25
	// }
	// var page_left_left = last_page - 2
	// var page_prev_last  = last_page - 1
	// var page_left = page_num - 1
	// var page_right = page_num + 1
	// $('.first-page_catalog').html('<a href =  ' +link  + '>' + '...' + '</a>' )
	// $('.last_page_catalog').html('<a href =  ' +link + '/p/' + last_page + '>' + '...' + '</a>' )
	// if (thispage == link || thispage == link + '/p/2'){
	// 	$('.first-page_catalog').css('visibility' , 'hidden')
	// }
	// if(page_num >=page_left_left ){
	// 	$('.last_page_catalog').css('visibility' , 'hidden')
	// }
	// if (thispage == link){
	// 	$('.prev-page_catalog').html('<span>'+'<--' + '</span>')
	// 	$('.left_page_catalog').html('<a href = ' + link  +'>' +1+ '</a>')
	// 	$('.center_page_catalog').html('<a href = ' + link+'/p/2' +'>' +2+ '</a>')
	// 	$('.right_page_catalog').html('<a href = ' + link + '/p/3'+'>' +3+ '</a>')
	// 	$('.next_page_catalog').html('<a href = ' + link + '/p/2'+'>' +'-->'+ '</a>')
	// 	$('.left_page_catalog').css('border-radius' , '50%').css('border' , '1px solid')
	// }
	// if (page_num == last_page){
	// 	$('.prev-page_catalog').html('<a href = ' + link+'/p/'+page_left +'>' +'<--'+ '</a>')
	// 	$('.next_page_catalog').html('<a href = ' + link + '/p/2'+'>' +'-->'+ '</a>')
	// 	$('.left_page_catalog').html('<a href = ' + link  +'/p/' +page_left_left+ '>' +page_left_left+ '</a>')
	// 	$('.center_page_catalog').html('<a href = ' + link+'/p/'+page_left +'>' +page_left+ '</a>')
	// 	$('.right_page_catalog').html('<a href = ' + link + '/p/'+last_page+'>' +last_page+ '</a>')
	// 	$('.right_page_catalog').css('border-radius' , '50%').css('border' , '1px solid')
	// }
	// if(page_num >= 2 && page_num <=page_prev_last){
	// 	$('.prev-page_catalog').html('<a href = '+link + '/p/' + page_left + '>' + '<--' + '</a>')
	// 	$('.left_page_catalog').html('<a href = '+link + '/p/' + page_left + '>' + page_left + '</a>')
	// 	$('.center_page_catalog').html('<a href = ' + link+'/p/'+page_num +'>' +page_num+ '</a>')
	// 	$('.right_page_catalog').html('<a href = '+link + '/p/' + page_right + '>' + page_right + '</a>')
	// 	$('.next_page_catalog').html('<a href = '+link + '/p/' + page_right + '>' + '-->' + '</a>')
	// 	$('.center_page_catalog').css('border-radius' , '50%').css('border' , '1px solid')

	// }
	/*
	if( thispage == "http://127.0.0.1:8000/p/449"){
		$('.last_page').css('visibility' , 'hidden')
		$('.left_page').html('<a href = http://127.0.0.1:8000/p/' + Number(page_left_left) + '>' + page_left_left + '</a>')
		$('.center_page').html('<a href = http://127.0.0.1:8000/p/' + Number(page_left) + '>' + page_left + '</a>')
		$('.right_page').html('<a href = http://127.0.0.1:8000/p/' + Number(page_num) + '>' + page_num + '</a>')
		$('.right_page').css('border-radius' , '50%').css('border' , '1px solid')
		$('.next_page').html('<span>' + '-->' + '</span>')
	}

	if (Number(page_num) >= 3 && Number(page_num) <=448){
		
		$('.left_page').html('<a href = http://127.0.0.1:8000/p/' + Number(page_left) + '>' + page_left + '</a>')
		$('.center_page').html('<a href = http://127.0.0.1:8000/p/' + Number(page_num) + '>' + page_num + '</a>')
		$('.right_page').html('<a href = http://127.0.0.1:8000/p/' + Number(page_right) + '>' + page_right + '</a>')
		$('.center_page').css('border-radius' , '50%').css('border' , '1px solid')

	}
	if( Number(page_num) != 449){
		$('.next_page').html('<a href = http://127.0.0.1:8000/p/' + Number(page_right) + '>' + '-->' + '</a>')
	}
	if( Number(page_num) >= 2){
		$('.prev-page').html('<a href = http://127.0.0.1:8000/p/' + Number(page_left) + '>' + '<--' + '</a>')
	}
	if (thispage == "http://127.0.0.1:8000/"){
		$('.prev-page').html('<span>' + '<--' + '</span>')
		$('.next_page').html('<a href = http://127.0.0.1:8000/p/' + 2 + '>' + '-->' + '</a>')
		$('.left_page').css('border-radius' , '50%').css('border' , '1px solid')

	}
	if (thispage == "http://127.0.0.1:8000/p/2"){
		$('.center_page').css('border-radius' , '50%').css('border' , '1px solid')

	}
	if (Number(page_num) >= 448){
		$('.last_page').css('visibility' , 'hidden')

	}*/
});