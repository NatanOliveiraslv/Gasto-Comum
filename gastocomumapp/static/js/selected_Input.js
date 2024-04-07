$(document).ready(function() {
    var selectedEmails = [];
  
    $('#userInput').on('input', function() {
      var userInput = $(this).val();
      $('#userList').empty();
      if (userInput.length > 0) {
        $.ajax({
          url: '/search_users/',
          type: 'GET',
          data: {'query': userInput},
          success: function(data) {
            var uniqueUsers = Array.from(new Set(data));
            uniqueUsers.forEach(function(user) {
              var email = user.email;
              if (!selectedEmails.includes(email)) {
                if ($('#userList').find('.autocomplete-item:contains("' + email + '")').length === 0) {
                  $('#userList').css({'margin-right':'auto', 'padding-left':'8px', 'margin-bottom':'8px'});
                  $('#userList').append('<div class="autocomplete-item">' + email + '</div>');
                }
              }
            });
          }
        });
      }
    });
  
    $(document).on('click', '.autocomplete-item', function() {
      var selectedEmail = $(this).text();
      if (!selectedEmails.includes(selectedEmail)) {
        selectedEmails.push(selectedEmail);
        updateEmailContainer();
        $('#userList').empty();
      }
      $(this).remove();
      $('#userInput').val('');
    });
  
    $(document).on('click', '.remove-email', function() {
      var emailToRemove = $(this).parent().data('email');
      var index = selectedEmails.indexOf(emailToRemove);
      if (index !== -1) {
        selectedEmails.splice(index, 1);
        updateEmailContainer();
      }
    });
  
    function updateEmailContainer() {
      var EmailContainer = $('#emailContainer');
      EmailContainer.empty();
      selectedEmails.forEach(function(email) {
        var emailBox = $('<input type="hidden" id="emails" name="emails" value="' + email + '">' + '<div class="email-box">' + email + '<span class="remove-email">X</span></div>');
        emailBox.data('email', email); // Armazena o email como um atributo de dados
        EmailContainer.append(emailBox);
      });
    }
});

$(document).ready(function() {
  $('.classDivided .arrow').on('click', function() {
    $('#userInput').toggle();
    if ($('#divUserInput').css('display') === 'flex') {
      // Se estiver sendo exibido, mude para display: none
      $('#divUserInput').css('display', 'none');
    } else {
      // Se estiver oculto, mude para display: flex
      $('#divUserInput').css('display', 'flex');
    }
  });
});

function validateForm() {
  var emailContainer = document.getElementById("emailContainer");
  if (emailContainer.innerText.trim() === "") {
    alert("Por favor, preencha o campo de email antes de enviar o formulário.");
    return false; // Impede o envio do formulário
  }
  return true; // Permite o envio do formulário
}
