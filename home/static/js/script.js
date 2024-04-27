// Добавляем обработчики событий для каждой кнопки "Добавить"
const openButtons = document.querySelectorAll('.openPopup');
openButtons.forEach(function (button) {
    button.addEventListener('click', function () {
        const productId = button.getAttribute('data-product-id');
        const popupId = 'popup_' + productId;
        const backgroundId = 'popup-background_' + productId;
        document.getElementById(popupId).style.display = 'block';
        document.getElementById(backgroundId).style.display = 'block'; // Показать затемненный фон
    });
});


// Добавляем обработчики событий для каждой кнопки "Закрыть"
const closeButtons = document.querySelectorAll('.closePopup');
closeButtons.forEach(function (button) {
    button.addEventListener('click', function () {
        const productId = button.getAttribute('data-product-id');
        const popupId = 'popup_' + productId;
        const backgroundId = 'popup-background_' + productId;

        document.getElementById(popupId).style.display = 'none';
        document.getElementById(backgroundId).style.display = 'none'; // Удалить затемненный фон

    });
});


// Добавляем обработчики событий для каждой кнопки "Убрать"
const openRemoveButtons = document.querySelectorAll('.openPopupRemove');
openRemoveButtons.forEach(function (button) {
    button.addEventListener('click', function () {
        const productId = button.getAttribute('data-product-id');
        const removePopupId = 'removePopup_' + productId;
        const backgroundId = 'popup-background_' + productId;
        document.getElementById(removePopupId).style.display = 'block';
        document.getElementById(backgroundId).style.display = 'block'; // Показать затемненный фон
    });
});

// Добавляем обработчики событий для каждой кнопки "Закрыть"
const closeRemoveButtons = document.querySelectorAll('.closePopupRemove');
closeRemoveButtons.forEach(function (button) {
    button.addEventListener('click', function () {
        const productId = button.getAttribute('data-product-id');
        const removePopupId = 'removePopup_' + productId;
        const backgroundId = 'popup-background_' + productId;
        document.getElementById(removePopupId).style.display = 'none';
        document.getElementById(backgroundId).style.display = 'none'; // Удалить затемненный фон
    });
});


let mask = document.querySelector('.mask');

window.addEventListener('load', () => {
    mask.classList.add('_hide');
    setTimeout(() => {
        mask.remove()
    }, 1000)
});
