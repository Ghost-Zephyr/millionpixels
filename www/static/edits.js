$('#getPixel').submit(function(event){
	event.preventDefault();
	$.ajax({
        url: '/api/pixel',
        type: 'get',
        data: $(this).serialize(),
        success: function(data) {
          console.log(data)
        },
        statusCode: {
            //200: function() { console.log(data) },
            400: function() { $('#pixelinfo').text('Bad request, x and y only between 0 and 999'); $('#pixelinfo').attr('style', 'color: #C42069') }
        }
	})
})
