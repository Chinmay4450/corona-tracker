$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#nameInput').val(),
				email : $('#emailInput').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

				$("#totalcases").text(data['totalcases']),
				$("#recovered").text(data['recovered']),
				$("#death").text(data['death']),
				$("#active").text(data['active'])
		
		});

		event.preventDefault();

	});

});
