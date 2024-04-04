// Добавляем обработчики событий для каждой кнопки "Добавить"
var openButtons = document.querySelectorAll('.openPopup');
openButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        var productId = button.getAttribute('data-product-id');
        var popupId = 'popup_' + productId;
        document.getElementById(popupId).style.display = 'block';
    });
});

// Добавляем обработчики событий для каждой кнопки "Закрыть"
var closeButtons = document.querySelectorAll('.closePopup');
closeButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        var productId = button.getAttribute('data-product-id');
        var popupId = 'popup_' + productId;
        document.getElementById(popupId).style.display = 'none';
    });
});
