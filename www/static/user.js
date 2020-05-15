$('#loginForm').submit(function(event){
	event.preventDefault();
	$.ajax({
        url: '/api/user/signin',
        type: 'post',
        data: $(this).serialize(),
        statusCode: {
            200: function() { window.location.replace('/'); },
            401: function() { $('#title').text('Wrong password!'); $('#title').attr('style', 'color: #C42069') },
            400: function() { $('#title').text('No such user.'); $('#title').attr('style', 'color: #C42069') }
        }
	})
})
$('#registerForm').submit(function(event){
  event.preventDefault()
  if ($('#pwd').serialize().slice(4) != $('#pwd1').serialize().slice(5)) {
    $('#title').text('Passwords does not match!')
    $('#title').attr('style', 'color: #C42069')
  }
  else {
    $.ajax({
      url: '/api/user/register',
      type: 'post',
      data: $(this).serialize(),
      statusCode: {
        200: function() { window.location.replace('/') },
        409: function() { $('#title').text('Nick taken.'); $('#title').attr('style', 'color: #C42069') },
        400: function() { $('#title').text('Could not create user.'); $('#title').attr('style', 'color: #C42069') }
      }
    })
  }
})
