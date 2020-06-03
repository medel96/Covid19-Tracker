
"use strict"

/*****Ready function start*****/
$(document).ready(function() {
	$('#example').DataTable( {
		dom: 'Bfrtip',
		buttons: [
			'copy', 'csv', 'excel', 'pdf', 'print'
		],
		order:[[0,'desc']]
	} );
} );

$(document).ready(function() {
	$('#world').DataTable( {
		dom: 'Bfrtip',
		buttons: [
			'copy', 'csv', 'excel', 'pdf', 'print'
		],
		order:[[0,'desc']]
	} );
} );





/*****Ready function end*****/


/*****Load function start*****/
$(window).load(function () {
	window.setTimeout(function () {
		$.toast({
			heading: 'Welcome',
			text: 'Data is from open sources on the web, so there is no guarantee of accuracy.',
			position: 'bottom-right',
			loaderBg: '#00887A',
			icon: 'success',
			hideAfter: 4500,
			stack: 6
		});
	}, 1500);

	//Line Chart


});




/*****Load function* end*****/
